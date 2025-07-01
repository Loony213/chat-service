# Etapa base
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar dependencias e instalar
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código (ahora desde el directorio actual)
COPY . .

# Exponer el puerto para WebSocket/HTTP
EXPOSE 8000

# Comando de arranque (apuntar a app.py en el directorio app)
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
