from pydantic import BaseModel

class Acudiente(BaseModel):
    id: int = None
    nombre: str
    apellido: str
    dni: str = None
    telefono: str = None
    telefono_emergencia: str = None
    email: str = None
    direccion: str = None
    relacion: str = 'otro'
    activo: bool = True