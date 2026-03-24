from pydantic import BaseModel

class NinoAcudiente(BaseModel):
    id: int = None
    nino_id: int
    acudiente_id: int
    es_contacto_principal: bool = False
    puede_recoger: bool = True