# app/routes/route_home.py
from fastapi import APIRouter
from fastapi.responses import FileResponse
from pathlib import Path


# Define the directory path for static files
STATIC_FILES_DIR = Path(__file__).parent.parent / "static"


# Initialize the APIRouter instance for the homepage routes
router_home = APIRouter()


@router_home.get("/")
async def home():
    """
    Handles GET requests to the root endpoint.

    Returns:
        FileResponse: Serves the 'index.html' file located in the static directory as the homepage.
    """
    return FileResponse(STATIC_FILES_DIR / "index.html")
