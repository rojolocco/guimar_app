# Create a fastapi route for homepage
from fastapi import APIRouter
from fastapi.responses import FileResponse

from pathlib import Path

STATIC_FILES_DIR = Path(__file__).parent.parent / "static"
print(STATIC_FILES_DIR)

router_home = APIRouter()


@router_home.get("/")
async def home():
    # Serve the index.html file from the static files directory
    return FileResponse(STATIC_FILES_DIR / "index.html")
