"""
Tests unitarios para la API Flask
"""
import pytest
import json
import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Asegurarse de que el modelo existe antes de importar la app
model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'model.pkl')
if not os.path.exists(model_path):
    from src.train_model import train_model
    print("⚠️  Modelo no encontrado. Entrenando...")
    train_model()

# Importar la app
from src.app import app


@pytest.fixture
def client():
    """Fixture para el cliente de pruebas"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    """Test del endpoint raíz"""
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data
    assert 'version' in data


def test_health_endpoint(client):
    """Test del health check"""
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'status' in data
    assert data['status'] == 'healthy'


def test_info_endpoint(client):
    """Test del endpoint de información"""
    response = client.get('/info')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'model_type' in data
    assert 'features' in data


def test_predict_valid_input(client):
    """Test de predicción con entrada válida"""
    payload = {
        'SepalLengthCm': 5.1,
        'SepalWidthCm': 3.5,
        'PetalLengthCm': 1.4,
        'PetalWidthCm': 0.2
    }
    
    response = client.post(
        '/predict',
        data=json.dumps(payload),
        content_type='application/json'
    )
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'prediction' in data
    assert 'probabilities' in data


def test_predict_missing_fields(client):
    """Test con campos faltantes"""
    payload = {
        'SepalLengthCm': 5.1,
        'SepalWidthCm': 3.5
    }
    
    response = client.post(
        '/predict',
        data=json.dumps(payload),
        content_type='application/json'
    )
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data


def test_predict_invalid_type(client):
    """Test con tipo de dato inválido"""
    payload = {
        'SepalLengthCm': 'invalid',
        'SepalWidthCm': 3.5,
        'PetalLengthCm': 1.4,
        'PetalWidthCm': 0.2
    }
    
    response = client.post(
        '/predict',
        data=json.dumps(payload),
        content_type='application/json'
    )
    
    assert response.status_code == 400


def test_predict_negative_values(client):
    """Test con valores negativos"""
    payload = {
        'SepalLengthCm': -1.0,
        'SepalWidthCm': 3.5,
        'PetalLengthCm': 1.4,
        'PetalWidthCm': 0.2
    }
    
    response = client.post(
        '/predict',
        data=json.dumps(payload),
        content_type='application/json'
    )
    
    assert response.status_code == 400


def test_predict_boundary_values(client):
    """Test con valores pequeños positivos"""
    payload = {
        'SepalLengthCm': 0.1,
        'SepalWidthCm': 0.1,
        'PetalLengthCm': 0.1,
        'PetalWidthCm': 0.1
    }
    
    response = client.post(
        '/predict',
        data=json.dumps(payload),
        content_type='application/json'
    )
    
    assert response.status_code == 200


def test_predict_all_fields_present(client):
    """Test verificando que todos los campos sean procesados"""
    payload = {
        'SepalLengthCm': 6.5,
        'SepalWidthCm': 3.0,
        'PetalLengthCm': 5.2,
        'PetalWidthCm': 2.0
    }
    
    response = client.post(
        '/predict',
        data=json.dumps(payload),
        content_type='application/json'
    )
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'input' in data
    assert data['input'] == payload

def test_predict_with_floats(client):
    """Test con diferentes valores float"""
    payload = {
        'SepalLengthCm': 5.84,
        'SepalWidthCm': 3.05,
        'PetalLengthCm': 4.35,
        'PetalWidthCm': 1.3
    }
    
    response = client.post(
        '/predict',
        data=json.dumps(payload),
        content_type='application/json'
    )
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'probabilities' in data
    assert len(data['probabilities']) == 3
