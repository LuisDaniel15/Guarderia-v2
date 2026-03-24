from fastapi import APIRouter
from controllers.actividad_controller import ActividadController
from models.actividad_model import Actividad

router = APIRouter()
ctrl = ActividadController()

@router.post("/create_actividad")
def create_actividad(actividad: Actividad):
    return ctrl.create_actividad(actividad)

@router.get("/get_actividad/{actividad_id}")
def get_actividad(actividad_id: int):
    return ctrl.get_actividad(actividad_id)

@router.get("/get_actividades")
def get_actividades():
    return ctrl.get_actividades()

@router.put("/update_actividad/{actividad_id}")
def update_actividad(actividad_id: int, actividad: Actividad):
    return ctrl.update_actividad(actividad_id, actividad)

@router.delete("/delete_actividad/{actividad_id}")
def delete_actividad(actividad_id: int):
    return ctrl.delete_actividad(actividad_id)