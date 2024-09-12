from fastapi import FastAPI
from .routes.route_home import router_home
from .routes.route_api import router_api

app = FastAPI()

# Include routes
app.include_router(router_home, tags=["Home"])
app.include_router(router_api, prefix="/api", tags=["WhatsApp API"])
