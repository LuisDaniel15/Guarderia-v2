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
                    'registrado_por':result[2],
                    'fecha':         str(result[3]),
                    'hora_entrada':  str(result[4]) if result[4] else None,
                    'hora_salida':   str(result[5]) if result[5] else None,
                    'estado':        result[6],
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
                    'registrado_por':data[2],
                    'fecha':         str(data[3]),
                    'hora_entrada':  str(data[4]) if data[4] else None,
                    'hora_salida':   str(data[5]) if data[5] else None,
                    'estado':        data[6],
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
                (asistencia.nino_id, asistencia.fecha, asistencia.hora_entrada,
                asistencia.hora_salida, asistencia.estado, asistencia.registrado_por,
                asistencia.observacion, asistencia_id)
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

    def registrar_asistencia_masiva(self, registros: list):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            for r in registros:
                cursor.execute(
                    "SELECT id FROM asistencia WHERE nino_id = %s AND fecha = CURRENT_DATE",
                    (r['nino_id'],)
                )
                existing = cursor.fetchone()
                if existing:
                    cursor.execute(
                        "UPDATE asistencia SET estado=%s, observacion=%s, registrado_por=%s WHERE id=%s",
                        (r['estado'], r.get('observacion'), r.get('registrado_por'), existing[0])
                    )
                else:
                    cursor.execute(
                        """INSERT INTO asistencia 
                        (nino_id, fecha, estado, observacion, registrado_por)
                        VALUES (%s, CURRENT_DATE, %s, %s, %s)""",
                        (r['nino_id'], r['estado'], r.get('observacion'), r.get('registrado_por'))
                    )
            conn.commit()
            return {"resultado": "Asistencia registrada correctamente"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
            return {"error": str(err)}
        finally:
            conn.close()

    def get_asistencias_hoy(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT a.*, n.nombre, n.apellido 
                FROM asistencia a
                JOIN ninos n ON a.nino_id = n.id
                WHERE a.fecha = CURRENT_DATE
            """)
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id':            data[0],
                    'nino_id':       data[1],
                    'registrado_por':data[2],
                    'fecha':         str(data[3]),
                    'hora_entrada':  str(data[4]) if data[4] else None,
                    'hora_salida':   str(data[5]) if data[5] else None,
                    'estado':        data[6],
                    'observacion':   data[7],
                    'creado_en':     str(data[8]),
                    'nombre':        data[9],
                    'apellido':      data[10]
                }
                payload.append(content)
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()