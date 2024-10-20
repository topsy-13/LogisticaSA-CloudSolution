# Utiliza una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación
COPY requirements.txt requirements.txt
COPY main.py main.py

# Copiar los datos de la carpeta data_wrangling al contenedor
COPY data_wrangling/ ./data_wrangling/

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Ejecutar el script de conversión de parquet a SQLite antes de iniciar la API
RUN python3 main.py

# Exponer el puerto en el que correrá la API
EXPOSE 8000

# Comando para ejecutar la API cuando el contenedor inicie
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]