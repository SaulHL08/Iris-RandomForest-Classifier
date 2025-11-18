# 🌸 Iris ML Classifier - DevOps Project

![CI Status](https://github.com/SaulHL08/Iris-RandomForest-Classifier/workflows/CI%20Pipeline/badge.svg)
![Docker](https://img.shields.io/docker/v/saulhl08/iris-ml-classifier?label=docker)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)

Sistema completo de clasificación de flores Iris con Machine Learning, containerización y despliegue automatizado usando prácticas DevOps.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Arquitectura](#arquitectura)
- [Tecnologías](#tecnologías)
- [Instalación](#instalación)
- [Uso](#uso)
- [Testing](#testing)
- [Docker](#docker)
- [CI/CD](#cicd)
- [Despliegue](#despliegue)

## ✨ Características

- 🤖 Modelo Random Forest para clasificación de especies Iris
- 🚀 API REST con Flask
- 🐳 Containerización con Docker
- ⚙️ CI/CD con GitHub Actions
- 🏗️ Infraestructura como Código (Terraform + Ansible)
- 🧪 Tests automatizados con pytest
- 🔒 Prácticas de seguridad implementadas
- 📊 Monitoreo y health checks

## 🏗️ Arquitectura

El proyecto utiliza una arquitectura cliente-servidor con los siguientes componentes:

- **API REST**: Flask application serving ML predictions
- **ML Model**: Random Forest Classifier entrenado con dataset Iris
- **Container**: Docker para portabilidad
- **Infrastructure**: AWS EC2 con Terraform y Ansible
- **CI/CD**: GitHub Actions para testing y despliegue automatizado

## 🛠️ Tecnologías

### Backend
- Python 3.8+
- Flask 3.0
- scikit-learn 1.3
- pandas 2.0
- numpy 1.24

### DevOps
- Docker 20.10+
- Terraform 1.6+
- Ansible 2.9+
- GitHub Actions

### Cloud
- AWS (EC2, VPC, Security Groups)

## 📦 Instalación

### Opción 1: Instalación Local
```bash
# Clonar repositorio
git clone https://github.com/SaulHL08/Iris-RandomForest-Classifier.git
cd Iris-RandomForest-Classifier

# Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Entrenar modelo (si no existe)
python src/train_model.py

# Ejecutar API
python src/app.py
```

### Opción 2: Docker
```bash
# Opción 2a: Construir localmente
docker build -t iris-ml-classifier .
docker run -p 5000:5000 iris-ml-classifier

# Opción 2b: Usar imagen de Docker Hub (cuando esté disponible)
docker pull saulhl08/iris-ml-classifier:latest
docker run -p 5000:5000 saulhl08/iris-ml-classifier:latest

# Opción 2c: Docker Compose
docker-compose up -d
```

## 🚀 Uso

### API Endpoints

#### Health Check
```bash
curl http://localhost:5000/health
```

**Respuesta:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "timestamp": "2024-11-18T08:30:00.000000"
}
```

#### Información del Modelo
```bash
curl http://localhost:5000/info
```

#### Predicción
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "SepalLengthCm": 5.1,
    "SepalWidthCm": 3.5,
    "PetalLengthCm": 1.4,
    "PetalWidthCm": 0.2
  }'
```

**Respuesta:**
```json
{
  "prediction": "Iris-setosa",
  "probabilities": {
    "Iris-setosa": 1.0,
    "Iris-versicolor": 0.0,
    "Iris-virginica": 0.0
  },
  "input": {
    "SepalLengthCm": 5.1,
    "SepalWidthCm": 3.5,
    "PetalLengthCm": 1.4,
    "PetalWidthCm": 0.2
  },
  "timestamp": "2024-11-18T08:30:00.000000"
}
```

## 🧪 Testing
```bash
# Ejecutar todos los tests
pytest tests/ -v

# Con cobertura
pytest tests/ --cov=src --cov-report=html

# Ver reporte de cobertura
open htmlcov/index.html  # Linux: xdg-open htmlcov/index.html
```

## 🐳 Docker

### Build
```bash
docker build -t iris-ml-classifier:latest .
```

### Run
```bash
docker run -d \
  -p 5000:5000 \
  --name iris-ml-api \
  iris-ml-classifier:latest
```

### Logs
```bash
docker logs -f iris-ml-api
```

### Stop y Remove
```bash
docker stop iris-ml-api
docker rm iris-ml-api
```

## ⚙️ CI/CD

### Continuous Integration

Cada push o pull request ejecuta automáticamente:

1. ✅ Lint con flake8
2. 🧪 Tests con pytest
3. 📊 Análisis de cobertura
4. 🐳 Build de Docker image
5. 🔒 Escaneo de seguridad con Trivy

Ver el estado del pipeline en: [GitHub Actions](https://github.com/SaulHL08/Iris-RandomForest-Classifier/actions)

## 🚢 Despliegue

### Paso 1: Provisionar Infraestructura con Terraform
```bash
cd IaC/terraform
terraform init
terraform plan
terraform apply
```

### Paso 2: Desplegar Aplicación con Ansible
```bash
cd IaC/ansible
cp inventory.ini.example inventory.ini
# Editar inventory.ini con la IP de EC2
ansible-playbook deploy.yml
```

## 🔒 Seguridad

- ✅ Contenedores con usuario no-root
- ✅ Validación de entrada en API
- ✅ Secrets management con variables de entorno
- ✅ Escaneo de vulnerabilidades en CI
- ✅ Security Groups restrictivos en AWS
- ✅ Health checks configurados

## 📚 Documentación Adicional

- [Documentación del Modelo](Documentación%20del%20modelo.md)
- [Guía de Terraform](IaC/terraform/README.md)
- [Guía de Ansible](IaC/ansible/README.md)

## 👥 Autor

- **Saúl Hernández Latiznere** - [SaulHL08](https://github.com/SaulHL08)

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

## 🙏 Agradecimientos

- Dataset: [Iris Flower Dataset](https://archive.ics.uci.edu/ml/datasets/iris)
- Frameworks: Flask, scikit-learn
- Infrastructure: AWS, Terraform, Ansible

---

⭐ Si este proyecto te fue útil, considera darle una estrella!

## 📞 Estructura del Proyecto
```
Iris-RandomForest-Classifier/
├── .github/
│   └── workflows/
│       └── ci.yml              # Pipeline CI/CD
├── src/
│   ├── app.py                  # API Flask
│   └── train_model.py          # Entrenamiento del modelo
├── tests/
│   ├── __init__.py
│   └── test_app.py             # Tests unitarios
├── models/
│   └── model.pkl               # Modelo entrenado
├── data/
│   └── Iris.csv                # Dataset
├── IaC/
│   ├── terraform/              # Scripts de Terraform
│   └── ansible/                # Playbooks de Ansible
├── Dockerfile                  # Configuración Docker
├── docker-compose.yml          # Docker Compose
├── requirements.txt            # Dependencias Python
└── README.md                   # Este archivo
```# Iris-RandomForest-Classifier

## Descripción

Este repositorio contiene un proyecto de aprendizaje automático que implementa un clasificador de Random Forest para el conjunto de datos Iris. El modelo de clasificación se entrena en las características de las flores Iris y es capaz de predecir la especie de una flor dadas sus características. El proyecto también incluye la implementación de un entorno Docker para ejecutar el modelo en un contenedor independiente.

## Características del Proyecto

Implementación de un modelo de Random Forest para clasificar flores Iris.

División de datos en conjuntos de entrenamiento y prueba.

Evaluación del modelo y generación de informes de clasificación y matriz de confusión.

Visualización de la precisión por clase y la importancia de las características.

Configuración de un entorno Docker para ejecutar el modelo en un contenedor independiente.

Este proyecto es una excelente demostración de cómo implementar un modelo de aprendizaje automático y empaquetarlo en un entorno Docker para facilitar su distribución y ejecución.

## Autor
Saúl Hernández Latiznere

## Fecha
8 de noviembre de 2023
