# Imagen base
FROM python:3.9-slim

# Configuración de entorno
ENV PYTHONUNBUFFERED=1

# Crear un directorio de trabajo
WORKDIR /app

# Instalar dependencias
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copiar requirements (si existen) e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar la aplicación al contenedor
COPY . .

# Crear un volumen para persistencia del token
VOLUME ["/app/data"]

# Exponer puertos de Flask y del otro servicio
EXPOSE 5000 8080

# Comando por defecto para iniciar la aplicación
CMD ["python", "app.py"]
