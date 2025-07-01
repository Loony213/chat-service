from app.core.ws_manager import WebSocketManager
from app.models.message import Message

class WebSocketService:
    def __init__(self, ws_manager: WebSocketManager):
        self.ws_manager = ws_manager

    async def handle_message(self, websocket, email: str, message: Message):
        to_email = message.to
        msg = message.message
        sender = message.from_email

        if to_email in self.ws_manager.active_connections:
            await self.ws_manager.send_message(to_email, {
                "sender": sender,
                "message": msg
            })
        else:
            await websocket.send_json({
                "sender": "Sistema",
                "message": f"{to_email} no está conectado"
            })
