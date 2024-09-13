# app/routes/route_api.py
from fastapi import APIRouter

# Create an instance of APIRouter for WhatsApp API routes
router_api = APIRouter()

# Define a route for the WhatsApp API controller
@router_api.get('/whatsapp')
def hello() -> dict:
    """
    Handles GET requests to the /whatsapp endpoint.

    Returns:
        dict: A dictionary containing a message indicating the purpose of the endpoint.
    """
    return {"message": "This is the WhatsApp API"}

# Note: The function is simple and serves as a placeholder. In a larger application,
# it can be refactored or expanded by separating logic into different layers or classes if needed.
