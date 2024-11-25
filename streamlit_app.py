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
            return response.json().get('text')
        else:
            error_message = response.json().get('error') if response.content else "No response content"
            return f"error: {response.status_code} - {error_message}"
    except Exception as e:
        return f"error: {str(e)}"

st.header('ChatGPT Gratis GUI via Flask')

# Input de usuario para Character ID y mensaje
character_id = st.text_input('Character ID:', 'eFF8HAxAEVRyZ8SQPNg5Mrl26EdecfekXyJ6NxZQJxM')
question = st.text_area('Pregunta lo que quieras:')

if st.button('Preguntar'):
    answer = get_answer_from_flask(character_id, question)
    st.markdown(f"**Respuesta:** {answer}")
