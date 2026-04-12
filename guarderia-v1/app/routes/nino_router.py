from fastapi import APIRouter
from controllers.nino_controller import NinoController
from models.nino_model import Nino
from pydantic import BaseModel
from typing import Optional

router = APIRouter()
ctrl = NinoController()

class AcudienteNino(BaseModel):
    id: Optional[int] = None
    nombre: str
    apellido: str
    dni: Optional[str] = None
    telefono: Optional[str] = None
    telefono_emergencia: Optional[str] = None
    email: Optional[str] = None
    direccion: Optional[str] = None
    relacion: str = 'otro'

class RegistroCompleto(BaseModel):
    nino: Nino
    acudiente: AcudienteNino

@router.post("/registrar_completo")
def registrar_completo(datos: RegistroCompleto):
    return ctrl.registrar_nino_completo(datos.dict())

@router.post("/create_nino")
def create_nino(nino: Nino):
    return ctrl.create_nino(nino)

@router.get("/get_nino/{nino_id}")
def get_nino(nino_id: int):
    return ctrl.get_nino(nino_id)

@router.get("/get_ninos")
def get_ninos():
    return ctrl.get_ninos()

@router.get("/get_ninos_by_grupo/{grupo_id}")
def get_ninos_by_grupo(grupo_id: int):
    return ctrl.get_ninos_by_grupo(grupo_id)

@router.put("/update_nino/{nino_id}")
def update_nino(nino_id: int, nino: Nino):
    return ctrl.update_nino(nino_id, nino)

@router.delete("/delete_nino/{nino_id}")
def delete_nino(nino_id: int):
    return ctrl.delete_nino(nino_id)