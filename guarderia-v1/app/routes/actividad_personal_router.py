from fastapi import APIRouter
from controllers.actividad_personal_controller import ActividadPersonalController
from models.actividad_personal_model import ActividadPersonal

router = APIRouter()
ctrl = ActividadPersonalController()

@router.post("/create_actividad_personal")
def create_actividad_personal(ap: ActividadPersonal):
    return ctrl.create_actividad_personal(ap)

@router.get("/get_actividad_personal/{ap_id}")
def get_actividad_personal(ap_id: int):
    return ctrl.get_actividad_personal(ap_id)

@router.get("/get_actividades_personal")
def get_actividades_personal():
    return ctrl.get_actividades_personal()

@router.get("/get_by_actividad/{actividad_id}")
def get_by_actividad(actividad_id: int):
    return ctrl.get_personal_by_actividad(actividad_id)

@router.put("/update_actividad_personal/{ap_id}")
def update_actividad_personal(ap_id: int, ap: ActividadPersonal):
    return ctrl.update_actividad_personal(ap_id, ap)

@router.delete("/delete_actividad_personal/{ap_id}")
def delete_actividad_personal(ap_id: int):
    return ctrl.delete_actividad_personal(ap_id)