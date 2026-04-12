import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.nino_model import Nino
from fastapi.encoders import jsonable_encoder

class NinoController:

    def create_nino(self, nino: Nino):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO ninos 
                (nombre, apellido, fecha_nacimiento, genero, foto_url, grupo, grupo_id,
                activo, tipo_sangre, medico_nombre, medico_telefono, 
                seguro_medico, observaciones_medicas) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (nino.nombre, nino.apellido, nino.fecha_nacimiento, nino.genero,
                 nino.foto_url, nino.grupo, nino.grupo_id, nino.activo, nino.tipo_sangre,
                 nino.medico_nombre, nino.medico_telefono, nino.seguro_medico,
                 nino.observaciones_medicas)
            )
            conn.commit()
            return {"resultado": "Nino creado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_nino(self, nino_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ninos WHERE id = %s", (nino_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id':                    result[0],
                    'nombre':                result[1],
                    'apellido':              result[2],
                    'fecha_nacimiento':      str(result[3]),
                    'genero':                result[4],
                    'foto_url':              result[5],
                    'grupo':                 result[6],
                    'fecha_ingreso':         str(result[7]),
                    'activo':                result[8],
                    'tipo_sangre':           result[9],
                    'medico_nombre':         result[10],
                    'medico_telefono':       result[11],
                    'seguro_medico':         result[12],
                    'observaciones_medicas': result[13],
                    'creado_en':             str(result[14]),
                    'actualizado_en':        str(result[15]),
                    'grupo_id':              result[16]
                }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="Nino no encontrado")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_ninos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ninos")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id':                    data[0],
                    'nombre':                data[1],
                    'apellido':              data[2],
                    'fecha_nacimiento':      str(data[3]),
                    'genero':                data[4],
                    'foto_url':              data[5],
                    'grupo':                 data[6],
                    'fecha_ingreso':         str(data[7]),
                    'activo':                data[8],
                    'tipo_sangre':           data[9],
                    'medico_nombre':         data[10],
                    'medico_telefono':       data[11],
                    'seguro_medico':         data[12],
                    'observaciones_medicas': data[13],
                    'creado_en':             str(data[14]),
                    'actualizado_en':        str(data[15]),
                    'grupo_id':              data[16]
                }
                payload.append(content)
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_ninos_by_grupo(self, grupo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ninos WHERE grupo_id = %s AND activo = TRUE", (grupo_id,))
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id':                    data[0],
                    'nombre':                data[1],
                    'apellido':              data[2],
                    'fecha_nacimiento':      str(data[3]),
                    'genero':                data[4],
                    'foto_url':              data[5],
                    'grupo':                 data[6],
                    'fecha_ingreso':         str(data[7]),
                    'activo':                data[8],
                    'tipo_sangre':           data[9],
                    'medico_nombre':         data[10],
                    'medico_telefono':       data[11],
                    'seguro_medico':         data[12],
                    'observaciones_medicas': data[13],
                    'creado_en':             str(data[14]),
                    'actualizado_en':        str(data[15]),
                    'grupo_id':              data[16]
                }
                payload.append(content)
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_nino(self, nino_id: int, nino: Nino):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE ninos SET nombre=%s, apellido=%s, fecha_nacimiento=%s, genero=%s,
                foto_url=%s, grupo=%s, grupo_id=%s, activo=%s, tipo_sangre=%s,
                medico_nombre=%s, medico_telefono=%s, seguro_medico=%s,
                observaciones_medicas=%s WHERE id=%s""",
                (nino.nombre, nino.apellido, nino.fecha_nacimiento, nino.genero,
                 nino.foto_url, nino.grupo, nino.grupo_id, nino.activo, nino.tipo_sangre,
                 nino.medico_nombre, nino.medico_telefono, nino.seguro_medico,
                 nino.observaciones_medicas, nino_id)
            )
            conn.commit()
            return {"resultado": "Nino actualizado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_nino(self, nino_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE ninos SET activo = FALSE WHERE id = %s", (nino_id,))
            conn.commit()
            return {"resultado": "Nino desactivado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def registrar_nino_completo(self, datos: dict):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            nino      = datos['nino']
            acudiente = datos['acudiente']

            # 1. Crear o buscar acudiente
            if acudiente.get('id'):
                acudiente_id = acudiente['id']
            else:
                cursor.execute(
                    """INSERT INTO acudientes 
                    (nombre, apellido, dni, telefono, telefono_emergencia, email, direccion, relacion)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id""",
                    (acudiente['nombre'], acudiente['apellido'], acudiente.get('dni'),
                    acudiente.get('telefono'), acudiente.get('telefono_emergencia'),
                    acudiente.get('email'), acudiente.get('direccion'), acudiente.get('relacion', 'otro'))
                )
                acudiente_id = cursor.fetchone()[0]

            # 2. Crear niño
            cursor.execute(
                """INSERT INTO ninos 
                (nombre, apellido, fecha_nacimiento, genero, grupo, grupo_id,
                tipo_sangre, medico_nombre, medico_telefono, seguro_medico, observaciones_medicas)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id""",
                (nino['nombre'], nino['apellido'], nino['fecha_nacimiento'],
                nino.get('genero'), nino.get('grupo'), nino.get('grupo_id'),
                nino.get('tipo_sangre'), nino.get('medico_nombre'),
                nino.get('medico_telefono'), nino.get('seguro_medico'),
                nino.get('observaciones_medicas'))
            )
            nino_id = cursor.fetchone()[0]

            # 3. Crear relación nino-acudiente
            cursor.execute(
                """INSERT INTO nino_acudiente 
                (nino_id, acudiente_id, es_contacto_principal, puede_recoger)
                VALUES (%s, %s, TRUE, TRUE)""",
                (nino_id, acudiente_id)
            )

            conn.commit()
            return {
                "resultado": "Nino registrado correctamente",
                "nino_id":      nino_id,
                "acudiente_id": acudiente_id
            }

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
            return {"error": str(err)}
        finally:
            conn.close()