from fastapi import APIRouter
from controllers.acudiente_controller import AcudienteController
from models.acudiente_model import Acudiente

router = APIRouter()
ctrl = AcudienteController()

@router.post("/create_acudiente")
def create_acudiente(acudiente: Acudiente):
    return ctrl.create_acudiente(acudiente)

@router.get("/get_acudiente/{acudiente_id}")
def get_acudiente(acudiente_id: int):
    return ctrl.get_acudiente(acudiente_id)

@router.get("/get_acudientes")
def get_acudientes():
    return ctrl.get_acudientes()

@router.put("/update_acudiente/{acudiente_id}")
def update_acudiente(acudiente_id: int, acudiente: Acudiente):
    return ctrl.update_acudiente(acudiente_id, acudiente)

@router.delete("/delete_acudiente/{acudiente_id}")
def delete_acudiente(acudiente_id: int):
    return ctrl.delete_acudiente(acudiente_id)