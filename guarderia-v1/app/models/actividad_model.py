from pydantic import BaseModel
from typing import Optional

class Actividad(BaseModel):
    id: Optional[int] = None
    titulo: str
    descripcion: Optional[str] = None
    tipo: str = 'educativa'
    fecha: str
    hora_inicio: Optional[str] = None
    hora_fin: Optional[str] = None
    grupo: Optional[str] = None
    grupo_id: Optional[int] = None