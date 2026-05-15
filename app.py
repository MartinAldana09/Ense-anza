import streamlit as st

st.set_page_config(
    page_title="Transformaciones Geométricas",
    layout="wide"
)

st.title("Transformaciones Geométricas")

st.markdown("""
## Plataforma interactiva de geometría

Esta aplicación permite:

- Visualizar transformaciones geométricas
- Trabajar con matrices
- Explorar figuras en el plano
- Resolver ejercicios
- Presentar evaluaciones

Use el menú lateral para navegar entre las secciones.
""")

st.divider()

st.subheader("Secciones")

st.write("Simulador")
st.write("Aprendizaje")
st.write("Examen")
