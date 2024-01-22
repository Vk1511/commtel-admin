from flask import Blueprint, Response, request, jsonify
from db_ops import fetch_client_keycloak_details
from datetime import datetime

auth_api_bp = Blueprint("auth_api", __name__)


@auth_api_bp.route("/create-user", methods=["POST"])
def create_client_user():
    try:
        try:
            json_data = request.get_json()
            client_id = json_data.get("client_id", None)
        except Exception as e:
            raise Exception("API body is missing!")

        client_data = fetch_client_keycloak_details(client_id=client_id)

        return (
            jsonify({"status": "success", "data": "data", "timestamp": datetime.now()}),
            200,
        )
    except Exception as e:
        error = {"code": 500, "message": str(e)}
        return (
            jsonify({"status": "failed", "data": error, "timestamp": datetime.now()}),
            200,
        )
