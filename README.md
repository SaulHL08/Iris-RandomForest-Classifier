# 🌸 Iris ML Classifier - DevOps Project

![CI Status](https://github.com/SaulHL08/Iris-RandomForest-Classifier/workflows/CI%20Pipeline/badge.svg)
![Docker](https://img.shields.io/docker/v/saulhl07/iris-ml-classifier?label=docker)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Sistema de clasificación de flores Iris usando Machine Learning (Random Forest) con CI/CD completo, containerización Docker y despliegue en AWS.

---

## 🚀 Quick Start

### Docker (Recomendado)
```bash
docker pull saulhl07/iris-ml-classifier:latest
docker run -p 5000:5000 saulhl07/iris-ml-classifier:latest
```

### Local
```bash
git clone https://github.com/SaulHL08/Iris-RandomForest-Classifier.git
cd Iris-RandomForest-Classifier
pip install -r requirements.txt
python src/train_model.py
python src/app.py
```

### Probar API
```bash
curl http://localhost:5000/health

curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"SepalLengthCm": 5.1, "SepalWidthCm": 3.5, "PetalLengthCm": 1.4, "PetalWidthCm": 0.2}'
```

---

## ✨ Características

- 🤖 **ML Model**: Random Forest Classifier (95% accuracy)
- 🚀 **API REST**: Flask con 4 endpoints
- 🐳 **Docker**: Imagen optimizada y publicada
- ☁️ **AWS**: Despliegue automatizado en EC2
- 🔧 **IaC**: Terraform + Ansible
- 🔄 **CI/CD**: GitHub Actions
- 🧪 **Testing**: pytest (91% cobertura)
- 🔒 **Seguridad**: Escaneo de vulnerabilidades, usuario no-root

---

## 🛠️ Tecnologías

**Backend & ML**  
Python 3.8+ • Flask 3.0 • scikit-learn 1.3 • Pandas • NumPy

**DevOps & Cloud**  
Docker • AWS EC2 • Terraform • Ansible • GitHub Actions

**Testing & Quality**  
pytest • flake8 • Coverage 91%

---

## 🌐 API Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Información del servicio |
| GET | `/health` | Health check |
| GET | `/info` | Información del modelo ML |
| POST | `/predict` | Realizar predicción |

### Ejemplo Predicción
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
  }
}
```

---

## 🏗️ Arquitectura
```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Usuario   │────▶│  API Flask   │────▶│  ML Model   │
│  (Cliente)  │◀────│  (Port 5000) │◀────│RandomForest │
└─────────────┘     └──────────────┘     └─────────────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  Docker      │
                    │  Container   │
                    └──────────────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  AWS EC2     │
                    │  Ubuntu      │
                    └──────────────┘
```

**Ver diagramas completos:** [docs/architecture.md](docs/architecture.md)

---

## ☁️ Despliegue en AWS

### Provisionar Infraestructura
```bash
cd IaC/terraform
terraform init
terraform apply

export EC2_IP=$(terraform output -raw instance_public_ip)
```

### Desplegar Aplicación
```bash
cd ../ansible

# Crear inventario con tu IP
cat > inventory.ini << EOF
[iris_ml_servers]
production ansible_host=$EC2_IP ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/iris-ml-key

[iris_ml_servers:vars]
ansible_python_interpreter=/usr/bin/python3
docker_image=saulhl07/iris-ml-classifier
docker_tag=latest
app_port=5000
EOF

# Desplegar
ansible all -m ping
ansible-playbook deploy.yml
```

### Acceder a la API
```bash
curl http://$EC2_IP:5000/health
```

### ⚠️ Destruir Recursos
```bash
cd IaC/terraform
terraform destroy  # Evita cargos en AWS
```

---

## 🧪 Testing
```bash
# Ejecutar tests
pytest tests/ -v

# Con cobertura
pytest tests/ --cov=src --cov-report=html

# Ver reporte
open htmlcov/index.html
```

**Cobertura actual: 91%**

---

## 🔄 CI/CD Pipeline

### GitHub Actions
Cada push ejecuta automáticamente:
1. ✅ Lint con flake8
2. ✅ Tests con pytest
3. ✅ Build Docker image
4. ✅ Escaneo de seguridad (Trivy)
5. ✅ Push a Docker Hub (en main)

**Ver pipelines:** [GitHub Actions](https://github.com/SaulHL08/Iris-RandomForest-Classifier/actions)

---

## 📁 Estructura del Proyecto
```
Iris-RandomForest-Classifier/
├── .github/workflows/      # CI/CD pipelines
├── IaC/
│   ├── terraform/          # Infraestructura AWS
│   └── ansible/            # Automatización despliegue
├── src/
│   ├── app.py             # API Flask
│   └── train_model.py     # Entrenamiento ML
├── tests/                 # Tests unitarios
├── models/                # Modelo entrenado
├── data/                  # Dataset Iris
├── docs/                  # Documentación
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## 🔒 Seguridad

- ✅ Contenedor con usuario no-root
- ✅ Validación estricta de entrada
- ✅ Escaneo de vulnerabilidades en CI
- ✅ Security Groups restrictivos (AWS)
- ✅ Secrets management (GitHub Secrets)
- ✅ Volúmenes EBS encriptados

---

## 📚 Documentación

- **[Arquitectura](docs/architecture.md)** - Diagramas y flujos
- **[Terraform Guide](IaC/terraform/README.md)** - IaC
- **[Ansible Guide](IaC/ansible/README.md)** - Automatización
- **[Checklist](CHECKLIST.md)** - Estado del proyecto
- **[Comandos](COMANDOS.txt)** - Referencia rápida

---

## 🌐 Enlaces

- **GitHub:** [github.com/SaulHL08/Iris-RandomForest-Classifier](https://github.com/SaulHL08/Iris-RandomForest-Classifier)
- **Docker Hub:** [hub.docker.com/r/saulhl07/iris-ml-classifier](https://hub.docker.com/r/saulhl07/iris-ml-classifier)
- **CI/CD:** [GitHub Actions](https://github.com/SaulHL08/Iris-RandomForest-Classifier/actions)

---

## 👨‍💻 Autor

**Saúl Hernández Latiznere**
