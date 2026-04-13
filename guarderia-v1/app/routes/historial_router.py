from fastapi import APIRouter
from controllers.historial_controller import HistorialController
from models.historial_model import Historial
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()
ctrl = HistorialController()

class HistorialCompleto(BaseModel):
    autor_id: Optional[int] = None
    categoria: str = 'general'
    titulo: Optional[str] = None
    descripcion: str
    medidas_tomadas: Optional[str] = None
    acudiente_notificado: bool = False
    es_privado: bool = False
    ninos: List[int] = []

@router.post("/crear_completo")
def crear_completo(datos: HistorialCompleto):
    return ctrl.crear_historial_completo(datos.dict())

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