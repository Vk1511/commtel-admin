from keycloak import KeycloakOpenID
from constant import (
    KEYCLOACK_ADMIN_USERNAME,
    KEYCLOACK_ADMIN_PASSWORD,
    KEYCLOACK_VERIFY,
)


class KeyClockOIDAPI:
    _keycloak_oid = None

    def __init__(
        self,
        keyclaok_server_url,
        keyclaok_client_id,
        keycloak_realm_name,
        keycloak_client_secret,
    ):
        # initializing keycloak open id client
        self._keycloak_oid = KeycloakOpenID(
            server_url=keyclaok_server_url,
            client_id=keyclaok_client_id,
            realm_name=keycloak_realm_name,
            client_secret_key=keycloak_client_secret,
            verify=KEYCLOACK_VERIFY,
        )

    @classmethod
    def factory(
        cls,
        keyclaok_server_url,
        keyclaok_client_id,
        keycloak_realm_name,
        keycloak_client_secret,
    ):
        if not cls._keycloak_oid:
            cls._keycloak_oid = cls(
                keyclaok_server_url,
                keyclaok_client_id,
                keycloak_realm_name,
                keycloak_client_secret,
            )

        return cls._keycloak_oid

    # creating user
    def get_token(self, keyclaok_user, keycloak_user_password):
        try:
            return self._keycloak_oid.token(keyclaok_user, keycloak_user_password)
        except Exception as e:
            print(
                self.__class__.__name__,
                ": Exception when getting tocken for user",
                str(e),
            )
            raise e
