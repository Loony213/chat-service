from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.models.message import Message
from app.services.websocket_service import WebSocketService
from app.core.ws_manager import WebSocketManager
import json

router = APIRouter()

ws_manager = WebSocketManager()
websocket_service = WebSocketService(ws_manager)

@router.websocket("/ws/{email}")
async def websocket_endpoint(websocket: WebSocket, email: str):
    # Verificar si ya existe una conexión y cerrarla si es necesario
    if email in ws_manager.active_connections:
        await ws_manager.active_connections[email].close()
    
    # Aceptar la nueva conexión
    await websocket.accept()
    # Añadir la conexión al manager
    ws_manager.active_connections[email] = websocket
    
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            to_email = message_data.get("to")
            msg = message_data.get("message")
            sender = message_data.get("from")

            if to_email in ws_manager.active_connections:
                # Enviar el mensaje al destinatario
                await ws_manager.active_connections[to_email].send_json({
                    "sender": sender,
                    "message": msg
                })
            else:
                # Si el destinatario no está conectado, informar al remitente
                await websocket.send_json({
                    "sender": "Sistema",
                    "message": f"{to_email} no está conectado"
                })
    except WebSocketDisconnect:
        # Manejar la desconexión del WebSocket
        ws_manager.active_connections.pop(email, None)  # Eliminar la conexión del manager
    except Exception as e:
        # Manejo de otros errores
        print(f"Error en WebSocket: {str(e)}")
        # Opcionalmente, manejar el error o realizar algún reintento
