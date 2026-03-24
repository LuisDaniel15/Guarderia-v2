from pydantic import BaseModel

class Asistencia(BaseModel):
    id: int = None
    nino_id: int
    fecha: str = None
    hora_entrada: str = None
    hora_salida: str = None
    estado: str = 'presente'
    registrado_por: int = None
    observacion: str = None