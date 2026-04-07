import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.asistencia_model import Asistencia
from fastapi.encoders import jsonable_encoder

class AsistenciaController:

    def create_asistencia(self, asistencia: Asistencia):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO asistencia 
                (nino_id, fecha, hora_entrada, hora_salida, estado, registrado_por, observacion) 
                VALUES (%s, COALESCE(%s, CURRENT_DATE), %s, %s, %s, %s, %s)""",
                (asistencia.nino_id, asistencia.fecha, asistencia.hora_entrada,
                asistencia.hora_salida, asistencia.estado, asistencia.registrado_por,
                asistencia.observacion)
            )
            conn.commit()
            return {"resultado": "Asistencia registrada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_asistencia(self, asistencia_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM asistencia WHERE id = %s", (asistencia_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id':            result[0],
                    'nino_id':       result[1],
                    'fecha':         str(result[2]),
                    'hora_entrada':  str(result[3]) if result[3] else None,
                    'hora_salida':   str(result[4]) if result[4] else None,
                    'estado':        result[5],
                    'registrado_por':result[6],
                    'observacion':   result[7],
                    'creado_en':     str(result[8])
                }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="Asistencia no encontrada")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_asistencias(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM asistencia")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id':            data[0],
                    'nino_id':       data[1],
                    'fecha':         str(data[2]),
                    'hora_entrada':  str(data[3]) if data[3] else None,
                    'hora_salida':   str(data[4]) if data[4] else None,
                    'estado':        data[5],
                    'registrado_por':data[6],
                    'observacion':   data[7],
                    'creado_en':     str(data[8])
                }
                payload.append(content)
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_asistencia(self, asistencia_id: int, asistencia: Asistencia):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE asistencia SET nino_id=%s, fecha=%s, hora_entrada=%s, hora_salida=%s, estado=%s, registrado_por=%s, observacion=%s WHERE id=%s",
                (asistencia.nino_id, asistencia.fecha, asistencia.hora_entrada, asistencia.hora_salida, asistencia.estado, asistencia.registrado_por, asistencia.observacion, asistencia_id)
            )
            conn.commit()
            return {"resultado": "Asistencia actualizada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_asistencia(self, asistencia_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM asistencia WHERE id = %s", (asistencia_id,))
            conn.commit()
            return {"resultado": "Asistencia eliminada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()