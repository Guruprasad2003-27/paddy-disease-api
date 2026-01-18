import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return {"status": "Paddy Disease API running"}

@app.route("/predict", methods=["POST"])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    # TEMP dummy response (we’ll connect model later)
    return jsonify({
    "disease": disease_name,
    "confidence": round(confidence * 100, 2),
    "fertilizer": fertilizer,
    "medicine": medicine,
    "advice": advice
})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
