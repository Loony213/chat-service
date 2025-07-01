
# 💬 Chat Service

This microservice is part of the **Distribuida** system and enables **real-time communication** between users using WebSockets. Built with **FastAPI**, it allows clients to join a live chat and exchange messages.

---

## 📌 Features

- 🔌 WebSocket endpoint at `/ws/{email}`
- 🧍 Tracks connected users
- 💬 Broadcasts messages to all participants
- 🔄 Supports reconnect logic from the frontend

---

## 🧩 Architecture

- 🧱 Style: Minimal, standalone microservice
- 🌐 Protocol: WebSocket (FastAPI)
- 🐍 Language: Python 3.11+
- 🐳 Containerized with Docker

### Folder Structure

The project follows a **modular folder structure**, where each directory has a clear responsibility:

- **`api/`**: Contains all WebSocket route handling logic, with endpoints like `/ws/{email}` for real-time communication.
- **`core/`**: Handles core components like WebSocket connection management.
- **`models/`**: Defines the data models, such as the message schema.
- **`services/`**: Encapsulates the business logic related to the WebSocket communication and message handling.
- **`app.py`**: The entry point for the FastAPI application, wiring everything together.

---

## 📁 Project Structure

```
chat-service/
├── app/                    # Main application code
│   ├── api/                # WebSocket API routes
│   │   └── websocket_api.py  # WebSocket routes for real-time communication
│   ├── core/               # Core components
│   │   └── ws_manager.py   # Manages active WebSocket connections
│   ├── models/             # Data models
│   │   └── message.py      # Defines the message schema
│   ├── services/           # Business logic
│   │   └── websocket_service.py  # Handles WebSocket communication logic
│   └── app.py              # FastAPI app entry point
├── Dockerfile              # Docker build file
└── requirements.txt        # Python dependencies
```

---

## 🧑‍💻 Design Patterns & Principles

### **Design Pattern Used:**

- **Microservices Architecture**: The chat service is designed as a **standalone microservice** to handle real-time communication between users. It communicates with other services through WebSockets, and each service in the system can independently scale, deploy, and update.

- **Observer Pattern**: This pattern is implicitly used in the WebSocket connection model. The WebSocket manager serves as an observer, maintaining a list of connected clients (subscribers). When a message is received, it notifies the relevant clients (observers).

- **Singleton Pattern**: The `WebSocketManager` follows the singleton pattern by maintaining a single instance to handle all active WebSocket connections.

### **Principles Used:**

- **Separation of Concerns**: The application is split into multiple layers based on the responsibilities:
  - WebSocket route handling (`api/`)
  - Business logic (`services/`)
  - Core connection management (`core/`)
  - Data modeling (`models/`)

- **Single Responsibility Principle**: Each file or component is responsible for only one part of the system. For example, `ws_manager.py` is responsible solely for managing WebSocket connections, while `websocket_service.py` handles the business logic related to the communication between users.

- **Modularity**: The project structure encourages modularity. Each directory and file has a focused responsibility, and dependencies are clearly defined, allowing easy modifications or replacements without impacting other parts of the system.

- **Minimalistic Design**: The service follows a minimalistic design by exposing only the necessary routes and methods for communication, keeping the service lightweight and easy to maintain.

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
📍 `ws://localhost:8000/ws/{email}`

---

## 🔗 Endpoints

- `GET /ws/{email}` → WebSocket endpoint for real-time chat

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
