import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.historial_nino_model import HistorialNino
from fastapi.encoders import jsonable_encoder

class HistorialNinoController:

    def create_historial_nino(self, hn: HistorialNino):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO historial_ninos (historial_id, nino_id) VALUES (%s, %s)",
                (hn.historial_id, hn.nino_id)
            )
            conn.commit()
            return {"resultado": "Relacion historial-nino creada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_historial_nino(self, hn_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM historial_ninos WHERE id = %s", (hn_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id':          result[0],
                    'historial_id':result[1],
                    'nino_id':     result[2],
                    'creado_en':   str(result[3])
                }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="Relacion no encontrada")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_historial_ninos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM historial_ninos")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id':          data[0],
                    'historial_id':data[1],
                    'nino_id':     data[2],
                    'creado_en':   str(data[3])
                }
                payload.append(content)
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_historial_nino(self, hn_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM historial_ninos WHERE id = %s", (hn_id,))
            conn.commit()
            return {"resultado": "Relacion eliminada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()