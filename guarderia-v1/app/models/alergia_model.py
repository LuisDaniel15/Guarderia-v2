from pydantic import BaseModel

class Alergia(BaseModel):
    id: int = None
    nino_id: int
    tipo: str
    descripcion: str
    severidad: str = 'moderada'