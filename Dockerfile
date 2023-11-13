# Usa una imagen base de Python
FROM python:3.8

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos del repositorio al contenedor
COPY . /app

# Instala las dependencias (si es necesario)
RUN pip install -r requirements.txt

# Instala Jupyter Notebook
RUN pip install jupyter

# Comando para ejecutar el servidor de Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]

