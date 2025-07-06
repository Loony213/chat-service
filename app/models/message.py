from pydantic import BaseModel

class Message(BaseModel):
    to: str
    from_email: str = None  # Cambio aquí
    message: str

    # Utilizar el campo 'from' del JSON
    from_email: str = None

    class Config:
        fields = {
            'from_email': 'from',  # Aquí se hace el mapeo entre 'from' y 'from_email'
        }
