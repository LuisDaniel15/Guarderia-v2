from fastapi import APIRouter
from controllers.usuario_controller import UsuarioController
from models.usuario_model import Usuario

router = APIRouter()
ctrl = UsuarioController()

@router.post("/create_usuario")
def create_usuario(usuario: Usuario):
    return ctrl.create_usuario(usuario)

@router.get("/get_usuario/{usuario_id}")
def get_usuario(usuario_id: int):
    return ctrl.get_usuario(usuario_id)

@router.get("/get_usuarios")
def get_usuarios():
    return ctrl.get_usuarios()

@router.put("/update_usuario/{usuario_id}")
def update_usuario(usuario_id: int, usuario: Usuario):
    return ctrl.update_usuario(usuario_id, usuario)

@router.delete("/delete_usuario/{usuario_id}")
def delete_usuario(usuario_id: int):
    return ctrl.delete_usuario(usuario_id)