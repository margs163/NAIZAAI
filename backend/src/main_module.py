from .audio import transcribe_audio_in_chunks, extract_audio
from .cutscenes import split_video_into_scenes
from .lcscript import app, seconds_to_precise_timestamp
from pathlib import Path
import asyncio
from .timescript import timestamp_includes, timestamps_overlap, combine_videos_moviepy
from pprint import pprint
from typing import List
import ffmpeg
import math

path_raw = "./audio/test.mp4"
output_path = "./audio/output.wav"

def add_leading_zeros(number, total_length=3):
    return str(number).zfill(total_length)

def format_time(seconds):
    hours = math.floor(seconds / 3600)
    seconds %= 3600
    minutes = math.floor(seconds / 60)
    seconds %= 60
    milliseconds = round((seconds - math.floor(seconds)) * 1000)
    seconds = math.floor(seconds)
    formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:01d},{milliseconds:03d}"

    return formatted_time

def overlapping_highlights(h_time: List[tuple[str, str]]):
    h_time_copy = h_time.copy()
    for index, time in enumerate(h_time_copy):
        if (index != len(h_time_copy) - 1):
            if timestamp_to_seconds(h_time_copy[index + 1][0]) - timestamp_to_seconds(time[1]) < 10:
                    h_time_copy[index] = (time[0], h_time_copy[index + 1][1])
                    del h_time_copy[index + 1]
    return h_time_copy

def timestamp_to_seconds(timestamp: str) -> float:
    timestamp = timestamp.replace('.', ':')
    parts = timestamp.split(':')
    if len(parts) != 4:
        raise ValueError("Timestamp must be in HH:MM:SS,MMM or HH:MM:SS:MMM format")
    hours, minutes, seconds, milliseconds = map(int, parts)
    total_seconds = hours * 3600 + minutes * 60 + seconds + milliseconds / 1000.0
    return total_seconds

async def generate_videos(path_input: str, path_output: str , clips_path: str ="./clips/", results_path: str ="./results"):
    result_paths = []
    saved_clips = {}
    existing_paths = []
    result = transcribe_audio_in_chunks(Path(path_output))
    state = await app.ainvoke({"transcriptions": result})
    h_time_r = state['highlight']
    h_time = [meta.timestamp for meta in h_time_r]
    h_description = [meta.description for meta in h_time_r]
    h_tags = [meta.tags for meta in h_time_r]
    h_time = overlapping_highlights(h_time)

    timestamps = split_video_into_scenes(path_input, clips_path)

    for index_h, h in enumerate(h_time):
            saved_clips.update({str(index_h): []})
            for index_t, t in enumerate(timestamps):
                print(f"Highlight: {h}", f", includes Timestamp: {t}", timestamp_includes(t, h) or timestamps_overlap(t, h))
                path = f"{clips_path}/processing-Scene-{add_leading_zeros(index_t + 1)}.mp4"
                if (timestamp_includes(t, h) or timestamps_overlap(t, h)):
                    existing_paths.append(path)
                    # saved_clips[str(index_h)].append(f"./clips/test-Scene-{add_leading_zeros(index_t - 1)}.mp4")
                    saved_clips[str(index_h)].append(path)

    for index_h, h in enumerate(h_time):
        path = f"{results_path}/result-{index_h}.mp4"
        if (saved_clips[str(index_h)]):
            result_paths.append(path)
            combine_videos_moviepy(saved_clips[str(index_h)], f"{results_path}/result-{index_h}.mp4")
    
    return (result_paths, h_description, h_tags)

async def add_subtitle_to_video(soft_subtitle, subtitle_files, video_files, subtitle_language, results_path="./resultSub"):
    for index, video in enumerate(video_files):
        video_input_stream = ffmpeg.input(video)
        output_video = f"{results_path}/output-result-{index}.mp4"
        subtitle_file = subtitle_files[index]
        subtitle_input_stream = ffmpeg.input(subtitle_file)
        subtitle_track_title = subtitle_file.replace(".srt", "")

        if soft_subtitle:
            stream = ffmpeg.output(
                video_input_stream, subtitle_input_stream, output_video, **{"c": "copy", "c:s": "mov_text"},
                **{"metadata:s:s:0": f"language={subtitle_language}",
                "metadata:s:s:0": f"title={subtitle_track_title}"}
            )
            ffmpeg.run(stream, overwrite_output=True)
        else:
            stream = ffmpeg.output(
                video_input_stream,
                output_video,
                vf=f"subtitles={subtitle_file}"
            )
            ffmpeg.run(stream, overwrite_output=True)

async def generate_subtitile_files(result_paths: List[str], subtitles_path="./subtitles"):
    subtitle_files = []
    for index, path in enumerate(result_paths):
        text = ""
        result = transcribe_audio_in_chunks(Path(path))
        
        subtitle_file = f"{subtitles_path}/sub-{index}.en.srt"
        subtitle_files.append(subtitle_file)
        for index, segment in enumerate(result["segments"]):
            segment_start = format_time(segment["start"])
            segment_end = format_time(segment["end"])
            text += f"{str(index+1)} \n"
            text += f"{segment_start} --> {segment_end} \n"
            text += f"{segment['text']} \n"
            text += "\n"

        with open(subtitle_file, "w") as f:
            f.write(text)

    return subtitle_files

async def main():
    result_paths, descriptions, tags = await generate_videos()
    subtitle_files = await generate_subtitile_files(result_paths)
    await add_subtitle_to_video(True, subtitle_files, result_paths, subtitle_language="en")

if __name__ == "__main__":
    asyncio.run(main())