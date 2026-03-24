import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.rol_model import Rol
from fastapi.encoders import jsonable_encoder

class RolController:

    def create_rol(self, rol: Rol):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO roles (nombre, descripcion) VALUES (%s, %s)",
                (rol.nombre, rol.descripcion)
            )
            conn.commit()
            return {"resultado": "Rol creado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_rol(self, rol_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roles WHERE id = %s", (rol_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id':          result[0],
                    'nombre':      result[1],
                    'descripcion': result[2]
                }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="Rol no encontrado")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_roles(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roles")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id':          data[0],
                    'nombre':      data[1],
                    'descripcion': data[2]
                }
                payload.append(content)
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_rol(self, rol_id: int, rol: Rol):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE roles SET nombre = %s, descripcion = %s WHERE id = %s",
                (rol.nombre, rol.descripcion, rol_id)
            )
            conn.commit()
            return {"resultado": "Rol actualizado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_rol(self, rol_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM roles WHERE id = %s", (rol_id,))
            conn.commit()
            return {"resultado": "Rol eliminado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()