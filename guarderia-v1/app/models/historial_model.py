from pydantic import BaseModel

class Historial(BaseModel):
    id: int = None
    autor_id: int = None
    categoria: str = 'general'
    titulo: str = None
    descripcion: str
    fecha: str = None
    medidas_tomadas: str = None
    acudiente_notificado: bool = False
    es_privado: bool = False