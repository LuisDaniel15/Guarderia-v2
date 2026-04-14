import psycopg2
import os

def get_db_connection():
    try:
        # Tu nueva URL de Neon
        # El parámetro sslmode=require es obligatorio en Neon
        db_url = "postgresql://neondb_owner:npg_Bivq23cHdnLe@ep-misty-glade-amirk0iq-pooler.c-5.us-east-1.aws.neon.tech/neondb?sslmode=require"
        
        conn = psycopg2.connect(db_url)
        return conn
    except Exception as e:
        print("\n==================================================")
        print(f"❌ ERROR DE CONEXIÓN EN NEON: {e}")
        print("==================================================\n")
        return None

    # Supabase3115*