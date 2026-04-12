from fastapi import APIRouter
from controllers.auth_controller import AuthController
from models.auth_model import LoginRequest
from pydantic import BaseModel

router = APIRouter()
ctrl = AuthController()

class RegisterRequest(BaseModel):
    nombre: str
    apellido: str
    email: str
    password: str
    rol_id: int = 2

@router.post("/login")
def login(data: LoginRequest):
    return ctrl.login(data)

@router.post("/register")
def register(data: RegisterRequest):
    return ctrl.register(data.nombre, data.apellido, data.email, data.password, data.rol_id)