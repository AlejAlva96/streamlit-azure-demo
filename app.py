import streamlit as st

st.set_page_config(page_title="Hola Azure + Streamlit", page_icon="💠", layout="centered")

st.title("Hola desde Azure Web App 👋")
st.write("Ejemplo mínimo en Azure App Service (Linux).")

nombre = st.text_input("¿Cómo te llamas?")
if nombre:
    st.success(f"¡Encantado, {nombre}!")