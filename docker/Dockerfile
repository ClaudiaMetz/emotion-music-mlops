# 1. Imagen base liviana
FROM python:3.9-slim

# 2. Directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiamos el archivo de dependencias primero (Optimización de capas)
COPY requirements.txt .

# 4. Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos el resto del código del proyecto
COPY . .

# 6. Comando para ejecutar la aplicación al iniciar el contenedor
CMD ["python", "main.py"]