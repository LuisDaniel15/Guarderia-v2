import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.notificacion_model import Notificacion
from fastapi.encoders import jsonable_encoder

class NotificacionController:

    def create_notificacion(self, notificacion: Notificacion):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO notificaciones (acudiente_id, nino_id, titulo, mensaje, canal, estado) VALUES (%s, %s, %s, %s, %s, %s)",
                (notificacion.acudiente_id, notificacion.nino_id, notificacion.titulo, notificacion.mensaje, notificacion.canal, notificacion.estado)
            )
            conn.commit()
            return {"resultado": "Notificacion creada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_notificacion(self, notificacion_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM notificaciones WHERE id = %s", (notificacion_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id':           result[0],
                    'acudiente_id': result[1],
                    'nino_id':      result[2],
                    'titulo':       result[3],
                    'mensaje':      result[4],
                    'canal':        result[5],
                    'estado':       result[6],
                    'enviada_en':   str(result[7]) if result[7] else None,
                    'leida_en':     str(result[8]) if result[8] else None,
                    'creado_en':    str(result[9])
                }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="Notificacion no encontrada")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_notificaciones(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM notificaciones")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id':           data[0],
                    'acudiente_id': data[1],
                    'nino_id':      data[2],
                    'titulo':       data[3],
                    'mensaje':      data[4],
                    'canal':        data[5],
                    'estado':       data[6],
                    'enviada_en':   str(data[7]) if data[7] else None,
                    'leida_en':     str(data[8]) if data[8] else None,
                    'creado_en':    str(data[9])
                }
                payload.append(content)
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_notificacion(self, notificacion_id: int, notificacion: Notificacion):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE notificaciones SET acudiente_id=%s, nino_id=%s, titulo=%s, mensaje=%s, canal=%s, estado=%s WHERE id=%s",
                (notificacion.acudiente_id, notificacion.nino_id, notificacion.titulo, notificacion.mensaje, notificacion.canal, notificacion.estado, notificacion_id)
            )
            conn.commit()
            return {"resultado": "Notificacion actualizada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_notificacion(self, notificacion_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM notificaciones WHERE id = %s", (notificacion_id,))
            conn.commit()
            return {"resultado": "Notificacion eliminada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()