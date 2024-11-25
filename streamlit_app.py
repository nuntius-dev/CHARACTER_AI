import streamlit as st
import requests

flask_api_url = 'http://localhost:5000/chat'

def get_answer_from_flask(character_id, message):
    try:
        response = requests.post(
            flask_api_url,
            json={"character_id": character_id, "message": message}
        )
        if response.status_code == 200:
            return response.json().get('text', 'Sin respuesta')
        else:
            return f"Error {response.status_code}: {response.json().get('error', 'Error desconocido')}"
    except Exception as e:
        return f"Error: {str(e)}"

st.title('Chat Interactivo con Flask')
st.write('Usa esta interfaz para interactuar con la API Flask.')

# Input de usuario
character_id = st.text_input('ID del Personaje:', 'eFF8HAxAEVRyZ8SQPNg5Mrl26EdecfekXyJ6NxZQJxM')
question = st.text_area('Escribe tu pregunta aquí:')

if st.button('Enviar'):
    answer = get_answer_from_flask(character_id, question)
    st.write(f"**Respuesta:** {answer}")
