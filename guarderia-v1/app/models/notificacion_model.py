from pydantic import BaseModel

class Notificacion(BaseModel):
    id: int = None
    acudiente_id: int
    nino_id: int = None
    titulo: str
    mensaje: str
    canal: str = 'interna'
    estado: str = 'pendiente'