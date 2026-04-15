import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("Cartographie des Instituts et Réseaux au Sénégal")

# Cette ligne permet d'afficher ton fichier index.html que tu as généré
with open("index.html", 'r', encoding='utf-8') as f:
    html_data = f.read()
    components.html(html_data, height=700)