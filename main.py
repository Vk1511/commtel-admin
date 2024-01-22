from flask import Flask, request, render_template, jsonify
import psycopg2
from flask_cors import CORS
from datetime import datetime
from auth.view import auth_api_bp

app = Flask(__name__)


app.register_blueprint(auth_api_bp)


@app.route("/test", methods=["GET"])
def trendingdataredis():
    try:
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


if __name__ == "__main__":
    app.run()
