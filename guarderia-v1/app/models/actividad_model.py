from pydantic import BaseModel

class Actividad(BaseModel):
    id: int = None
    titulo: str
    descripcion: str = None
    tipo: str = 'educativa'
    fecha: str
    hora_inicio: str = None
    hora_fin: str = None
    grupo: str = None