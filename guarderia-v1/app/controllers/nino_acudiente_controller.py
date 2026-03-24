import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.nino_acudiente_model import NinoAcudiente
from fastapi.encoders import jsonable_encoder

class NinoAcudienteController:

    def create_nino_acudiente(self, na: NinoAcudiente):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO nino_acudiente (nino_id, acudiente_id, es_contacto_principal, puede_recoger) VALUES (%s, %s, %s, %s)",
                (na.nino_id, na.acudiente_id, na.es_contacto_principal, na.puede_recoger)
            )
            conn.commit()
            return {"resultado": "Relacion nino-acudiente creada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_nino_acudiente(self, na_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM nino_acudiente WHERE id = %s", (na_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id':                   result[0],
                    'nino_id':              result[1],
                    'acudiente_id':         result[2],
                    'es_contacto_principal':result[3],
                    'puede_recoger':        result[4],
                    'creado_en':            str(result[5])
                }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="Relacion no encontrada")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_ninos_acudientes(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM nino_acudiente")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id':                   data[0],
                    'nino_id':              data[1],
                    'acudiente_id':         data[2],
                    'es_contacto_principal':data[3],
                    'puede_recoger':        data[4],
                    'creado_en':            str(data[5])
                }
                payload.append(content)
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_nino_acudiente(self, na_id: int, na: NinoAcudiente):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE nino_acudiente SET nino_id=%s, acudiente_id=%s, es_contacto_principal=%s, puede_recoger=%s WHERE id=%s",
                (na.nino_id, na.acudiente_id, na.es_contacto_principal, na.puede_recoger, na_id)
            )
            conn.commit()
            return {"resultado": "Relacion actualizada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_nino_acudiente(self, na_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM nino_acudiente WHERE id = %s", (na_id,))
            conn.commit()
            return {"resultado": "Relacion eliminada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()