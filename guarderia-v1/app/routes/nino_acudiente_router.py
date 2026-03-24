from fastapi import APIRouter
from controllers.nino_acudiente_controller import NinoAcudienteController
from models.nino_acudiente_model import NinoAcudiente

router = APIRouter()
ctrl = NinoAcudienteController()

@router.post("/create_nino_acudiente")
def create_nino_acudiente(na: NinoAcudiente):
    return ctrl.create_nino_acudiente(na)

@router.get("/get_nino_acudiente/{na_id}")
def get_nino_acudiente(na_id: int):
    return ctrl.get_nino_acudiente(na_id)

@router.get("/get_ninos_acudientes")
def get_ninos_acudientes():
    return ctrl.get_ninos_acudientes()

@router.put("/update_nino_acudiente/{na_id}")
def update_nino_acudiente(na_id: int, na: NinoAcudiente):
    return ctrl.update_nino_acudiente(na_id, na)

@router.delete("/delete_nino_acudiente/{na_id}")
def delete_nino_acudiente(na_id: int):
    return ctrl.delete_nino_acudiente(na_id)