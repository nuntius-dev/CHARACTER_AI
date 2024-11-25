#!/bin/bash

# Variable para el token
TOKEN=${CHARACTER_AI_TOKEN}

# Verifica si el token ya está configurado
if [ ! -f "token.json" ]; then
  if [ -z "$TOKEN" ]; then
    echo "Error: El token no está configurado. Usa la variable de entorno CHARACTER_AI_TOKEN."
    exit 1
  fi

  # Crea archivo token.json
  echo "{\"token\": \"$TOKEN\"}" > token.json
  echo "Token configurado correctamente."
fi

# Inicia la aplicación Flask
python ia.py
