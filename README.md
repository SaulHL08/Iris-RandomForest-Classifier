# 🌸 Iris ML Classifier - DevOps Project

![CI Status](https://github.com/SaulHL08/Iris-RandomForest-Classifier/workflows/CI%20Pipeline/badge.svg)
![Docker](https://img.shields.io/docker/v/saulhl07/iris-ml-classifier?label=docker)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Sistema completo de clasificación de flores Iris usando Machine Learning con Random Forest, containerización con Docker y despliegue automatizado en AWS usando prácticas DevOps modernas.

---

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Arquitectura](#-arquitectura)
- [Demo en Vivo](#-demo-en-vivo)
- [Tecnologías](#-tecnologías)
- [Instalación Local](#-instalación-local)
- [Uso con Docker](#-uso-con-docker)
- [Despliegue en AWS](#-despliegue-en-aws)
- [API Endpoints](#-api-endpoints)
- [Testing](#-testing)
- [CI/CD Pipeline](#-cicd-pipeline)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Seguridad](#-seguridad)
- [Documentación](#-documentación)
- [Autor](#-autor)

---

## ✨ Características

- 🤖 **Machine Learning**: Modelo Random Forest entrenado con 95% de precisión
- 🚀 **API REST**: Endpoints Flask para predicciones en tiempo real
- 🐳 **Docker**: Containerización completa para portabilidad
- ☁️ **AWS**: Infraestructura en la nube con EC2
- 🔧 **IaC**: Terraform para gestión de infraestructura
- ⚙️ **Automation**: Ansible para configuración y despliegue
- 🔄 **CI/CD**: GitHub Actions para integración y despliegue continuo
- 🧪 **Testing**: Suite completa de tests con pytest (91% cobertura)
- 🔒 **Seguridad**: Contenedores con usuario no-root, secrets management
- 📊 **Monitoring**: Health checks y logging

---

## 🏗️ Arquitectura

![Arquitectura](docs/architecture.md)

### Componentes Principales:
```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Usuario   │────▶│  API Flask   │────▶│  ML Model   │
│  (Cliente)  │◀────│   (Port:5000)│◀────│ Random Forest│
└─────────────┘     └──────────────┘     └─────────────┘
                           │
                           ▼
                    ┌──────────────┐
                    │ AWS EC2      │
                    │ Ubuntu 22.04 │
                    └──────────────┘
```

**[Ver diagrama completo](docs/architecture.md)**

---

## 🌐 Demo en Vivo

**Imagen Docker Pública:**
```bash
docker pull saulhl07/iris-ml-classifier:latest
```

**Docker Hub:**
[https://hub.docker.com/r/saulhl07/iris-ml-classifier](https://hub.docker.com/r/saulhl07/iris-ml-classifier)

**Repositorio GitHub:**
[https://github.com/SaulHL08/Iris-RandomForest-Classifier](https://github.com/SaulHL08/Iris-RandomForest-Classifier)

---

## 🛠️ Tecnologías

### Backend & ML
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.0-000000?logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.0-F7931E?logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0.0-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.24.0-013243?logo=numpy&logoColor=white)

### DevOps & Cloud
![Docker](https://img.shields.io/badge/Docker-20.10+-2496ED?logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-EC2-FF9900?logo=amazon-aws&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-1.6+-7B42BC?logo=terraform&logoColor=white)
![Ansible](https://img.shields.io/badge/Ansible-2.9+-EE0000?logo=ansible&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-2088FF?logo=github-actions&logoColor=white)

### Testing & Quality
![pytest](https://img.shields.io/badge/pytest-7.4.0-0A9EDC?logo=pytest&logoColor=white)
![flake8](https://img.shields.io/badge/flake8-6.0.0-blue)
![Coverage](https://img.shields.io/badge/coverage-91%25-brightgreen)

---

## 📦 Instalación Local

### Prerrequisitos
- Python 3.8+
- pip
- virtualenv (opcional)

### Pasos
```bash
# 1. Clonar repositorio
git clone https://github.com/SaulHL08/Iris-RandomForest-Classifier.git
cd Iris-RandomForest-Classifier

# 2. Crear entorno virtual (opcional pero recomendado)
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Entrenar modelo (si no existe)
python src/train_model.py

# 5. Ejecutar API
python src/app.py
```

La API estará disponible en: `http://localhost:5000`

---

## 🐳 Uso con Docker

### Opción 1: Imagen desde Docker Hub (Recomendado)
```bash
# Descargar y ejecutar
docker run -d -p 5000:5000 --name iris-ml-api saulhl07/iris-ml-classifier:latest

# Ver logs
docker logs -f iris-ml-api

# Detener
docker stop iris-ml-api
docker rm iris-ml-api
```

### Opción 2: Construir localmente
```bash
# Construir imagen
docker build -t iris-ml-classifier .

# Ejecutar
docker run -d -p 5000:5000 --name iris-ml-api iris-ml-classifier

# O usar docker-compose
docker-compose up -d
```

### Verificar funcionamiento
```bash
# Health check
curl http://localhost:5000/health

# Obtener info del modelo
curl http://localhost:5000/info

# Realizar predicción
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "SepalLengthCm": 5.1,
    "SepalWidthCm": 3.5,
    "PetalLengthCm": 1.4,
    "PetalWidthCm": 0.2
  }'
```

---

## ☁️ Despliegue en AWS

### Prerrequisitos
- Cuenta AWS (Free Tier)
- AWS CLI configurado
- Terraform >= 1.6
- Ansible >= 2.9
- SSH key generado

### Paso 1: Provisionar Infraestructura con Terraform
```bash
cd IaC/terraform

# Inicializar Terraform
terraform init

# Ver plan
terraform plan

# Aplicar (crear recursos)
terraform apply

# Guardar IP pública
export EC2_IP=$(terraform output -raw instance_public_ip)
echo $EC2_IP
```

### Paso 2: Desplegar Aplicación con Ansible
```bash
cd ../ansible

# Crear inventario con la IP real
cat > inventory.ini << EOF
[iris_ml_servers]
production ansible_host=$EC2_IP ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/iris-ml-key

[iris_ml_servers:vars]
ansible_python_interpreter=/usr/bin/python3
docker_image=saulhl07/iris-ml-classifier
docker_tag=latest
app_port=5000
