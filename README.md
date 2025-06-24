
# 💬 Chat Service

This microservice is part of the **Distribuida** system and enables **real-time communication** between users using WebSockets. Built with **FastAPI**, it allows clients to join a live chat and exchange messages.

---

## 📌 Features

- 🔌 WebSocket endpoint at `/ws/{username}`
- 🧍 Tracks connected users
- 💬 Broadcasts messages to all participants
- 🔄 Supports reconnect logic from the frontend

---

## 🧩 Architecture

- 🧱 Style: Minimal, standalone microservice
- 🌐 Protocol: WebSocket (FastAPI)
- 🐍 Language: Python 3.11+
- 🐳 Containerized with Docker

---

## 📁 Project Structure

```
chat-service/
├── .github/               # GitHub Actions or workflows (if used)
├── app.py                 # Main FastAPI app with WebSocket logic
├── Dockerfile             # Docker build file
└── README.md              # This documentation
```

---

## 🚀 How to Deploy

### 🐳 Using Docker

1. **Clone the repository**:

```bash
git clone https://github.com/Loony213/chat-service.git
cd chat-service
```

2. **Build the Docker image**:

```bash
docker build -t kamartinez/chat-service .
```

3. **Run the container**:

```bash
docker run -d -p 8000:8000 kamartinez/chat-service
```

The WebSocket server will be available at:  
📍 `ws://localhost:8000/ws/{username}`

---

## 🔗 Endpoints

- `GET /ws/{username}` → WebSocket endpoint for real-time chat

---

## 🛠️ Requirements

- Python 3.11+
- Docker
- FastAPI
- WebSockets support (via `fastapi.WebSocket`)

---

## 👤 Author

Developed by **Loony213**  
Image on Docker Hub: `kamartinez/chat-service`  
Part of the **Distribuida** system
