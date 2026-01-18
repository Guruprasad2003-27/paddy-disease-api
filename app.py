from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import io
from PIL import Image
import tensorflow as tf
from tensorflow.keras.utils import img_to_array
from recommendation import recommend_treatment

app = Flask(__name__)
CORS(app)
# ✅ Load model (IMPORTANT: compile=False)
model = tf.keras.models.load_model("best_model7.h5", compile=False)

# ✅ Class labels (must match training order)
class_names = [
    "bacterial_leaf_blight",
    "bacterial_leaf_streak",
    "bacterial_panicle_blight",
    "bacterial_panicle_blight",
    "blast",
    "brown_spot",
    "dead_heart",
    "downy_mildew",
    "hispa",
    "normal",
    "tungro"
]

@app.route("/")
def home():
    return "✅ Paddy Disease Detection API is running"

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]

    try:
        # ✅ Read image from request
        image = Image.open(io.BytesIO(file.read())).convert("RGB")
        image = image.resize((224, 224))

        # ✅ Preprocess
        img_array = img_to_array(image)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0

        # ✅ Prediction
        predictions = model.predict(img_array)
        class_idx = int(np.argmax(predictions))
        confidence = float(np.max(predictions)) * 100

        disease = class_names[class_idx]
        recommendation = recommend_treatment(disease)

        return jsonify({
            "disease": disease,
            "confidence": round(confidence, 2),
            "fertilizer": recommendation["fertilizer"],
            "medicine": recommendation["medicine"],
            "advice": recommendation["advice"]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ⚠️ IMPORTANT FOR RENDER
# ❌ Do NOT use app.run() in production
# Gunicorn will handle running the app