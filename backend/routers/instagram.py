from fastapi import APIRouter
from pydantic import BaseModel
from instagrapi import Client
from pathlib import Path


router = APIRouter(prefix="/upload")

class UploadClass(BaseModel):
    login: str
    password: str
    video_path: str
    video_caption: str

@router.post("/")
async def upload_video_on_instagram(upload_body: UploadClass):
    login, password = upload_body.login, upload_body.password

    cl = Client()
    cl.login(login, password)

    cl.video_upload(Path(upload_body.video_path), upload_body.video_caption)
    return {"status": True}
