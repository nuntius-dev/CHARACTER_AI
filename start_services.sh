#!/bin/bash

# Iniciar el servidor Flask en segundo plano
python app.py &

# Iniciar el servidor Streamlit
streamlit run streamlit_app.py
