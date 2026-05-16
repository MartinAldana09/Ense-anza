import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# =========================================================
# CONFIGURACIÓN
# =========================================================

st.set_page_config(
    page_title="Aprendizaje",
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
    font-size: 42px;
}

h2 {
    color: #004080;
    border-left: 6px solid #004080;
    padding-left: 12px;
}

h3 {
    color: #003366;
}

.block-container {
    padding-top: 2rem;
}

section[data-testid="stSidebar"] {
    background-color: #eaf2ff;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    background-color: #003366;
    color: white;
    font-weight: bold;
    border: none;
    padding: 0.6rem;
}

.stButton>button:hover {
    background-color: #0055aa;
    color: white;
}

.info-box {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    border-left: 6px solid #003366;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# PORTADA
# =========================================================

st.title("Aprendizaje de Transformaciones Geométricas")

st.markdown("""
<div class="info-box">

Las transformaciones geométricas permiten mover, girar,
reflejar o cambiar el tamaño de figuras en el plano cartesiano.

En esta sección estudiará:

<ul>
<li>Traslaciones</li>
<li>Rotaciones</li>
<li>Reflexiones</li>
<li>Homotecias</li>
</ul>

Cada tema incluye:

<ul>
<li>Explicación intuitiva</li>
<li>Interpretación geométrica</li>
<li>Representación algebraica</li>
<li>Visualización gráfica</li>
<li>Ejercicios interactivos</li>
<li>Validación automática</li>
</ul>

</div>
""", unsafe_allow_html=True)

st.divider()

# =========================================================
# FUNCIÓN GRAFICAR
# =========================================================

def graficar(P, P2, titulo1, titulo2):

    fig, ax = plt.subplots(figsize=(8,8))

    P_c = np.vstack([P, P[0]])
    P2_c = np.vstack([P2, P2[0]])

    # -----------------------------------------------------

    ax.plot(
        P_c[:,0],
        P_c[:,1],
        linestyle='--',
        linewidth=3,
        label=titulo1
    )

    ax.plot(
        P2_c[:,0],
        P2_c[:,1],
        linewidth=3,
        label=titulo2
    )

    # -----------------------------------------------------

    ax.scatter(
        P[:,0],
        P[:,1],
        s=90
    )

    ax.scatter(
        P2[:,0],
        P2[:,1],
        s=90
    )

    # -----------------------------------------------------
    # NOMBRES
    # -----------------------------------------------------

    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i, p in enumerate(P):

        ax.text(
            p[0],
            p[1],
            letras[i],
            fontsize=13
        )

    for i, p in enumerate(P2):

        ax.text(
            p[0],
            p[1],
            letras[i] + "'",
            fontsize=13
        )

    # -----------------------------------------------------

    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # -----------------------------------------------------

    ax.grid(
        True,
        linestyle='--',
        alpha=0.5
    )

    ax.set_xlim(-8,8)
    ax.set_ylim(-8,8)

    ax.set_aspect('equal')

    ax.legend(fontsize=11)

    st.pyplot(fig)

# =========================================================
# FIGURA BASE
# =========================================================

P = np.array([
    [0,0],
    [2,0],
    [1,2]
], dtype=float)

# =========================================================
# TRASLACIÓN
# =========================================================

st.header("Traslación")

col1, col2 = st.columns([1.2,1])

with col1:

    st.write("""
Una traslación mueve todos los puntos
la misma distancia y en la misma dirección.

La figura:

- no gira
- no cambia de tamaño
- no cambia de forma

únicamente cambia de posición.
""")

    st.subheader("Representación algebraica")

    st.latex(r"(x,y)\rightarrow(x+a,y+b)")

    st.subheader("Interpretación")

    st.write("""
El vector de traslación determina:

- cuánto se mueve la figura horizontalmente
- cuánto se mueve verticalmente
""")

with col2:

    st.info("""
Ejemplo intuitivo:

Mover una silla dentro del salón.

La silla sigue siendo exactamente la misma,
solo cambia de ubicación.
""")

# ---------------------------------------------------------

a = 3
b = 2

P_tras = P + np.array([a,b])

graficar(
    P,
    P_tras,
    "Figura original",
    "Figura trasladada"
)

# ---------------------------------------------------------

st.subheader("Tabla de coordenadas")

tabla_tras = pd.DataFrame({
    "Original": [tuple(p) for p in P],
    "Transformada": [tuple(np.round(p,2)) for p in P_tras]
})

st.table(tabla_tras)

# ---------------------------------------------------------

st.subheader("Ejercicio")

st.write("""
Un dron se encuentra en el punto:

\[
(2,3)
\]

Luego realiza el siguiente movimiento:

- 5 unidades a la derecha
- 2 unidades hacia abajo

Escriba la respuesta exactamente en el formato:

( x , y )
""")

respuesta1 = st.text_input(
    "Ingrese su respuesta",
    key="tras"
)

if st.button("Verificar respuesta", key="btn_tras"):

    if respuesta1.replace(" ","") == "(7,1)":

        st.success("""
Respuesta correcta.

Cálculo realizado:

x = 2 + 5 = 7

y = 3 - 2 = 1
""")

    else:

        st.error("""
Respuesta incorrecta.

Recuerde:

- derecha suma en x
- abajo resta en y

Formato esperado:

(7,1)
""")

st.divider()

# =========================================================
# ROTACIÓN
# =========================================================

st.header("Rotación")

col1, col2 = st.columns([1.2,1])

with col1:

    st.write("""
Una rotación gira una figura
alrededor de un punto fijo.

Ese punto recibe el nombre de:

centro de rotación.
""")

    st.subheader("Representación algebraica")

    :contentReference[oaicite:0]{index=0}

with col2:

    st.info("""
Ejemplos cotidianos:

- las aspas de un ventilador
- las manecillas de un reloj
- una puerta al abrirse
""")

# ---------------------------------------------------------

theta = 90

t = np.radians(theta)

A = np.array([
    [np.cos(t), -np.sin(t)],
    [np.sin(t),  np.cos(t)]
])

P_rot = P @ A.T

graficar(
    P,
    P_rot,
    "Figura original",
    "Figura rotada"
)

# ---------------------------------------------------------

st.subheader("Interpretación geométrica")

st.write("""
La figura se rotó:

- 90° antihorario
- alrededor del origen

En una rotación de 90° antihorario:

\[
(x,y)\rightarrow(-y,x)
\]
""")

# ---------------------------------------------------------

st.subheader("Ejercicio")

st.write("""
El punto:

\[
(2,0)
\]

se rota 90° antihorario alrededor del origen.

Ingrese la respuesta usando el formato:

(x,y)
""")

respuesta2 = st.text_input(
    "Ingrese su respuesta",
    key="rot"
)

if st.button("Verificar respuesta", key="btn_rot"):

    if respuesta2.replace(" ","") == "(0,2)":

        st.success("""
Respuesta correcta.

Aplicando:

(x,y) → (-y,x)

se obtiene:

(2,0) → (0,2)
""")

    else:

        st.error("""
Respuesta incorrecta.

Observe el sentido antihorario
de la rotación.
""")

st.divider()

# =========================================================
# REFLEXIÓN
# =========================================================

st.header("Reflexión")

col1, col2 = st.columns([1.2,1])

with col1:

    st.write("""
Una reflexión produce
una imagen especular.

La figura queda invertida
respecto a una recta.
""")

    st.subheader("Reflexión respecto al eje X")

    :contentReference[oaicite:1]{index=1}

with col2:

    st.info("""
Ejemplo intuitivo:

Cuando una persona se mira
en un espejo.
""")

# ---------------------------------------------------------

A_refx = np.array([
    [1,0],
    [0,-1]
])

P_ref = P @ A_refx.T

graficar(
    P,
    P_ref,
    "Figura original",
    "Figura reflejada"
)

# ---------------------------------------------------------

st.subheader("Interpretación geométrica")

st.write("""
En una reflexión respecto al eje X:

- las coordenadas x permanecen iguales
- las coordenadas y cambian de signo
""")

# ---------------------------------------------------------

st.subheader("Ejercicio")

st.write("""
Refleje el punto:

\[
(4,-3)
\]

respecto al eje X.

Ingrese la respuesta en formato:

(x,y)
""")

respuesta3 = st.text_input(
    "Ingrese su respuesta",
    key="ref"
)

if st.button("Verificar respuesta", key="btn_ref"):

    if respuesta3.replace(" ","") == "(4,3)":

        st.success("""
Respuesta correcta.

La coordenada x permanece igual
y la coordenada y cambia de signo.
""")

    else:

        st.error("""
Respuesta incorrecta.

Observe cuál coordenada
debe cambiar de signo.
""")

st.divider()

# =========================================================
# HOMOTECIA
# =========================================================

st.header("Homotecia")

col1, col2 = st.columns([1.2,1])

with col1:

    st.write("""
Una homotecia cambia
el tamaño de una figura.

Puede:

- ampliar
- reducir

manteniendo la forma geométrica.
""")

    st.subheader("Representación algebraica")

    :contentReference[oaicite:2]{index=2}

with col2:

    st.info("""
Ejemplo intuitivo:

Ampliar o reducir una imagen
en el celular.
""")

# ---------------------------------------------------------

k = 2

P_hom = k * P

graficar(
    P,
    P_hom,
    "Figura original",
    "Homotecia"
)

# ---------------------------------------------------------

st.subheader("Interpretación geométrica")

st.write("""
La figura aumentó su tamaño
al doble.

Todas las distancias
se multiplicaron por:

\[
k=2
\]
""")

# ---------------------------------------------------------

st.subheader("Ejercicio")

st.write("""
Aplique una homotecia de razón:

\[
k=3
\]

al punto:

\[
(2,1)
\]

Ingrese la respuesta usando el formato:

(x,y)
""")

respuesta4 = st.text_input(
    "Ingrese su respuesta",
    key="hom"
)

if st.button("Verificar respuesta", key="btn_hom"):

    if respuesta4.replace(" ","") == "(6,3)":

        st.success("""
Respuesta correcta.

Aplicando:

(x,y) → (kx,ky)

se obtiene:

(2,1) → (6,3)
""")

    else:

        st.error("""
Respuesta incorrecta.

Multiplique ambas coordenadas
por k.
""")

st.divider()

# =========================================================
# COMPARACIÓN
# =========================================================

st.header("Comparación de transformaciones")

tabla = pd.DataFrame({
    "Transformación": [
        "Traslación",
        "Rotación",
        "Reflexión",
        "Homotecia"
    ],
    "Cambia posición": [
        "Sí",
        "Sí",
        "Sí",
        "Sí"
    ],
    "Cambia orientación": [
        "No",
        "Sí",
        "Sí",
        "No"
    ],
    "Cambia tamaño": [
        "No",
        "No",
        "No",
        "Sí"
    ]
})

st.table(tabla)

st.divider()

# =========================================================
# RETO FINAL
# =========================================================

st.header("Reto final")

st.write("""
Considere el triángulo:

A=(0,0)

B=(2,0)

C=(1,2)

Analice qué ocurre si:

1. primero refleja la figura
2. luego la traslada

¿El orden de las transformaciones
puede modificar el resultado final?
""")

respuesta_final = st.text_input(
    "Escriba su conclusión",
    key="reto"
)

if st.button("Verificar análisis", key="btn_reto"):

    texto = respuesta_final.lower()

    if "sí" in texto or "si" in texto:

        st.success("""
Correcto.

El orden de las transformaciones
puede modificar:

- la posición final
- la orientación
- el resultado geométrico
""")

    else:

        st.error("""
Revise nuevamente la composición
de transformaciones geométricas.
""")

st.divider()

# =========================================================
# CONCLUSIÓN
# =========================================================

st.header("Conclusión")

st.markdown("""
<div class="info-box">

Las transformaciones geométricas son fundamentales en:

<ul>
<li>Matemáticas</li>
<li>Física</li>
<li>Ingeniería</li>
<li>Arquitectura</li>
<li>Diseño gráfico</li>
<li>Videojuegos</li>
<li>Animación</li>
</ul>

Comprenderlas permite analizar
cómo cambian las figuras
en el plano cartesiano y cómo
pueden modelarse fenómenos reales
mediante geometría.

</div>
""", unsafe_allow_html=True)
