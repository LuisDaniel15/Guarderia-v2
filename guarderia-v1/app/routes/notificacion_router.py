from fastapi import APIRouter
from controllers.notificacion_controller import NotificacionController
from models.notificacion_model import Notificacion

router = APIRouter()
ctrl = NotificacionController()

@router.post("/create_notificacion")
def create_notificacion(notificacion: Notificacion):
    return ctrl.create_notificacion(notificacion)

@router.get("/get_notificacion/{notificacion_id}")
def get_notificacion(notificacion_id: int):
    return ctrl.get_notificacion(notificacion_id)

@router.get("/get_notificaciones")
def get_notificaciones():
    return ctrl.get_notificaciones()

@router.put("/update_notificacion/{notificacion_id}")
def update_notificacion(notificacion_id: int, notificacion: Notificacion):
    return ctrl.update_notificacion(notificacion_id, notificacion)

@router.delete("/delete_notificacion/{notificacion_id}")
def delete_notificacion(notificacion_id: int):
    return ctrl.delete_notificacion(notificacion_id)