from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Permitir acceso desde el frontends
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia por tu dominio en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

connected_users = {}

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await websocket.accept()
    connected_users[username] = websocket

    try:
        while True:
            data = await websocket.receive_text()
            for user, conn in connected_users.items():
                if conn != websocket:
                    await conn.send_json({"sender": username, "message": data})
    except WebSocketDisconnect:
        del connected_users[username]
