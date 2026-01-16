from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Paddy Disease API Running"

@app.route("/predict", methods=["POST"])
def predict():
    if 'image' not in request.files:
        return jsonify({"prediction": "No image received"})

    image = request.files['image']

    # 🔴 TEMP DUMMY PREDICTION (WE WILL ADD MODEL LATER)
    return jsonify({
        "prediction": "Bacterial Leaf Blight"
    })

if __name__ == "__main__":
    app.run()