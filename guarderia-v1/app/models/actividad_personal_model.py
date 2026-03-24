from pydantic import BaseModel

class ActividadPersonal(BaseModel):
    id: int = None
    actividad_id: int
    usuario_id: int
    rol: str = 'apoyo'
    notas: str = None