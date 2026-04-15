import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide")
st.title("Cartographie des Instituts et Réseaux au Sénégal")

file_name = "index.html"

if os.path.exists(file_name):
    path = file_name
else:
    path = os.path.join("DV2", file_name)

try:
    with open(path, 'r', encoding='utf-8') as f:
        html_data = f.read()
        components.html(html_data, height=700, scrolling=True)
except FileNotFoundError:
    st.error(f"Erreur : Le fichier {file_name} est introuvable.")
