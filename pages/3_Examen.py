import streamlit as st

st.title("Evaluación")

st.write("""
Esta evaluación mide:

- Interpretación
- Formulación
- Argumentación
""")

nombre = st.text_input("Nombre")

curso = st.text_input("Curso")

if st.button("Comenzar evaluación"):
    st.success("Evaluación iniciada")

st.divider()

st.header("Ejercicio 1")

st.write("""
Se tienen dos triángulos en el plano cartesiano.
""")

st.latex(r"A_1=\left(\frac12,\frac32\right)")
st.latex(r"A_2=\left(\frac72,\frac32\right)")
st.latex(r"A_3=\left(\frac12,\frac92\right)")

respuesta = st.text_area(
    "Explique qué relación observa entre los triángulos."
)

if st.button("Guardar respuesta"):
    st.success("Respuesta guardada")
