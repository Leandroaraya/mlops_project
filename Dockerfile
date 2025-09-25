# Imagen base con Python
FROM python:3.12-slim

# Establecer directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos de requirements e instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos del proyecto al contenedor
COPY . .

# Exponer el puerto que usará Flask
EXPOSE 5000

# Comando para ejecutar la API
CMD ["python", "app.py"]
