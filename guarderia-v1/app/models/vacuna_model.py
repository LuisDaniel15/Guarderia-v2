from pydantic import BaseModel

class Vacuna(BaseModel):
    id: int = None
    nino_id: int
    nombre: str
    fecha_aplicacion: str
    proxima_dosis: str = None
    notas: str = None