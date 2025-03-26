import tensorflow as tf
from flask import Flask, request, jsonify
import numpy as np
import joblib

# Cargar el modelo entrenado
model = tf.keras.models.load_model("modelo_housing.h5")
scaler = joblib.load("scaler.pkl")

# Crear la API con Flask
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_features = np.array(data['features']).reshape(1, -1)  # Asegurar que es 2D
        input_scaled = scaler.transform(input_features)  # Normalizar
        prediction = model.predict(input_scaled)
        return jsonify({'predicted_price': float(prediction[0][0])})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
