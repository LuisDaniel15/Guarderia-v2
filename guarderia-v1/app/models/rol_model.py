from pydantic import BaseModel

class Rol(BaseModel):
    id: int = None
    nombre: str
    descripcion: str = None