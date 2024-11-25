# Imagen base
FROM python:3.10-slim

# Configuración de entorno
ENV PYTHONUNBUFFERED=1

# Crear un directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copiar los archivos de la aplicación
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

# Crear el directorio persistente para el token
RUN mkdir -p /app/data

# Exponer los puertos para Flask y Streamlit
EXPOSE 5000 8501

# Permitir que el script de inicio sea ejecutable
RUN chmod +x /app/start_services.sh

# Comando para ejecutar los servicios
CMD ["/app/start_services.sh"]
