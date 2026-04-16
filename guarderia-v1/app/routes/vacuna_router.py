from fastapi import APIRouter
from controllers.vacuna_controller import VacunaController
from models.vacuna_model import Vacuna

router = APIRouter()
ctrl = VacunaController()

@router.post("/create_vacuna")
def create_vacuna(vacuna: Vacuna):
    return ctrl.create_vacuna(vacuna)

@router.get("/get_vacuna/{vacuna_id}")
def get_vacuna(vacuna_id: int):
    return ctrl.get_vacuna(vacuna_id)

@router.get("/get_vacunas")
def get_vacunas():
    return ctrl.get_vacunas()

@router.get("/get_by_nino/{nino_id}")
def get_by_nino(nino_id: int):
    return ctrl.get_vacunas_by_nino(nino_id)

@router.put("/update_vacuna/{vacuna_id}")
def update_vacuna(vacuna_id: int, vacuna: Vacuna):
    return ctrl.update_vacuna(vacuna_id, vacuna)

@router.delete("/delete_vacuna/{vacuna_id}")
def delete_vacuna(vacuna_id: int):
    return ctrl.delete_vacuna(vacuna_id)