from fastapi import APIRouter
from controllers.historial_nino_controller import HistorialNinoController
from models.historial_nino_model import HistorialNino

router = APIRouter()
ctrl = HistorialNinoController()

@router.post("/create_historial_nino")
def create_historial_nino(hn: HistorialNino):
    return ctrl.create_historial_nino(hn)

@router.get("/get_historial_nino/{hn_id}")
def get_historial_nino(hn_id: int):
    return ctrl.get_historial_nino(hn_id)

@router.get("/get_historial_ninos")
def get_historial_ninos():
    return ctrl.get_historial_ninos()

@router.delete("/delete_historial_nino/{hn_id}")
def delete_historial_nino(hn_id: int):
    return ctrl.delete_historial_nino(hn_id)