from fastapi import APIRouter
from controllers.actividad_participante_controller import ActividadParticipanteController
from models.actividad_participante_model import ActividadParticipante

router = APIRouter()
ctrl = ActividadParticipanteController()

@router.post("/create_participante")
def create_participante(ap: ActividadParticipante):
    return ctrl.create_participante(ap)

@router.get("/get_participante/{ap_id}")
def get_participante(ap_id: int):
    return ctrl.get_participante(ap_id)

@router.get("/get_participantes")
def get_participantes():
    return ctrl.get_participantes()

@router.put("/update_participante/{ap_id}")
def update_participante(ap_id: int, ap: ActividadParticipante):
    return ctrl.update_participante(ap_id, ap)

@router.delete("/delete_participante/{ap_id}")
def delete_participante(ap_id: int):
    return ctrl.delete_participante(ap_id)