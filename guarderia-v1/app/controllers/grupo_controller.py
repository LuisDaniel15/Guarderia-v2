import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.grupo_model import Grupo
from fastapi.encoders import jsonable_encoder

class GrupoController:

    def create_grupo(self, grupo: Grupo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO grupos (nombre, descripcion) VALUES (%s, %s)",
                (grupo.nombre, grupo.descripcion)
            )
            conn.commit()
            return {"resultado": "Grupo creado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_grupo(self, grupo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM grupos WHERE id = %s", (grupo_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id':          result[0],
                    'nombre':      result[1],
                    'descripcion': result[2]
                }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="Grupo no encontrado")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_grupos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM grupos")
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

    def update_grupo(self, grupo_id: int, grupo: Grupo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE grupos SET nombre=%s, descripcion=%s WHERE id=%s",
                (grupo.nombre, grupo.descripcion, grupo_id)
            )
            conn.commit()
            return {"resultado": "Grupo actualizado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_grupo(self, grupo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM grupos WHERE id = %s", (grupo_id,))
            conn.commit()
            return {"resultado": "Grupo eliminado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()