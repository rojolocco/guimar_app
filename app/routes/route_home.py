# Create a fastapi route for homepage
from fastapi import APIRouter
from fastapi.responses import FileResponse
from ..database.crud import get_all_data, insert_data

from pathlib import Path

STATIC_FILES_DIR = Path(__file__).parent.parent / "static"

router_home = APIRouter()


@router_home.get("/")
async def home():
    return FileResponse(STATIC_FILES_DIR / "index.html")

@router_home.get("/api")
async def api():
    res = get_all_data("countries")
    return res

@router_home.post("/api")
async def api(data: dict):
    res = insert_data("countries", data)
    return res