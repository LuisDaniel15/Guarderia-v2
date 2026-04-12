from fastapi import APIRouter
from controllers.asistencia_controller import AsistenciaController
from models.asistencia_model import Asistencia
from typing import List
from pydantic import BaseModel

router = APIRouter()
ctrl = AsistenciaController()

class AsistenciaMasiva(BaseModel):
    nino_id: int
    estado: str = 'presente'
    observacion: str = None
    registrado_por: int = None

@router.post("/create_asistencia")
def create_asistencia(asistencia: Asistencia):
    return ctrl.create_asistencia(asistencia)

@router.post("/registrar_masiva")
def registrar_masiva(registros: List[AsistenciaMasiva]):
    return ctrl.registrar_asistencia_masiva([r.dict() for r in registros])

@router.get("/get_asistencia/{asistencia_id}")
def get_asistencia(asistencia_id: int):
    return ctrl.get_asistencia(asistencia_id)

@router.get("/get_asistencias")
def get_asistencias():
    return ctrl.get_asistencias()

@router.get("/get_asistencias_hoy")
def get_asistencias_hoy():
    return ctrl.get_asistencias_hoy()

@router.put("/update_asistencia/{asistencia_id}")
def update_asistencia(asistencia_id: int, asistencia: Asistencia):
    return ctrl.update_asistencia(asistencia_id, asistencia)

@router.delete("/delete_asistencia/{asistencia_id}")
def delete_asistencia(asistencia_id: int):
    return ctrl.delete_asistencia(asistencia_id)