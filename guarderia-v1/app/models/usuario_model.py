from pydantic import BaseModel

class Usuario(BaseModel):
    id: int = None
    nombre: str
    apellido: str
    email: str
    password_hash: str = None
    rol_id: int
    activo: bool = True