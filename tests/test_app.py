"""
Tests unitarios para la API Flask
"""
import pytest
import json
import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar desde src
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
    assert response.status_code in [200, 503]
    data = json.loads(response.data)
    assert 'status' in data
    assert 'model_loaded' in data

def test_info_endpoint(client):
    """Test del endpoint de información"""
    response = client.get('/info')
    data = json.loads(response.data)
    
    if response.status_code == 200:
        assert 'model_type' in data
        assert 'features' in data
    else:
        assert response.status_code == 503

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
    
    if response.status_code == 200:
        data = json.loads(response.data)
        assert 'prediction' in data
        assert 'probabilities' in data
        assert data['prediction'] in ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

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
