from fastapi import APIRouter, UploadFile, WebSocket
from ..src.main_module import generate_videos, generate_subtitile_files, add_subtitle_to_video, extract_audio
import os

router = APIRouter(prefix="/highlight")

@router.post("/")
async def post_videofie(video_file: UploadFile):    
    contents = await video_file.read()
    file_type = video_file.content_type.split("/")[-1]
    input_path = f"./backend/data/processing.{file_type}"
    output_audio_path = "./backend/data/processing.wav"

    with open(input_path, "wb") as file:
        file.write(contents)

    extract_audio(input_path, output_audio_path)
    return {"status": True}

@router.websocket("/ws")
async def get_highlights(websocket: WebSocket):

    await websocket.accept()
    
    input_path = "./backend/data/processing.mp4"
    output_audio_path = "./backend/data/processing.wav"

    while True:
        text = await websocket.receive_text()
        
        if (text == "order_69"):
            result_paths, descriptions, tags = await generate_videos(path_input=input_path, 
                path_output=output_audio_path, 
                clips_path="./backend/data/clips",
                results_path="./backend/data/results")

            subtitle_files = await generate_subtitile_files(result_paths, subtitles_path="./backend/data/subtitles")
            await add_subtitle_to_video(False, subtitle_files, result_paths, subtitle_language="", results_path="./backend/static")

            files_to_remove = [input_path, output_audio_path]
            directories_to_remove = ["./backend/data/clips", "./backend/data/results", "./backend/data/subtitles"]

            for file in files_to_remove:
                if os.path.exists(file):
                    os.remove(file)

            for directory in directories_to_remove:
                for filename in os.listdir(directory):
                    filepath = os.path.join(directory, filename)
                    if os.path.isfile(filepath):
                        os.remove(filepath)

            filenames = os.listdir("./backend/static")
            new_filenames = [os.path.join("http://localhost:8000/static/", filename) for filename in filenames]
            await websocket.send_json({
                "filenames": new_filenames,
                "descriptions": descriptions,
                "tags": tags
            })

        
    
