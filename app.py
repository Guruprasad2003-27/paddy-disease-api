from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

model = tf.keras.models.load_model("best_model7.h5")

CLASS_NAMES = [
    "Bacterial Leaf Blight",
    "Bacterial Leaf Streak",
    "Bacterial Panicle Blight",
    "Blast",
    "Brown Spot",
    "Dead Heart",
    "Downy Mildew",
    "Hispa",
    "Healthy",
    "Tungro"
]

IMG_SIZE = 224

def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((IMG_SIZE, IMG_SIZE))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Paddy Disease API Running"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        image_file = request.files["image"]
        image_bytes = image_file.read()

        img = preprocess_image(image_bytes)
        predictions = model.predict(img)[0]

        class_index = int(np.argmax(predictions))
        confidence = float(np.max(predictions))

        return jsonify({
            "disease": CLASS_NAMES[class_index],
            "confidence": round(confidence * 100, 2)
        })

    except Exception as e:
        return jsonify({
            "error": "Prediction failed",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run()