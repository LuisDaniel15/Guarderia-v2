from fastapi import APIRouter
from controllers.alergia_controller import AlergiaController
from models.alergia_model import Alergia

router = APIRouter()
ctrl = AlergiaController()

@router.post("/create_alergia")
def create_alergia(alergia: Alergia):
    return ctrl.create_alergia(alergia)

@router.get("/get_alergia/{alergia_id}")
def get_alergia(alergia_id: int):
    return ctrl.get_alergia(alergia_id)

@router.get("/get_alergias")
def get_alergias():
    return ctrl.get_alergias()

@router.get("/get_by_nino/{nino_id}")
def get_by_nino(nino_id: int):
    return ctrl.get_alergias_by_nino(nino_id)

@router.put("/update_alergia/{alergia_id}")
def update_alergia(alergia_id: int, alergia: Alergia):
    return ctrl.update_alergia(alergia_id, alergia)

@router.delete("/delete_alergia/{alergia_id}")
def delete_alergia(alergia_id: int):
    return ctrl.delete_alergia(alergia_id)