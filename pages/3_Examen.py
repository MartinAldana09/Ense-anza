import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import datetime

# =========================================================
# CONFIGURACIÓN
# =========================================================

st.set_page_config(
    page_title="Evaluación",
    layout="wide"
)

# =========================================================
# ESTILO
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

h1 {
    color: #003366;
    text-align: center;
}

h2, h3 {
    color: #004080;
}

.block-container {
    padding-top: 2rem;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    background-color: #003366;
    color: white;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TÍTULO
# =========================================================

st.title("Evaluación Interactiva: Transformaciones Geométricas")

st.write("""
Esta evaluación combina:

- interpretación geométrica
- análisis visual
- razonamiento matemático
- uso del simulador

Utilice el simulador para resolver
las preguntas donde sea necesario.
""")

st.divider()

# =========================================================
# DATOS ESTUDIANTE
# =========================================================

st.header("Información del estudiante")

col_d1, col_d2 = st.columns(2)

with col_d1:

    nombre = st.text_input("Nombre completo")

with col_d2:

    curso = st.text_input("Curso")

st.divider()

# =========================================================
# FUNCIÓN GRAFICAR
# =========================================================

def dibujar(P1, P2=None):

    fig, ax = plt.subplots(figsize=(8,8))

    P1_c = np.vstack([P1, P1[0]])

    ax.plot(
        P1_c[:,0],
        P1_c[:,1],
        linewidth=3,
        linestyle='--',
        label="Figura original"
    )

    ax.scatter(P1[:,0], P1[:,1], s=80)

    for i, p in enumerate(P1):

        ax.text(
            p[0],
            p[1],
            f"A{i+1}",
            fontsize=12
        )

    if P2 is not None:

        P2_c = np.vstack([P2, P2[0]])

        ax.plot(
            P2_c[:,0],
            P2_c[:,1],
            linewidth=3,
            label="Figura transformada"
        )

        ax.scatter(P2[:,0], P2[:,1], s=80)

        for i, p in enumerate(P2):

            ax.text(
                p[0],
                p[1],
                f"B{i+1}",
                fontsize=12
            )

    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.grid(True, linestyle='--', alpha=0.5)

    ax.set_xlim(-5, 12)
    ax.set_ylim(-5, 12)

    ax.set_aspect('equal')

    ax.legend()

    st.pyplot(fig)

# =========================================================
# FIGURAS
# =========================================================

A = np.array([
    [0.5, 1.5],
    [3.5, 1.5],
    [0.5, 4.5]
])

B = np.array([
    [3,1],
    [9,1],
    [3,7]
])

# =========================================================
# INTRODUCCIÓN
# =========================================================

st.header("Situación problema")

st.write("""
Un diseñador gráfico está utilizando transformaciones
geométricas para modificar figuras en el plano cartesiano.

Analice cuidadosamente las figuras y responda
las preguntas.
""")

dibujar(A, B)

# =========================================================
# PREGUNTAS
# =========================================================

puntaje = 0

# ---------------------------------------------------------

st.divider()

st.header("Pregunta 1")

st.write("""
¿Qué ocurrió con el tamaño del triángulo?
""")

r1 = st.radio(
    "Seleccione una opción",
    [
        "Disminuyó",
        "Conservó exactamente el mismo tamaño",
        "Aumentó",
        "Desapareció"
    ],
    key="r1"
)

# ---------------------------------------------------------

st.divider()

st.header("Pregunta 2")

st.write("""
¿Qué transformación mueve una figura
sin cambiar forma ni tamaño?
""")

r2 = st.radio(
    "Seleccione una opción",
    [
        "Rotación",
        "Traslación",
        "Homotecia",
        "Reflexión"
    ],
    key="r2"
)

# ---------------------------------------------------------

st.divider()

st.header("Pregunta 3")

st.write("""
Si un punto rota 90° antihorario
respecto al origen:

¿Qué ocurre?
""")

r3 = st.radio(
    "Seleccione una opción",
    [
        "La figura gira",
        "La figura desaparece",
        "La figura se refleja",
        "La figura cambia de tamaño"
    ],
    key="r3"
)

# ---------------------------------------------------------

st.divider()

st.header("Pregunta 4")

st.write("""
¿Qué produce una reflexión
respecto al eje X?
""")

r4 = st.radio(
    "Seleccione una opción",
    [
        "Un giro",
        "Una imagen especular",
        "Una traslación",
        "Una ampliación"
    ],
    key="r4"
)

# ---------------------------------------------------------

st.divider()

st.header("Pregunta 5")

st.write("""
En una homotecia con:

k = 2

¿Qué ocurre?
""")

r5 = st.radio(
    "Seleccione una opción",
    [
        "La figura gira",
        "La figura se reduce",
        "La figura duplica su tamaño",
        "La figura desaparece"
    ],
    key="r5"
)

# =========================================================
# SIMULADOR
# =========================================================

st.divider()

st.header("Exploración con simulador")

st.write("""
Use esta sección para intentar transformar
el triángulo original hasta hacerlo coincidir
con el triángulo destino.
""")

col1, col2, col3 = st.columns(3)

with col1:

    a = st.number_input(
        "Traslación X",
        value=0.0
    )

    b = st.number_input(
        "Traslación Y",
        value=0.0
    )

with col2:

    k = st.number_input(
        "Escala k",
        value=1.0
    )

with col3:

    theta = st.number_input(
        "Rotación θ",
        value=0.0
    )

# =========================================================
# TRANSFORMACIONES
# =========================================================

def escala(P, k):

    A_mat = k * np.eye(2)

    return P @ A_mat.T

# ---------------------------------------------------------

def rotacion(P, theta):

    t = np.radians(theta)

    A_mat = np.array([
        [np.cos(t), -np.sin(t)],
        [np.sin(t),  np.cos(t)]
    ])

    return P @ A_mat.T

# ---------------------------------------------------------

def traslacion(P, a, b):

    return P + np.array([a,b])

# =========================================================
# APLICAR
# =========================================================

P_new = A.copy()

P_new = escala(P_new, k)
P_new = rotacion(P_new, theta)
P_new = traslacion(P_new, a, b)

# =========================================================
# GRÁFICA
# =========================================================

fig, ax = plt.subplots(figsize=(9,9))

A_c = np.vstack([A, A[0]])
B_c = np.vstack([B, B[0]])
P_c = np.vstack([P_new, P_new[0]])

# ORIGINAL

ax.plot(
    A_c[:,0],
    A_c[:,1],
    linewidth=3,
    linestyle='--',
    label="Original"
)

# DESTINO

ax.plot(
    B_c[:,0],
    B_c[:,1],
    linewidth=3,
    label="Destino"
)

# ESTUDIANTE

ax.plot(
    P_c[:,0],
    P_c[:,1],
    linewidth=3,
    label="Tu transformación"
)

ax.scatter(P_new[:,0], P_new[:,1], s=80)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.grid(True, linestyle='--', alpha=0.5)

ax.set_xlim(-5, 12)
ax.set_ylim(-5, 12)

ax.set_aspect('equal')

ax.legend()

st.pyplot(fig)

# =========================================================
# VALIDACIÓN
# =========================================================

error = np.linalg.norm(P_new - B)

if error < 0.01:

    st.success("""
Excelente.

La transformación coincide correctamente.
""")

else:

    st.info("""
La figura todavía no coincide completamente.

Continúe experimentando con:

- traslación
- escala
- rotación
""")

# =========================================================
# MATRICES
# =========================================================

st.divider()

st.header("Representación matricial")

t = np.radians(theta)

A_mat = k * np.array([
    [np.cos(t), -np.sin(t)],
    [np.sin(t),  np.cos(t)]
])

b_vec = np.array([a,b])

st.write("Matriz A")

st.write(np.round(A_mat,3))

st.write("Vector b")

st.write(np.round(b_vec,3))

st.latex(r"T(x)=Ax+b")

# =========================================================
# REFLEXIÓN FINAL
# =========================================================

st.divider()

st.header("Pregunta final")

r_final = st.radio(
    "¿El orden de las transformaciones puede cambiar el resultado?",
    [
        "Sí",
        "No"
    ]
)

# =========================================================
# ENVIAR EVALUACIÓN
# =========================================================

st.divider()

if st.button("Enviar evaluación"):

    # -----------------------------------------------------
    # CALIFICAR
    # -----------------------------------------------------

    if r1 == "Aumentó":
        puntaje += 1

    if r2 == "Traslación":
        puntaje += 1

    if r3 == "La figura gira":
        puntaje += 1

    if r4 == "Una imagen especular":
        puntaje += 1

    if r5 == "La figura duplica su tamaño":
        puntaje += 1

    if r_final == "Sí":
        puntaje += 1

    # -----------------------------------------------------
    # CREAR REGISTRO
    # -----------------------------------------------------

    datos = {
        "Fecha": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "Nombre": [nombre],
        "Curso": [curso],
        "Pregunta 1": [r1],
        "Pregunta 2": [r2],
        "Pregunta 3": [r3],
        "Pregunta 4": [r4],
        "Pregunta 5": [r5],
        "Pregunta Final": [r_final],
        "Puntaje": [puntaje]
    }

    df_nuevo = pd.DataFrame(datos)

    archivo = "resultados.csv"

    # -----------------------------------------------------
    # GUARDAR CSV
    # -----------------------------------------------------

    if os.path.exists(archivo):

        df_existente = pd.read_csv(archivo)

        df_total = pd.concat(
            [df_existente, df_nuevo],
            ignore_index=True
        )

    else:

        df_total = df_nuevo

    df_total.to_csv(
        archivo,
        index=False
    )

    # -----------------------------------------------------
    # MENSAJE
    # -----------------------------------------------------

    st.success(f"""
Evaluación enviada correctamente.

Puntaje obtenido: {puntaje}/6
""")

    # -----------------------------------------------------
    # MOSTRAR TABLA
    # -----------------------------------------------------

    st.subheader("Resultados registrados")

    st.dataframe(df_total)

    # -----------------------------------------------------
    # DESCARGAR CSV
    # -----------------------------------------------------

    with open(archivo, "rb") as f:

        st.download_button(
            label="Descargar resultados CSV",
            data=f,
            file_name="resultados.csv",
            mime="text/csv"
        )
