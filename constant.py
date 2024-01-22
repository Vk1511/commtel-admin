from dotenv import load_dotenv
import os

load_dotenv()

COMMTEL_ADMIN_DB_HOST = os.getenv("COMMTEL_ADMIN_DB_HOST")
COMMTEL_ADMIN_DB_PORT = os.getenv("COMMTEL_ADMIN_DB_PORT")
COMMTEL_ADMIN_DB_USER = os.getenv("COMMTEL_ADMIN_DB_USER")
COMMTEL_ADMIN_DB_PASSWORD = os.getenv("COMMTEL_ADMIN_DB_PASSWORD")
COMMTEL_ADMIN_DB_DB = os.getenv("COMMTEL_ADMIN_DB_DB")

KEYCLOAK_SERVER_URL = os.getenv("KEYCLOAK_SERVER_URL")
KEYCLOACK_ADMIN_USERNAME = os.getenv("KEYCLOACK_ADMIN_USERNAME")
KEYCLOACK_ADMIN_PASSWORD = os.getenv("KEYCLOACK_ADMIN_PASSWORD")
KEYCLOACK_REALM_NAME = os.getenv("KEYCLOACK_REALM_NAME")
KEYCLOACK_CLIENT_ID = os.getenv("KEYCLOACK_CLIENT_ID")
KEYCLOACK_CLIENT_SECRET = os.getenv("KEYCLOACK_CLIENT_SECRET")
KEYCLOACK_VERIFY = os.getenv("KEYCLOACK_VERIFY")