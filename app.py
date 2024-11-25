import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta del archivo persistente
TOKEN_FILE = './data/token.json'

# Verificar o inicializar el token
def get_or_initialize_token():
    if not os.path.exists(TOKEN_FILE):
        token = input("Por favor, introduzca el token de autenticación: ")
        with open(TOKEN_FILE, 'w') as f:
            json.dump({"token": token}, f)
    else:
        with open(TOKEN_FILE, 'r') as f:
            token_data = json.load(f)
            token = token_data.get("token")
            if not token:
                token = input("Por favor, introduzca el token de autenticación: ")
                with open(TOKEN_FILE, 'w') as f:
                    json.dump({"token": token}, f)
    return token

# Endpoint para verificar el token
@app.route('/token', methods=['GET'])
def get_token():
    try:
        with open(TOKEN_FILE, 'r') as f:
            token_data = json.load(f)
        return jsonify({"token": token_data.get("token")}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Inicializar el token al arrancar
@app.before_first_request
def initialize():
    get_or_initialize_token()

@app.route('/', methods=['GET'])
def home():
    return "API corriendo correctamente."

if __name__ == '__main__':
    # Inicia la aplicación Flask
    app.run(host='0.0.0.0', port=5000)
