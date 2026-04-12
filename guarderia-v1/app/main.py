from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.rol_router import router as rol_router
from routes.usuario_router import router as usuario_router
from routes.acudiente_router import router as acudiente_router
from routes.nino_router import router as nino_router
from routes.nino_acudiente_router import router as nino_acudiente_router
from routes.alergia_router import router as alergia_router
from routes.vacuna_router import router as vacuna_router
from routes.asistencia_router import router as asistencia_router
from routes.actividad_router import router as actividad_router
from routes.actividad_personal_router import router as actividad_personal_router
from routes.actividad_participante_router import router as actividad_participante_router
from routes.historial_router import router as historial_router
from routes.historial_nino_router import router as historial_nino_router
from routes.notificacion_router import router as notificacion_router
from routes.auth_router import router as auth_router
from routes.grupo_router import router as grupo_router


app = FastAPI(title="Sistema Guarderia", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rol_router,                    prefix="/roles",                 tags=["Roles"])
app.include_router(usuario_router,                prefix="/usuarios",              tags=["Usuarios"])
app.include_router(acudiente_router,              prefix="/acudientes",            tags=["Acudientes"])
app.include_router(nino_router,                   prefix="/ninos",                 tags=["Ninos"])
app.include_router(nino_acudiente_router,         prefix="/nino-acudiente",        tags=["Nino-Acudiente"])
app.include_router(alergia_router,                prefix="/alergias",              tags=["Alergias"])
app.include_router(vacuna_router,                 prefix="/vacunas",               tags=["Vacunas"])
app.include_router(asistencia_router,             prefix="/asistencia",            tags=["Asistencia"])
app.include_router(actividad_router,              prefix="/actividades",           tags=["Actividades"])
app.include_router(actividad_personal_router,     prefix="/actividad-personal",    tags=["Actividad-Personal"])
app.include_router(actividad_participante_router, prefix="/actividad-participantes",tags=["Actividad-Participantes"])
app.include_router(historial_router,              prefix="/historial",             tags=["Historial"])
app.include_router(historial_nino_router,         prefix="/historial-ninos",       tags=["Historial-Ninos"])
app.include_router(notificacion_router,           prefix="/notificaciones",        tags=["Notificaciones"])
app.include_router(grupo_router, prefix="/grupos", tags=["Grupos"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])

@app.get("/")
def root():
    return {"mensaje": "API Sistema Guarderia v1.0"}    