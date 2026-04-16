import psycopg2
import os

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host="aws-0-us-west-2.pooler.supabase.com",
            port=6543,
            database="postgres",
            user="postgres.ilbbknzbfbmzpzineojv",
            password="zPPQYrCSnhAHd1KE"
        )
        return conn
    except Exception as e:
        print(f"Error: {e}")
        return None

# CONEXION A LA BASE DE DATOS DE RESPALDO EN NEON
# import psycopg2
# import os

# def get_db_connection():
#     try:
#         db_url = "postgresql://neondb_owner:npg_Bivq23cHdnLe@ep-misty-glade-amirk0iq-pooler.c-5.us-east-1.aws.neon.tech/neondb?sslmode=require"
        
#         conn = psycopg2.connect(db_url)
#         return conn
#     except Exception as e:
#         print("\n==================================================")
#         print(f"ERROR DE CONEXIÓN EN NEON: {e}")
#         print("==================================================\n")
#         return None
