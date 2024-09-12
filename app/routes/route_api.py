from fastapi import APIRouter


router_api = APIRouter()

# Create aa route for the api controller


@router_api.get('/whatsapp')
def hello():
    return {"message": f"This is the whatsapp api"}
