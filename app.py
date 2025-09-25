import os
import joblib
import numpy as np
import logging
from flask import Flask, request, jsonify

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)

# --- Cargar modelo ---
try:
    MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models", "breast_cancer_model.pkl")
    model = joblib.load(MODEL_PATH)
    logging.info("Modelo cargado exitosamente desde %s", MODEL_PATH)
except Exception as e:
    logging.error("Error cargando modelo: %s", e)
    model = None

# --- Rutas ---
@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "API funcionando correctamente"})

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Modelo no cargado"}), 500

    try:
        data = request.get_json(force=True)

        if "features" not in data:
            return jsonify({"error": "JSON debe contener 'features'"}), 400

        features = data["features"]

        if not isinstance(features, list):
            return jsonify({"error": "'features' debe ser una lista"}), 400

        # Convertir a numpy array y dar forma correcta
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array).tolist()

        return jsonify({"prediction": prediction})

    except Exception as e:
        logging.error("Error en predicción: %s", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
