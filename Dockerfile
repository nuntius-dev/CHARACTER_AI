# Imagen base
FROM python:3.9-slim

# Directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios
COPY requirements.txt /app/requirements.txt
COPY ia.py /app/ia.py

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer puerto de Flask
EXPOSE 5000

# Comando de inicio
CMD ["python", "ia.py"]
