from fastapi import APIRouter
from controllers.grupo_controller import GrupoController
from models.grupo_model import Grupo

router = APIRouter()
ctrl = GrupoController()

@router.post("/create_grupo")
def create_grupo(grupo: Grupo):
    return ctrl.create_grupo(grupo)

@router.get("/get_grupo/{grupo_id}")
def get_grupo(grupo_id: int):
    return ctrl.get_grupo(grupo_id)

@router.get("/get_grupos")
def get_grupos():
    return ctrl.get_grupos()

@router.put("/update_grupo/{grupo_id}")
def update_grupo(grupo_id: int, grupo: Grupo):
    return ctrl.update_grupo(grupo_id, grupo)

@router.delete("/delete_grupo/{grupo_id}")
def delete_grupo(grupo_id: int):
    return ctrl.delete_grupo(grupo_id)