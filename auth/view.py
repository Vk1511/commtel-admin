from flask import Blueprint, Response, request, jsonify
from .db_ops import fetch_client_keycloak_details
from datetime import datetime
from keycloak_sdk.keycloak_oid import KeyClockOIDAPI
from auth_svc_sdk.user import AuthSvcAPI

auth_api_bp = Blueprint("auth_api", __name__)


@auth_api_bp.route("/create-user", methods=["POST"])
def create_client_user():
    try:
        try:
            json_data = request.get_json()
            client_id = json_data.get("client_id", None)
            role = json_data.get("role", None)
            email = json_data.get("email", None)
            first_name = json_data.get("first_name", None)
            last_name = json_data.get("last_name", None)

        except Exception as e:
            raise Exception("API body is missing!")

        client_data = fetch_client_keycloak_details(client_id=client_id)
        keyclaok_oid_obj = KeyClockOIDAPI(
            keyclaok_server_url=client_data[2],
            keyclaok_client_id=client_data[3],
            keycloak_realm_name=client_data[5],
            keycloak_client_secret=client_data[4],
        )
        token = keyclaok_oid_obj.get_token(
            keyclaok_user=client_data[6], keycloak_user_password=client_data[7]
        )
        access_token = token.get("access_token")

        auth_svc_obj = AuthSvcAPI()
        permission = auth_svc_obj.get_role_default_permission(
            token=access_token, role=role
        )

        user = auth_svc_obj.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            role=role,
            permission=permission,
            token=access_token,
        )

        if user["status"]:
            return (
                jsonify(
                    {
                        "status": "success",
                        "data": "User created successfully!",
                        "timestamp": datetime.now(),
                    }
                ),
                200,
            )
        else:
            raise Exception("Something went wrong!")
    except Exception as e:
        error = {"code": 500, "message": str(e)}
        return (
            jsonify({"status": "failed", "data": error, "timestamp": datetime.now()}),
            200,
        )


