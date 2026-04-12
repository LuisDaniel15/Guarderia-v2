import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.usuario_model import Usuario
from fastapi.encoders import jsonable_encoder

class UsuarioController:

    def create_usuario(self, usuario: Usuario):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO usuarios (nombre, apellido, email, password_hash, rol_id, grupo_id, activo) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (usuario.nombre, usuario.apellido, usuario.email, usuario.password_hash, usuario.rol_id, usuario.grupo_id, usuario.activo)
            )
            conn.commit()
            return {"resultado": "Usuario creado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_usuario(self, usuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE id = %s", (usuario_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id':             result[0],
                    'nombre':         result[1],
                    'apellido':       result[2],
                    'email':          result[3],
                    'password_hash':  result[4],
                    'activo':         result[5],
                    'creado_en':      str(result[6]),
                    'actualizado_en': str(result[7]),
                    'rol_id':         result[8],
                    'grupo_id':       result[9]
                }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_usuarios(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id':             data[0],
                    'nombre':         data[1],
                    'apellido':       data[2],
                    'email':          data[3],
                    'password_hash':  data[4],
                    'activo':         data[5],
                    'creado_en':      str(data[6]),
                    'actualizado_en': str(data[7]),
                    'rol_id':         data[8],
                    'grupo_id':       data[9]
                }
                payload.append(content)
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_usuario(self, usuario_id: int, usuario: Usuario):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE usuarios SET nombre=%s, apellido=%s, email=%s, password_hash=%s, rol_id=%s, grupo_id=%s, activo=%s WHERE id=%s",
                (usuario.nombre, usuario.apellido, usuario.email, usuario.password_hash, usuario.rol_id, usuario.grupo_id, usuario.activo, usuario_id)
            )
            conn.commit()
            return {"resultado": "Usuario actualizado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_usuario(self, usuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE usuarios SET activo = FALSE WHERE id = %s", (usuario_id,))
            conn.commit()
            return {"resultado": "Usuario desactivado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()