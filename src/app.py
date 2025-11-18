"""
API REST para clasificación de flores Iris
"""
from flask import Flask, request, jsonify
import pickle
import numpy as np
import os
from datetime import datetime

app = Flask(__name__)

# Cargar modelo
MODEL_PATH = os.getenv('MODEL_PATH', 'models/model.pkl')
try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    print(f"✅ Modelo cargado desde {MODEL_PATH}")
except Exception as e:
    print(f"❌ Error cargando modelo: {e}")
    model = None

# Nombres de características esperadas
FEATURE_NAMES = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']


@app.route('/')
def home():
    """Endpoint raíz"""
    return jsonify({
        'message': 'Iris ML Classifier API',
        'version': '1.0.0',
        'endpoints': {
            '/health': 'Health check',
            '/predict': 'POST - Predict iris species',
            '/info': 'GET - Model information'
        }
    })


@app.route('/health')
def health():
    """Health check endpoint"""
    is_healthy = model is not None
    return jsonify({
        'status': 'healthy' if is_healthy else 'unhealthy',
        'model_loaded': is_healthy,
        'timestamp': datetime.utcnow().isoformat()
    }), 200 if is_healthy else 503


@app.route('/info')
def info():
    """Información del modelo"""
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 503

    return jsonify({
        'model_type': 'RandomForestClassifier',
        'n_estimators': model.n_estimators,
        'features': FEATURE_NAMES,
        'classes': model.classes_.tolist() if hasattr(model, 'classes_') else []
    })


@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint de predicción

    Espera JSON con formato:
    {
        "SepalLengthCm": 5.1,
        "SepalWidthCm": 3.5,
        "PetalLengthCm": 1.4,
        "PetalWidthCm": 0.2
    }
    """
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 503

    try:
        # Obtener datos del request
        data = request.get_json()

        # Validar que todos los campos estén presentes
        missing_fields = [field for field in FEATURE_NAMES if field not in data]
        if missing_fields:
            return jsonify({
                'error': 'Missing required fields',
                'missing_fields': missing_fields
            }), 400

        # Validar tipos y valores
        for field in FEATURE_NAMES:
            value = data[field]
            if not isinstance(value, (int, float)):
                return jsonify({
                    'error': f'Invalid type for {field}',
                    'expected': 'number',
                    'received': type(value).__name__
                }), 400

            if value < 0:
                return jsonify({
                    'error': f'Invalid value for {field}',
                    'message': 'Values must be positive'
                }), 400

        # Preparar características
        features = np.array([[
            data['SepalLengthCm'],
            data['SepalWidthCm'],
            data['PetalLengthCm'],
            data['PetalWidthCm']
        ]])

        # Realizar predicción
        prediction = model.predict(features)[0]
        probabilities = model.predict_proba(features)[0]

        # Preparar respuesta
        response = {
            'prediction': prediction,
            'probabilities': {
                class_name: float(prob)
                for class_name, prob in zip(model.classes_, probabilities)
            },
            'input': data,
            'timestamp': datetime.utcnow().isoformat()
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            'error': 'Prediction failed',
            'message': str(e)
        }), 500


if __name__ == '__main__':
    port = int(os.getenv('API_PORT', 5000))
    host = os.getenv('API_HOST', '0.0.0.0')
    debug = os.getenv('FLASK_DEBUG', '0') == '1'

    print(f"🚀 Starting Iris ML API on {host}:{port}")
    app.run(host=host, port=port, debug=debug)
