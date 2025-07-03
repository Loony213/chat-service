from fastapi import APIRouter
from app.services.websocket_service import messages_collection

router = APIRouter()

@router.get("/messages/{chat_id}")
async def get_messages(chat_id: str):
    messages = messages_collection.find({"chat_id": chat_id})
    return list(messages)  # Devuelve los mensajes como una lista
