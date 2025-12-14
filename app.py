from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/routes", methods=["POST"])
def routes():
    return jsonify({
        "routes": [
            {"mode": "Train", "distance": 200, "co2": 8, "score": 9},
            {"mode": "Bus", "distance": 200, "co2": 20, "score": 7},
            {"mode": "Car", "distance": 200, "co2": 36, "score": 5}
        ]
    })
