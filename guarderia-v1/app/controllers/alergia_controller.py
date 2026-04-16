import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.alergia_model import Alergia
from fastapi.encoders import jsonable_encoder

class AlergiaController:

    def create_alergia(self, alergia: Alergia):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO alergias (nino_id, tipo, descripcion, severidad) VALUES (%s, %s, %s, %s)",
                (alergia.nino_id, alergia.tipo, alergia.descripcion, alergia.severidad)
            )
            conn.commit()
            return {"resultado": "Alergia creada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_alergia(self, alergia_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM alergias WHERE id = %s", (alergia_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id':          result[0],
                    'nino_id':     result[1],
                    'tipo':        result[2],
                    'descripcion': result[3],
                    'severidad':   result[4],
                    'creado_en':   str(result[5])
                }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="Alergia no encontrada")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_alergias(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM alergias")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id':          data[0],
                    'nino_id':     data[1],
                    'tipo':        data[2],
                    'descripcion': data[3],
                    'severidad':   data[4],
                    'creado_en':   str(data[5])
                }
                payload.append(content)
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_alergia(self, alergia_id: int, alergia: Alergia):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE alergias SET nino_id=%s, tipo=%s, descripcion=%s, severidad=%s WHERE id=%s",
                (alergia.nino_id, alergia.tipo, alergia.descripcion, alergia.severidad, alergia_id)
            )
            conn.commit()
            return {"resultado": "Alergia actualizada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_alergia(self, alergia_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM alergias WHERE id = %s", (alergia_id,))
            conn.commit()
            return {"resultado": "Alergia eliminada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()


    def get_alergias_by_nino(self, nino_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM alergias WHERE nino_id = %s", (nino_id,))
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id':          data[0],
                    'nino_id':     data[1],
                    'tipo':        data[2],
                    'descripcion': data[3],
                    'severidad':   data[4],
                    'creado_en':   str(data[5])
                }
                payload.append(content)
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()