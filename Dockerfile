# Imagen base oficial de Python
FROM python:3.8-slim

# Metadata
LABEL maintainer="tu-email@example.com"
LABEL version="1.0.0"
LABEL description="Iris ML Classification API"

# Variables de entorno
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    MODEL_PATH=/app/models/model.pkl \
    FLASK_ENV=production

# Directorio de trabajo
WORKDIR /app

# Crear usuario no-root
RUN groupadd -r mluser && \
    useradd -r -g mluser -u 1000 mluser && \
    chown -R mluser:mluser /app

# Copiar requirements primero (cache layer)
COPY --chown=mluser:mluser requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache

# Copiar código de aplicación
COPY --chown=mluser:mluser src/ ./src/
COPY --chown=mluser:mluser models/ ./models/
COPY --chown=mluser:mluser data/ ./data/

# Cambiar a usuario no-root
USER mluser

# Exponer puerto
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health', timeout=5)"

# Comando de inicio
CMD ["python", "src/app.py"]
