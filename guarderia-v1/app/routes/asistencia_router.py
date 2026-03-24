from fastapi import APIRouter
from controllers.asistencia_controller import AsistenciaController
from models.asistencia_model import Asistencia

router = APIRouter()
ctrl = AsistenciaController()

@router.post("/create_asistencia")
def create_asistencia(asistencia: Asistencia):
    return ctrl.create_asistencia(asistencia)

@router.get("/get_asistencia/{asistencia_id}")
def get_asistencia(asistencia_id: int):
    return ctrl.get_asistencia(asistencia_id)

@router.get("/get_asistencias")
def get_asistencias():
    return ctrl.get_asistencias()

@router.put("/update_asistencia/{asistencia_id}")
def update_asistencia(asistencia_id: int, asistencia: Asistencia):
    return ctrl.update_asistencia(asistencia_id, asistencia)

@router.delete("/delete_asistencia/{asistencia_id}")
def delete_asistencia(asistencia_id: int):
    return ctrl.delete_asistencia(asistencia_id)