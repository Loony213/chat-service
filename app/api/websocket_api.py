from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.websocket_service import handle_message  # Importa la función de servicio
import json

router = APIRouter()

ws_manager = {}  # Aquí gestionas las conexiones activas

@router.websocket("/ws/{email}")
async def websocket_endpoint(websocket: WebSocket, email: str):
    # Aceptar la conexión WebSocket
    await websocket.accept()
    ws_manager[email] = websocket

    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)  # Recibir los datos en formato JSON
            to_email = message_data.get("to")
            chat_id, msg = await handle_message(message_data)  # Guarda el mensaje en MongoDB

            if to_email in ws_manager:
                await ws_manager[to_email].send_json({
                    "sender": message_data.get("from"),
                    "message": msg
                })
            else:
                await websocket.send_json({
                    "sender": "Sistema",
                    "message": f"{to_email} no está conectado"
                })
    except WebSocketDisconnect:
        del ws_manager[email]
