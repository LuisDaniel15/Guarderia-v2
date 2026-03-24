from pydantic import BaseModel

class Nino(BaseModel):
    id: int = None
    nombre: str
    apellido: str
    fecha_nacimiento: str
    genero: str = None
    foto_url: str = None
    grupo: str = None
    fecha_ingreso: str = None
    activo: bool = True
    tipo_sangre: str = None
    medico_nombre: str = None
    medico_telefono: str = None
    seguro_medico: str = None
    observaciones_medicas: str = None