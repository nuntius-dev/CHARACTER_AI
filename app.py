import asyncio
import os
import json
from flask import Flask, request, jsonify
from pycharacterai import Client  # Asegúrate de que la clase se llama con mayúscula

app = Flask(__name__)

# Ruta del archivo persistente para el token
token_file = './data/token.json'

# Obtener o inicializar el token
def get_or_initialize_token():
    # Crear directorio si no existe
    os.makedirs(os.path.dirname(token_file), exist_ok=True)  # 'true' a 'True'

    if not os.path.exists(token_file):
        # Solicitar el token si no existe
        token = input("Por favor, introduce tu token de Character AI: ").strip()
        with open(token_file, 'w') as f:
            json.dump({"token": token}, f)
    else:
        # Leer el token desde el archivo
        with open(token_file, 'r') as f:
            token_data = json.load(f)
            token = token_data.get("token")
            if not token:  # Si el archivo está vacío o inválido
                token = input("Por favor, introduce tu token de Character AI: ").strip()
                with open(token_file, 'w') as f:
                    json.dump({"token": token}, f)
    return token

# Función para autenticar el cliente
async def authenticate_client():
    client = Client()  # Asegúrate de que la clase se llama con mayúscula
    token = get_or_initialize_token()
    try:
        await client.authenticate_with_token(token)  # Esto debería ser await en un contexto async
    except Exception as e:
        print(f"Error autenticando el cliente: {str(e)}")
        return None
    return client

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json(force=True)
        if not data:
            return jsonify({"error": "Invalid JSON"}), 400

        character_id = data.get('character_id')
        message = data.get('message')

        if not character_id or not message:
            return jsonify({"error": "character_id and message are required"}), 400

        client = authenticate_client()
        chat = asyncio.run(client.create_or_continue_chat(character_id))
        answer = asyncio.run(chat.send_message(message))

        if answer is None:
            return jsonify({"error": "No response from chat"}), 500

        return jsonify({
            'name': answer.src_character_name,
            'text': answer.text
        })
    except Exception as e:
        # Cambié 'exception' a 'Exception' e imprime el error para mayor visibilidad
        print(f"Error en el endpoint /chat: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # 'true' a 'True'
