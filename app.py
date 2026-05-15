import streamlit as st

st.set_page_config(
    page_title="Transformaciones Geométricas",
    layout="wide"
)

# =========================================================
# PORTADA
# =========================================================

st.markdown("""
# Transformaciones Geométricas Interactivas
""")

st.markdown("""
### Exploración visual del plano cartesiano
""")

st.write("""
Esta plataforma permite aprender, experimentar y analizar
transformaciones geométricas de manera visual e interactiva.

Aquí podrá:

- visualizar figuras en el plano cartesiano
- aplicar transformaciones en tiempo real
- explorar matrices de transformación
- analizar composiciones geométricas
- resolver ejercicios interactivos
- desarrollar argumentación matemática
""")

st.divider()

# =========================================================
# BLOQUES VISUALES
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown("""
    ## Traslación
    
    Desplaza figuras
    sin cambiar:
    
    - tamaño
    - forma
    - orientación
    """)

with col2:

    st.markdown("""
    ## Rotación
    
    Gira figuras
    alrededor de:
    
    - un punto
    - un centro
    - un ángulo
    """)

with col3:

    st.markdown("""
    ## Reflexión
    
    Produce imágenes
    especulares respecto:
    
    - eje X
    - eje Y
    - rectas
    """)

with col4:

    st.markdown("""
    ## Homotecia
    
    Modifica:
    
    - tamaño
    - escala
    - proporciones
    """)

st.divider()

# =========================================================
# SECCIONES
# =========================================================

st.header("Módulos de la Plataforma")

col5, col6, col7 = st.columns(3)

with col5:

    st.subheader("Simulador")

    st.write("""
    Experimente libremente
    con transformaciones.

    Puede:

    - crear figuras
    - moverlas
    - rotarlas
    - reflejarlas
    - escalarlas
    """)

with col6:

    st.subheader("Aprendizaje")

    st.write("""
    Estudie conceptos mediante:

    - explicaciones intuitivas
    - gráficos dinámicos
    - ejercicios interactivos
    - interpretación geométrica
    """)

with col7:

    st.subheader("Evaluación")

    st.write("""
    Resuelva problemas usando:

    - el simulador
    - superposición de figuras
    - análisis geométrico
    - argumentación matemática
    """)

st.divider()

# =========================================================
# IMPORTANCIA
# =========================================================

st.header("¿Por qué estudiar transformaciones geométricas?")

st.write("""
Las transformaciones geométricas son fundamentales en:

- matemáticas
- física
- arquitectura
- ingeniería
- videojuegos
- animación
- diseño gráfico
- modelación matemática
""")

st.info("""
Utilice el menú lateral para navegar entre las diferentes secciones.
""")
