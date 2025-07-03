import json
from pymongo import MongoClient
from datetime import datetime

# Conexión a MongoDB
client = MongoClient("mongodb://44.193.21.197:27017/")
db = client["chat_db"]  # Base de datos
messages_collection = db["messages"]  # Colección de mensajes

async def handle_message(data):
    sender = data.get("from")
    to_email = data.get("to")
    msg = data.get("message")
    chat_id = f"{sender}_{to_email}" if sender < to_email else f"{to_email}_{sender}"
    
    # Guardar el mensaje en MongoDB
    messages_collection.insert_one({
        "chat_id": chat_id,
        "sender_id": sender,
        "receiver_id": to_email,
        "message": msg,
        "timestamp": data.get("timestamp")
    })
    
    return chat_id, msg  # Retorna el chat_id para la consulta de mensajes
