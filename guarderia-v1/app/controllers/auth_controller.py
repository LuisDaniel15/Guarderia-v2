import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from utils.auth import verify_password, hash_password, create_access_token
from models.auth_model import LoginRequest

class AuthController:

    def login(self, data: LoginRequest):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, nombre, apellido, email, password_hash, rol_id, activo, grupo_id FROM usuarios WHERE email = %s",
                (data.email,)
            )
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=401, detail="Credenciales incorrectas")

            usuario_id    = result[0]
            nombre        = result[1]
            password_hash = result[4]
            rol_id        = result[5]
            activo        = result[6]
            grupo_id      = result[7]

            if not activo:
                raise HTTPException(status_code=401, detail="Usuario inactivo")

            if not password_hash:
                raise HTTPException(status_code=401, detail="Este usuario no tiene acceso al sistema")

            if not verify_password(data.password, password_hash):
                raise HTTPException(status_code=401, detail="Credenciales incorrectas")

            token = create_access_token({
                "sub":      str(usuario_id),
                "nombre":   nombre,
                "rol_id":   rol_id,
                "grupo_id": grupo_id
            })

            return {
                "access_token": token,
                "token_type":   "bearer",
                "usuario_id":   usuario_id,
                "nombre":       nombre,
                "rol_id":       rol_id,
                "grupo_id":     grupo_id
            }

        except HTTPException:
            raise
        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en la base de datos")
        finally:
            conn.close()

    def register(self, nombre: str, apellido: str, email: str, password: str, rol_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM usuarios WHERE email = %s", (email,))
            if cursor.fetchone():
                raise HTTPException(status_code=400, detail="El email ya esta registrado")
            hashed = hash_password(password)
            cursor.execute(
                "INSERT INTO usuarios (nombre, apellido, email, password_hash, rol_id) VALUES (%s, %s, %s, %s, %s)",
                (nombre, apellido, email, hashed, rol_id)
            )
            conn.commit()
            return {"resultado": "Usuario registrado correctamente"}
        except HTTPException:
            raise
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error en la base de datos")
        finally:
            conn.close()