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
    data = request.json
    if data["username"] == "admin" and data["password"] == "admin123":
        return jsonify({"success": True, "token": "dummy-token"})
    return jsonify({"success": False}), 401

@app.route("/change-password", methods=["POST"])
def change_password():
    return jsonify({"success": True, "newPassword": "NewPass@123"})

@app.route("/logs")
def logs():
    return jsonify([
        {"timestamp": "23 Dec 2025 22:30", "newPassword": "••••••••"}
    ])

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
