# Create a fastapi route for homepage
from fastapi import APIRouter
from fastapi.responses import FileResponse
from ..database.crud import get_all_data, insert_data, delete_data
from ..database.crud import delete_all_data

from pathlib import Path

STATIC_FILES_DIR = Path(__file__).parent.parent / "static"

router_home = APIRouter()


@router_home.get("/")
async def home():
    return FileResponse(STATIC_FILES_DIR / "index.html")


@router_home.get("/api")
async def fetch_data():
    res = get_all_data("countries")
    return res


@router_home.post("/api")
async def new_data(data: dict):
    res = insert_data("countries", data)
    return res


@router_home.delete("/api")
async def delete_data_id(id: int):
    res = delete_data("countries", id)
    return res


@router_home.delete("/api")
async def remove_all_data():
    res = delete_all_data("countries")
    return res
