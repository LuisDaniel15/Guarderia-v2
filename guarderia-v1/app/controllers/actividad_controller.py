import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.actividad_model import Actividad
from fastapi.encoders import jsonable_encoder

class ActividadController:

    def create_actividad(self, actividad: Actividad):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO actividades (titulo, descripcion, tipo, fecha, hora_inicio, hora_fin, grupo) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (actividad.titulo, actividad.descripcion, actividad.tipo, actividad.fecha, actividad.hora_inicio, actividad.hora_fin, actividad.grupo)
            )
            conn.commit()
            return {"resultado": "Actividad creada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_actividad(self, actividad_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM actividades WHERE id = %s", (actividad_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id':            result[0],
                    'titulo':        result[1],
                    'descripcion':   result[2],
                    'tipo':          result[3],
                    'fecha':         str(result[4]),
                    'hora_inicio':   str(result[5]) if result[5] else None,
                    'hora_fin':      str(result[6]) if result[6] else None,
                    'grupo':         result[7],
                    'creado_en':     str(result[8]),
                    'actualizado_en':str(result[9])
                }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="Actividad no encontrada")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_actividades(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM actividades")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id':            data[0],
                    'titulo':        data[1],
                    'descripcion':   data[2],
                    'tipo':          data[3],
                    'fecha':         str(data[4]),
                    'hora_inicio':   str(data[5]) if data[5] else None,
                    'hora_fin':      str(data[6]) if data[6] else None,
                    'grupo':         data[7],
                    'creado_en':     str(data[8]),
                    'actualizado_en':str(data[9])
                }
                payload.append(content)
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_actividad(self, actividad_id: int, actividad: Actividad):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE actividades SET titulo=%s, descripcion=%s, tipo=%s, fecha=%s, hora_inicio=%s, hora_fin=%s, grupo=%s WHERE id=%s",
                (actividad.titulo, actividad.descripcion, actividad.tipo, actividad.fecha, actividad.hora_inicio, actividad.hora_fin, actividad.grupo, actividad_id)
            )
            conn.commit()
            return {"resultado": "Actividad actualizada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_actividad(self, actividad_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM actividades WHERE id = %s", (actividad_id,))
            conn.commit()
            return {"resultado": "Actividad eliminada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()