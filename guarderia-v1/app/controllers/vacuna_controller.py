import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.vacuna_model import Vacuna
from fastapi.encoders import jsonable_encoder

class VacunaController:

    def create_vacuna(self, vacuna: Vacuna):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO vacunas (nino_id, nombre, fecha_aplicacion, proxima_dosis, notas) VALUES (%s, %s, %s, %s, %s)",
                (vacuna.nino_id, vacuna.nombre, vacuna.fecha_aplicacion, vacuna.proxima_dosis, vacuna.notas)
            )
            conn.commit()
            return {"resultado": "Vacuna creada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_vacuna(self, vacuna_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vacunas WHERE id = %s", (vacuna_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id':               result[0],
                    'nino_id':          result[1],
                    'nombre':           result[2],
                    'fecha_aplicacion': str(result[3]),
                    'proxima_dosis':    str(result[4]) if result[4] else None,
                    'notas':            result[5],
                    'creado_en':        str(result[6])
                }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="Vacuna no encontrada")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_vacunas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vacunas")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id':               data[0],
                    'nino_id':          data[1],
                    'nombre':           data[2],
                    'fecha_aplicacion': str(data[3]),
                    'proxima_dosis':    str(data[4]) if data[4] else None,
                    'notas':            data[5],
                    'creado_en':        str(data[6])
                }
                payload.append(content)
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_vacuna(self, vacuna_id: int, vacuna: Vacuna):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE vacunas SET nino_id=%s, nombre=%s, fecha_aplicacion=%s, proxima_dosis=%s, notas=%s WHERE id=%s",
                (vacuna.nino_id, vacuna.nombre, vacuna.fecha_aplicacion, vacuna.proxima_dosis, vacuna.notas, vacuna_id)
            )
            conn.commit()
            return {"resultado": "Vacuna actualizada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_vacuna(self, vacuna_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM vacunas WHERE id = %s", (vacuna_id,))
            conn.commit()
            return {"resultado": "Vacuna eliminada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()