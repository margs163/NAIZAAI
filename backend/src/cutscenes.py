from scenedetect import open_video, SceneManager, SceneList, FrameTimecode
from scenedetect.detectors import ContentDetector
from scenedetect.video_splitter import split_video_ffmpeg
from pathlib import Path
from pprint import pprint

def split_long_scenes(scene_list: SceneList, max_duration_sec=60):
    new_scene_list = []
    for start_time, end_time in scene_list:
        duration = end_time.get_seconds() - start_time.get_seconds()
        if duration > max_duration_sec:
            # Split at midpoint
            mid_seconds = start_time.get_seconds() + duration / 2
            mid_time = FrameTimecode(mid_seconds, fps=start_time.get_framerate())
            new_scene_list.append((start_time, mid_time))
            new_scene_list.append((mid_time, end_time))
        else:
            new_scene_list.append((start_time, end_time))
    return new_scene_list

def split_video_into_scenes(video_path: str, output_dir: str, threshold=27.0):
    timestampts = []
    video = open_video(video_path)
    scene_manager = SceneManager()
    scene_manager.add_detector(
        ContentDetector(threshold=threshold))
    scene_manager.detect_scenes(video, show_progress=True)
    scene_list = scene_manager.get_scene_list()
    scene_list = split_long_scenes(scene_list, max_duration_sec=60)
    split_video_ffmpeg(video_path, scene_list, show_progress=True, output_dir=Path(output_dir))
    for scene in scene_list:
       timestampts.append((scene[0].get_timecode(), scene[1].get_timecode()))
    return timestampts

if __name__ == "__main__":
    pprint(split_video_into_scenes('./audio/test.mp4', './clips'))