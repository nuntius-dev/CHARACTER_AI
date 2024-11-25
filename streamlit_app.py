import json
import os
import streamlit as st

# Ruta del archivo persistente
TOKEN_FILE = './data/token.json'

# Leer el token
def load_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as f:
            return json.load(f).get("token")
    return "Token no encontrado."

# Aplicación Streamlit
st.title("Interfaz de Administración")
st.write("Esta es una interfaz interactiva para administrar el token.")

token = load_token()
st.text_input("Token actual:", token, disabled=True)

if st.button("Actualizar token"):
    new_token = st.text_input("Ingrese un nuevo token:")
    if new_token:
        with open(TOKEN_FILE, 'w') as f:
            json.dump({"token": new_token}, f)
        st.success("Token actualizado correctamente.")
