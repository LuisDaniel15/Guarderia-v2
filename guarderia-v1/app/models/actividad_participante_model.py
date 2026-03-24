from pydantic import BaseModel

class ActividadParticipante(BaseModel):
    id: int = None
    actividad_id: int
    nino_id: int
    asistio: bool = True
    observacion: str = None