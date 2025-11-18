"""
Configuración de pytest
"""
import os
import sys

# Agregar src al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def pytest_configure(config):
    """Configuración antes de ejecutar tests"""
    # Asegurarse de que el modelo existe
    model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'model.pkl')
    if not os.path.exists(model_path):
        print("\n⚠️  Modelo no encontrado. Entrenando...")
        from src.train_model import train_model
        train_model()
        print("✅ Modelo entrenado correctamente\n")
