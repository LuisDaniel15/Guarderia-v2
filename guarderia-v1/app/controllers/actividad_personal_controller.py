import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.actividad_personal_model import ActividadPersonal
from fastapi.encoders import jsonable_encoder

class ActividadPersonalController:

    def create_actividad_personal(self, ap: ActividadPersonal):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO actividad_personal (actividad_id, usuario_id, rol, notas) VALUES (%s, %s, %s, %s)",
                (ap.actividad_id, ap.usuario_id, ap.rol, ap.notas)
            )
            conn.commit()
            return {"resultado": "Personal asignado a actividad"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_actividad_personal(self, ap_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM actividad_personal WHERE id = %s", (ap_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id':           result[0],
                    'actividad_id': result[1],
                    'usuario_id':   result[2],
                    'rol':          result[3],
                    'notas':        result[4],
                    'creado_en':    str(result[5])
                }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="Registro no encontrado")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_actividades_personal(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM actividad_personal")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id':           data[0],
                    'actividad_id': data[1],
                    'usuario_id':   data[2],
                    'rol':          data[3],
                    'notas':        data[4],
                    'creado_en':    str(data[5])
                }
                payload.append(content)
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_actividad_personal(self, ap_id: int, ap: ActividadPersonal):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE actividad_personal SET actividad_id=%s, usuario_id=%s, rol=%s, notas=%s WHERE id=%s",
                (ap.actividad_id, ap.usuario_id, ap.rol, ap.notas, ap_id)
            )
            conn.commit()
            return {"resultado": "Registro actualizado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_actividad_personal(self, ap_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM actividad_personal WHERE id = %s", (ap_id,))
            conn.commit()
            return {"resultado": "Registro eliminado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()