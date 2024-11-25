#!/bin/bash

# Iniciar Flask en segundo plano
python app.py &

# Iniciar Streamlit en segundo plano
streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0
