import streamlit as st

st.set_page_config(
    page_title="Examen Final",
    layout="wide"
)

# =====================================================
# ESTILOS
# =====================================================

st.markdown("""
<style>

.main-title{
    font-size:60px;
    font-weight:bold;
    text-align:center;
    color:#0D47A1;
}

.subtitle{
    font-size:30px;
    text-align:center;
    color:#1565C0;
}

.box{
    background-color:#E3F2FD;
    padding:30px;
    border-radius:20px;
    border:2px solid #64B5F6;
}

.info{
    background-color:#FFF3E0;
    padding:25px;
    border-radius:20px;
    border-left:10px solid orange;
}

.section{
    background-color:#F5F5F5;
    padding:20px;
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# PORTADA
# =====================================================

st.markdown(
    '<p class="main-title">Examen Final</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Transformaciones Geométricas</p>',
    unsafe_allow_html=True
)

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Cartesian-coordinate-system.svg/1200px-Cartesian-coordinate-system.svg.png",
    use_container_width=True
)

st.divider()

# =====================================================
# INTRODUCCIÓN
# =====================================================

st.markdown("""
<div class="box">

## Plataforma de evaluación interactiva

En este examen trabajará con:

- Traslaciones
- Rotaciones
- Reflexiones
- Homotecias
- Composición de transformaciones
- Interpretación geométrica
- Argumentación matemática

La plataforma está diseñada para que el estudiante:

- explore
- visualice
- compare
- experimente
- valide resultados

directamente en el simulador interactivo.

</div>
""", unsafe_allow_html=True)

st.divider()

# =====================================================
# INSTRUCCIONES IMPORTANTES
# =====================================================

st.markdown("""
<div class="info">

## Importante

Las preguntas del PDF que indiquen:

- "Use GeoGebra"
- "Grafique"
- "Observe la transformación"
- "Superponga figuras"
- "Use papel cuadriculado"

deben resolverse utilizando el:

# Simulador de Transformaciones

disponible en esta plataforma.

El simulador reemplaza:

- GeoGebra
- papel milimetrado
- construcciones manuales

</div>
""", unsafe_allow_html=True)

st.divider()

# =====================================================
# DESCARGAR PDF
# =====================================================

st.header("Descargar examen")

st.write("""
Presione el botón para descargar
el examen final en formato PDF.
""")

with open("archivos/examen_final.pdf", "rb") as pdf_file:

    PDFbyte = pdf_file.read()

st.download_button(
    label=" Descargar examen final",
    data=PDFbyte,
    file_name="Examen_Final_Transformaciones.pdf",
    mime="application/pdf"
)

st.divider()

# =====================================================
# RECOMENDACIONES
# =====================================================

st.markdown("""
<div class="section">

## Recomendaciones antes de iniciar

- Revise las fórmulas principales
- Verifique signos y coordenadas
- Indique correctamente:
    - sentido horario
    - sentido antihorario
- Revise el orden de las transformaciones
- Etiquete vértices
- Justifique procedimientos

Recuerde:

El orden de las transformaciones
puede cambiar completamente el resultado final.

</div>
""", unsafe_allow_html=True)

st.divider()

# =====================================================
# FINAL
# =====================================================

st.success("""
Cuando esté listo:

1. Descargue el PDF
2. Abra la pestaña 'Simulador'
3. Resuelva los ejercicios utilizando la plataforma
""")
