import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.actividad_participante_model import ActividadParticipante
from fastapi.encoders import jsonable_encoder

class ActividadParticipanteController:

    def create_participante(self, ap: ActividadParticipante):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO actividad_participantes (actividad_id, nino_id, asistio, observacion) VALUES (%s, %s, %s, %s)",
                (ap.actividad_id, ap.nino_id, ap.asistio, ap.observacion)
            )
            conn.commit()
            return {"resultado": "Participante agregado a actividad"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_participante(self, ap_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM actividad_participantes WHERE id = %s", (ap_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id':           result[0],
                    'actividad_id': result[1],
                    'nino_id':      result[2],
                    'asistio':      result[3],
                    'observacion':  result[4],
                    'creado_en':    str(result[5])
                }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="Participante no encontrado")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_participantes(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM actividad_participantes")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id':           data[0],
                    'actividad_id': data[1],
                    'nino_id':      data[2],
                    'asistio':      data[3],
                    'observacion':  data[4],
                    'creado_en':    str(data[5])
                }
                payload.append(content)
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_participante(self, ap_id: int, ap: ActividadParticipante):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE actividad_participantes SET actividad_id=%s, nino_id=%s, asistio=%s, observacion=%s WHERE id=%s",
                (ap.actividad_id, ap.nino_id, ap.asistio, ap.observacion, ap_id)
            )
            conn.commit()
            return {"resultado": "Participante actualizado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_participante(self, ap_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM actividad_participantes WHERE id = %s", (ap_id,))
            conn.commit()
            return {"resultado": "Participante eliminado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def get_participantes_by_actividad(self, actividad_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT ap.*, n.nombre, n.apellido
                FROM actividad_participantes ap
                JOIN ninos n ON ap.nino_id = n.id
                WHERE ap.actividad_id = %s
            """, (actividad_id,))
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id':           data[0],
                    'actividad_id': data[1],
                    'nino_id':      data[2],
                    'asistio':      data[3],
                    'observacion':  data[4],
                    'creado_en':    str(data[5]),
                    'nombre':       data[6],
                    'apellido':     data[7]
                }
                payload.append(content)
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()