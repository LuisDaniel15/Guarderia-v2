from fastapi import APIRouter
from controllers.historial_controller import HistorialController
from models.historial_model import Historial

router = APIRouter()
ctrl = HistorialController()

@router.post("/create_historial")
def create_historial(historial: Historial):
    return ctrl.create_historial(historial)

@router.get("/get_historial/{historial_id}")
def get_historial(historial_id: int):
    return ctrl.get_historial(historial_id)

@router.get("/get_historiales")
def get_historiales():
    return ctrl.get_historiales()

@router.put("/update_historial/{historial_id}")
def update_historial(historial_id: int, historial: Historial):
    return ctrl.update_historial(historial_id, historial)

@router.delete("/delete_historial/{historial_id}")
def delete_historial(historial_id: int):
    return ctrl.delete_historial(historial_id)