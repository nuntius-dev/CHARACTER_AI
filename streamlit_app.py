import asyncio
from flask import Flask, request, jsonify
from PyCharacterAI import Client

app = Flask(__name__)

token = 'su token'  # Reemplaza con tu token de Character AI

def authenticate_client():
    client = Client()
    asyncio.run(client.authenticate_with_token(token))
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

        return jsonify({
            'name': answer.src_character_name,
            'text': answer.text
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
