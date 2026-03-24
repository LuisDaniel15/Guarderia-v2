from fastapi import APIRouter
from controllers.rol_controller import RolController
from models.rol_model import Rol

router = APIRouter()
ctrl = RolController()

@router.post("/create_rol")
def create_rol(rol: Rol):
    return ctrl.create_rol(rol)

@router.get("/get_rol/{rol_id}")
def get_rol(rol_id: int):
    return ctrl.get_rol(rol_id)

@router.get("/get_roles")
def get_roles():
    return ctrl.get_roles()

@router.put("/update_rol/{rol_id}")
def update_rol(rol_id: int, rol: Rol):
    return ctrl.update_rol(rol_id, rol)

@router.delete("/delete_rol/{rol_id}")
def delete_rol(rol_id: int):
    return ctrl.delete_rol(rol_id)