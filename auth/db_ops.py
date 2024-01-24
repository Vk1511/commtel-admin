import psycopg2
from constant import (
    COMMTEL_ADMIN_DB_HOST,
    COMMTEL_ADMIN_DB_PORT,
    COMMTEL_ADMIN_DB_USER,
    COMMTEL_ADMIN_DB_PASSWORD,
    COMMTEL_ADMIN_DB_DB,
)


# creating connection with commtel-admin DB
def connection_admin_db():
    try:
        conn = psycopg2.connect(
            host=COMMTEL_ADMIN_DB_HOST,
            database=COMMTEL_ADMIN_DB_DB,
            user=COMMTEL_ADMIN_DB_USER,
            password=COMMTEL_ADMIN_DB_PASSWORD,
            port=COMMTEL_ADMIN_DB_PORT,
        )
        return conn
    except Exception as e:
        print("Failed to connect with commtel-admin DB!")
        raise e


# fetching client's keycloak cred based on client id
def fetch_client_keycloak_details(client_id):
    conn = connection_admin_db()
    cur = conn.cursor()
    sql = (
        f"select * from client_keycloak_mapping where cast(id as TEXT) = '{client_id}';"
    )
    cur.execute(sql)
    client_data = cur.fetchone()
    cur.close()
    conn.close()
    if not client_data:
        raise Exception("Invalid client id passed!")
    return client_data
