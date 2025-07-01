from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.websocket_api import router

# Inicializamos la aplicación FastAPI
app = FastAPI()

# Configuración del middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes limitar los orígenes según tus necesidades
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los encabezados
)

# Incluir las rutas de WebSocket
app.include_router(router)
