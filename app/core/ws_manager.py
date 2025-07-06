from fastapi import WebSocket
from typing import Dict

class WebSocketManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, email: str):
        await websocket.accept()
        self.active_connections[email] = websocket

    async def disconnect(self, email: str):
        self.active_connections.pop(email, None)

    async def send_message(self, to_email: str, message: dict):
        websocket = self.active_connections.get(to_email)
        if websocket:
            await websocket.send_json(message)
        else:
            return None
