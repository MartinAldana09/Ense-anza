import streamlit as st

st.set_page_config(
    page_title="Transformaciones Geométricas",
    layout="wide"
)

# =========================================================
# ESTILOS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

h1 {
    color: #0b3d91;
    text-align: center;
    font-size: 55px;
}

h2 {
    color: #1248a4;
}

h3 {
    color: #1f5fbf;
}

.bloque {
    background-color: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.azul {
    background: linear-gradient(135deg, #dbeafe, #bfdbfe);
    padding: 25px;
    border-radius: 20px;
}

.verde {
    background: linear-gradient(135deg, #dcfce7, #bbf7d0);
    padding: 25px;
    border-radius: 20px;
}

.rojo {
    background: linear-gradient(135deg, #fee2e2, #fecaca);
    padding: 25px;
    border-radius: 20px;
}

.morado {
    background: linear-gradient(135deg, #ede9fe, #ddd6fe);
    padding: 25px;
    border-radius: 20px;
}

.titulo-central {
    text-align: center;
    font-size: 24px;
    color: #1e3a8a;
    font-weight: bold;
}

.texto-central {
    text-align: center;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# PORTADA
# =========================================================

st.markdown("""
<h1>
Transformaciones Geométricas Interactivas
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<div class="azul">

<div class="titulo-central">
Exploración visual del plano cartesiano
</div>

<br>

<div class="texto-central">

Aprenda geometría de manera interactiva mediante:

• simulaciones dinámicas  
• visualización gráfica  
• transformaciones en tiempo real  
• interpretación geométrica  
• ejercicios interactivos  
• análisis matemático  

</div>

</div>
""", unsafe_allow_html=True)

st.write("")

# =========================================================
# TARJETAS
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown("""
    <div class="verde">

    <h3 style="text-align:center;">
    Traslación
    </h3>

    <p style="text-align:center;">

    Desplaza figuras  
    sin cambiar:

    • forma  
    • tamaño  
    • orientación

    </p>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="rojo">

    <h3 style="text-align:center;">
    Rotación
    </h3>

    <p style="text-align:center;">

    Gira figuras  
    alrededor de:

    • un punto  
    • un centro  
    • un ángulo

    </p>

    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="morado">

    <h3 style="text-align:center;">
    Reflexión
    </h3>

    <p style="text-align:center;">

    Construye imágenes  
    especulares respecto:

    • eje X  
    • eje Y  
    • rectas

    </p>

    </div>
    """, unsafe_allow_html=True)

with col4:

    st.markdown("""
    <div class="azul">

    <h3 style="text-align:center;">
    Homotecia
    </h3>

    <p style="text-align:center;">

    Modifica:

    • tamaño  
    • escala  
    • proporciones

    </p>

    </div>
    """, unsafe_allow_html=True)

st.write("")

# =========================================================
# SECCIONES
# =========================================================

st.markdown("""
<div class="bloque">

<h2 style="text-align:center;">
Módulos de la Plataforma
</h2>

</div>
""", unsafe_allow_html=True)

col5, col6, col7 = st.columns(3)

with col5:

    st.markdown("""
    <div class="verde">

    <h3 style="text-align:center;">
    Simulador
    </h3>

    <p>

    Experimente libremente:

    • crear figuras  
    • trasladar  
    • rotar  
    • reflejar  
    • escalar  
    • superponer figuras

    </p>

    </div>
    """, unsafe_allow_html=True)

with col6:

    st.markdown("""
    <div class="azul">

    <h3 style="text-align:center;">
    Aprendizaje
    </h3>

    <p>

    Estudie mediante:

    • explicaciones intuitivas  
    • ejemplos visuales  
    • ejercicios interactivos  
    • interpretación geométrica

    </p>

    </div>
    """, unsafe_allow_html=True)

with col7:

    st.markdown("""
    <div class="rojo">

    <h3 style="text-align:center;">
    Evaluación
    </h3>

    <p>

    Resuelva problemas usando:

    • el simulador  
    • análisis geométrico  
    • argumentación matemática  
    • validación visual

    </p>

    </div>
    """, unsafe_allow_html=True)

st.write("")

# =========================================================
# IMPORTANCIA
# =========================================================

st.markdown("""
<div class="bloque">

<h2 style="text-align:center;">
Aplicaciones de las Transformaciones
</h2>

<p style="font-size:18px;">

Las transformaciones geométricas son fundamentales en:

• matemáticas  
• física  
• ingeniería  
• arquitectura  
• videojuegos  
• diseño gráfico  
• animación  
• modelación matemática  

</p>

</div>
""", unsafe_allow_html=True)

# =========================================================
# MENSAJE FINAL
# =========================================================

st.success("""
Utilice el menú lateral para navegar entre:

• Simulador
• Aprendizaje
• Evaluación
""")
