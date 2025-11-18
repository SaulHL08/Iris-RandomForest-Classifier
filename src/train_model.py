"""
Script para entrenar el modelo Random Forest
"""
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import os


def train_model():
    """Entrena el modelo y lo guarda"""

    # Cargar datos
    print("📊 Cargando datos...")
    data = pd.read_csv('data/Iris.csv')

    # Preparar datos
    X = data.drop(["Id", "Species"], axis=1)
    y = data["Species"]

    # Dividir datos
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Entrenar modelo
    print("🤖 Entrenando modelo...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluar
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"✅ Precisión del modelo: {accuracy * 100:.2f}%")
    print("\n📋 Reporte de clasificación:")
    print(classification_report(y_test, y_pred))

    # Guardar modelo
    os.makedirs('models', exist_ok=True)
    with open('models/model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("💾 Modelo guardado en models/model.pkl")


if __name__ == "__main__":
    train_model()
