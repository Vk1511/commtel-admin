from keycloak import KeycloakOpenID
from constant import (
    KEYCLOAK_SERVER_URL,
    KEYCLOACK_ADMIN_USERNAME,
    KEYCLOACK_ADMIN_PASSWORD,
    KEYCLOACK_REALM_NAME,
    KEYCLOACK_CLIENT_ID,
    KEYCLOACK_CLIENT_SECRET,
    KEYCLOACK_VERIFY,
)


class KeyClockOIDAPI:
    _keycloak_oid = None

    def __init__(
        self,
    ):
        # initializing keycloak open id client
        self._keycloak_oid = KeycloakOpenID(
            server_url=KEYCLOAK_SERVER_URL,
            client_id=KEYCLOACK_CLIENT_ID,
            realm_name=KEYCLOACK_REALM_NAME,
            client_secret_key=KEYCLOACK_CLIENT_SECRET,
            verify=KEYCLOACK_VERIFY,
        )

    @classmethod
    def factory(
        cls,
    ):
        if not cls._keycloak_oid:
            cls._keycloak_oid = cls()

        return cls._keycloak_oid

    # creating user
    def get_token(self):
        try:
            return self._keycloak_oid.token(
                KEYCLOACK_ADMIN_USERNAME, KEYCLOACK_ADMIN_PASSWORD
            )
        except Exception as e:
            print(
                self.__class__.__name__,
                ": Exception when getting tocken for user",
                str(e),
            )
            raise e
