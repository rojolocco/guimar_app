from fastapi import FastAPI #, File, UploadFile
from pathlib import Path

from fastapi.responses import FileResponse

app = FastAPI()

# Define the path to the static files directory
STATIC_FILES_DIR = Path(__file__).parent / "static"
print(STATIC_FILES_DIR)


@app.get("/")
async def home():
    # Serve the index.html file from the static files directory
    return FileResponse(STATIC_FILES_DIR / "index.html")
