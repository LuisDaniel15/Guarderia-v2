from pydantic import BaseModel

class HistorialNino(BaseModel):
    id: int = None
    historial_id: int
    nino_id: int