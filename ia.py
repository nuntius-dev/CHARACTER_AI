import os
import json
import asyncio
from flask import Flask, request, jsonify

from PyCharacterAI import Client

app = Flask(__name__)

# Ruta para almacenar el token
TOKEN_FILE = "token.json"

# Función para cargar el token desde el archivo
def load_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as file:
            data = json.load(file)
            return data.get("token")
    return None

# Función para guardar el token en el archivo
def save_token(token):
    with open(TOKEN_FILE, "w") as file:
        json.dump({"token": token}, file)

# Endpoint para configurar el token
@app.route('/admin/set_token', methods=['POST'])
def set_token():
    data = request.get_json()
    token = data.get("token")
    if not token:
        return jsonify({"error": "Token is required"}), 400
    save_token(token)
    return jsonify({"message": "Token saved successfully"}), 200

# Endpoint para el chat
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

        token = load_token()
        if not token:
            return jsonify({"error": "Token not configured"}), 500

        client = Client()
        asyncio.run(client.authenticate_with_token(token))
        chat = asyncio.run(client.create_or_continue_chat(character_id))
        answer = asyncio.run(chat.send_message(message))

        return jsonify({
            'name': answer.src_character_name,
            'text': answer.text
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
