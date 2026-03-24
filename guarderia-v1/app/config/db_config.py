import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host="aws-0-us-west-2.pooler.supabase.com",
        port=5432,
        database="postgres",
        user="postgres.ilbbknzbfbmzpzineojv",
        password="Supabase2026*"
    )
    return conn