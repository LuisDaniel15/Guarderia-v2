from fastapi import APIRouter
from controllers.nino_controller import NinoController
from models.nino_model import Nino

router = APIRouter()
ctrl = NinoController()

@router.post("/create_nino")
def create_nino(nino: Nino):
    return ctrl.create_nino(nino)

@router.get("/get_nino/{nino_id}")
def get_nino(nino_id: int):
    return ctrl.get_nino(nino_id)

@router.get("/get_ninos")
def get_ninos():
    return ctrl.get_ninos()

@router.put("/update_nino/{nino_id}")
def update_nino(nino_id: int, nino: Nino):
    return ctrl.update_nino(nino_id, nino)

@router.delete("/delete_nino/{nino_id}")
def delete_nino(nino_id: int):
    return ctrl.delete_nino(nino_id)