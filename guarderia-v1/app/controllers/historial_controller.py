import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.historial_model import Historial
from fastapi.encoders import jsonable_encoder

class HistorialController:

    def create_historial(self, historial: Historial):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO historial 
                (autor_id, categoria, titulo, descripcion, fecha, medidas_tomadas, 
                acudiente_notificado, es_privado) 
                VALUES (%s, %s, %s, %s, COALESCE(%s, CURRENT_DATE), %s, %s, %s)""",
                (historial.autor_id, historial.categoria, historial.titulo,
                 historial.descripcion, historial.fecha, historial.medidas_tomadas,
                 historial.acudiente_notificado, historial.es_privado)
            )
            conn.commit()
            return {"resultado": "Historial creado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_historial(self, historial_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM historial WHERE id = %s", (historial_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id':                   result[0],
                    'autor_id':             result[1],
                    'categoria':            result[2],
                    'titulo':               result[3],
                    'descripcion':          result[4],
                    'fecha':                str(result[5]),
                    'medidas_tomadas':      result[6],
                    'acudiente_notificado': result[7],
                    'es_privado':           result[8],
                    'creado_en':            str(result[9]),
                    'actualizado_en':       str(result[10])
                }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="Historial no encontrado")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_historiales(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM historial")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id':                   data[0],
                    'autor_id':             data[1],
                    'categoria':            data[2],
                    'titulo':               data[3],
                    'descripcion':          data[4],
                    'fecha':                str(data[5]),
                    'medidas_tomadas':      data[6],
                    'acudiente_notificado': data[7],
                    'es_privado':           data[8],
                    'creado_en':            str(data[9]),
                    'actualizado_en':       str(data[10])
                }
                payload.append(content)
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_historial(self, historial_id: int, historial: Historial):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE historial SET autor_id=%s, categoria=%s, titulo=%s, descripcion=%s, fecha=%s, medidas_tomadas=%s, acudiente_notificado=%s, es_privado=%s WHERE id=%s",
                (historial.autor_id, historial.categoria, historial.titulo, historial.descripcion, historial.fecha, historial.medidas_tomadas, historial.acudiente_notificado, historial.es_privado, historial_id)
            )
            conn.commit()
            return {"resultado": "Historial actualizado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_historial(self, historial_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM historial WHERE id = %s", (historial_id,))
            conn.commit()
            return {"resultado": "Historial eliminado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()