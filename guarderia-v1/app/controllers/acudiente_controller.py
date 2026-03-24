import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.acudiente_model import Acudiente
from fastapi.encoders import jsonable_encoder

class AcudienteController:

    def create_acudiente(self, acudiente: Acudiente):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO acudientes (nombre, apellido, dni, telefono, telefono_emergencia, email, direccion, relacion, activo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (acudiente.nombre, acudiente.apellido, acudiente.dni, acudiente.telefono, acudiente.telefono_emergencia, acudiente.email, acudiente.direccion, acudiente.relacion, acudiente.activo)
            )
            conn.commit()
            return {"resultado": "Acudiente creado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_acudiente(self, acudiente_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM acudientes WHERE id = %s", (acudiente_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id':                   result[0],
                    'nombre':               result[1],
                    'apellido':             result[2],
                    'dni':                  result[3],
                    'telefono':             result[4],
                    'telefono_emergencia':  result[5],
                    'email':                result[6],
                    'direccion':            result[7],
                    'relacion':             result[8],
                    'activo':               result[9],
                    'creado_en':            str(result[10]),
                    'actualizado_en':       str(result[11])
                }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="Acudiente no encontrado")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_acudientes(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM acudientes")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id':                   data[0],
                    'nombre':               data[1],
                    'apellido':             data[2],
                    'dni':                  data[3],
                    'telefono':             data[4],
                    'telefono_emergencia':  data[5],
                    'email':                data[6],
                    'direccion':            data[7],
                    'relacion':             data[8],
                    'activo':               data[9],
                    'creado_en':            str(data[10]),
                    'actualizado_en':       str(data[11])
                }
                payload.append(content)
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_acudiente(self, acudiente_id: int, acudiente: Acudiente):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE acudientes SET nombre=%s, apellido=%s, dni=%s, telefono=%s, telefono_emergencia=%s, email=%s, direccion=%s, relacion=%s, activo=%s WHERE id=%s",
                (acudiente.nombre, acudiente.apellido, acudiente.dni, acudiente.telefono, acudiente.telefono_emergencia, acudiente.email, acudiente.direccion, acudiente.relacion, acudiente.activo, acudiente_id)
            )
            conn.commit()
            return {"resultado": "Acudiente actualizado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_acudiente(self, acudiente_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE acudientes SET activo = FALSE WHERE id = %s", (acudiente_id,))
            conn.commit()
            return {"resultado": "Acudiente desactivado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()