from pydantic import BaseModel

class Grupo(BaseModel):
    id: int = None
    nombre: str
    descripcion: str = None