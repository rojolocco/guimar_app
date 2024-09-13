# app/main.py
from fastapi import FastAPI
from .routes.route_home import router_home
from .routes.route_api import router_api
from .routes.route_db import router_db


# Create an instance of the FastAPI application
app = FastAPI()


# Function to include routes into the FastAPI app
def include_routes(app: FastAPI) -> None:
    """
    Includes all route modules into the FastAPI app instance.

    Args:
        app (FastAPI): The main application instance of FastAPI.
    """
    app.include_router(router_home, tags=["Home"])
    app.include_router(router_api, prefix="/api", tags=["WhatsApp"])
    app.include_router(router_db, prefix= "/db", tags=["Database"])


# Main entry point for adding routes
include_routes(app)
