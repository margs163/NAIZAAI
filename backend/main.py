from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .routers.highlight import router as highlight_router
from .routers.instagram import router as instagram_router

app = FastAPI(title="Highlight Cutter")
app.include_router(highlight_router, tags=["highlight"])
app.include_router(instagram_router, tags=["instagramm"])
app.mount("/static", app = StaticFiles(directory="./backend/static"), name="static")

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {"message": "api works"}