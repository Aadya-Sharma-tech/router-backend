from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/router-info")
def router_info():
    return jsonify({
        "routerName": "Demo Router",
        "ssid": "Home_WiFi",
        "password": "••••••••"
    })

@app.route("/devices")
def devices():
    return jsonify([
        {"name": "Phone", "ip": "192.168.1.2", "mac": "AA:BB:CC:DD:01"},
        {"name": "Laptop", "ip": "192.168.1.3", "mac": "AA:BB:CC:DD:02"}
    ])

@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json(force=True, silent=True)

        if not data:
            return jsonify({
                "success": False,
                "message": "No JSON received"
            }), 400

        username = data.get("username")
        password = data.get("password")

        if username == "admin" and password == "admin123":
            return jsonify({
                "success": True,
                "token": "dummy-token"
            }), 200

        return jsonify({
            "success": False,
            "message": "Invalid credentials"
        }), 200   # ⚠️ important (not 401)

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
