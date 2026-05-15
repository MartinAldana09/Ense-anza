import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import json

st.set_page_config(
    page_title="Simulador PRO",
    layout="wide"
)

# =========================================================
# ESTILOS
# =========================================================

st.markdown("""
<style>

.main-title{
    font-size:55px;
    font-weight:bold;
    text-align:center;
    color:#0D47A1;
}

.subtitle{
    font-size:25px;
    text-align:center;
    color:#1565C0;
}

.box{
    background-color:#E3F2FD;
    padding:20px;
    border-radius:20px;
    border:2px solid #64B5F6;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<p class="main-title">Simulador PRO</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Transformaciones Geométricas Interactivas</p>',
    unsafe_allow_html=True
)

st.divider()

# =========================================================
# FUNCIONES DE FIGURAS
# =========================================================

def triangulo():
    return np.array([
        [1,1],
        [4,1],
        [2,3]
    ], dtype=float)

def cuadrado():
    return np.array([
        [1,1],
        [3,1],
        [3,3],
        [1,3]
    ], dtype=float)

def pentagono():
    return np.array([
        [0,2],
        [2,4],
        [4,2],
        [3,0],
        [1,0]
    ], dtype=float)

def hexagono():
    return np.array([
        [1,0],
        [3,0],
        [4,2],
        [3,4],
        [1,4],
        [0,2]
    ], dtype=float)

# =========================================================
# CREAR FIGURA 1
# =========================================================

st.header("Figura principal")

tipo1 = st.selectbox(
    "Seleccione figura",
    [
        "Triángulo",
        "Cuadrado",
        "Pentágono",
        "Hexágono"
    ]
)

if tipo1 == "Triángulo":
    P = triangulo()

elif tipo1 == "Cuadrado":
    P = cuadrado()

elif tipo1 == "Pentágono":
    P = pentagono()

else:
    P = hexagono()

# =========================================================
# FIGURA SECUNDARIA
# =========================================================

st.header("Superposición de figuras")

usar_figura2 = st.checkbox(
    "Activar segunda figura"
)

if usar_figura2:

    tipo2 = st.selectbox(
        "Figura secundaria",
        [
            "Triángulo",
            "Cuadrado",
            "Pentágono",
            "Hexágono"
        ]
    )

    if tipo2 == "Triángulo":
        P2 = triangulo()

    elif tipo2 == "Cuadrado":
        P2 = cuadrado()

    elif tipo2 == "Pentágono":
        P2 = pentagono()

    else:
        P2 = hexagono()

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.header("Transformaciones")

a = st.sidebar.slider(
    "Traslación X",
    -10.0,
    10.0,
    0.0
)

b = st.sidebar.slider(
    "Traslación Y",
    -10.0,
    10.0,
    0.0
)

theta = st.sidebar.slider(
    "Rotación θ",
    -360.0,
    360.0,
    0.0
)

k = st.sidebar.slider(
    "Escala k",
    -5.0,
    5.0,
    1.0
)

# =========================================================
# CENTRO
# =========================================================

st.sidebar.subheader("Centro de rotación")

x0 = st.sidebar.number_input(
    "x₀",
    value=0.0
)

y0 = st.sidebar.number_input(
    "y₀",
    value=0.0
)

# =========================================================
# TRANSFORMACIONES ACTIVAS
# =========================================================

usar_tras = st.sidebar.checkbox(
    "Traslación",
    True
)

usar_rot = st.sidebar.checkbox(
    "Rotación"
)

usar_esc = st.sidebar.checkbox(
    "Homotecia"
)

usar_refx = st.sidebar.checkbox(
    "Reflexión eje X"
)

usar_refy = st.sidebar.checkbox(
    "Reflexión eje Y"
)

# =========================================================
# OPCIONES EXTRA
# =========================================================

st.sidebar.header("Opciones")

mostrar_vertices = st.sidebar.checkbox(
    "Mostrar vértices",
    True
)

mostrar_coordenadas = st.sidebar.checkbox(
    "Mostrar coordenadas",
    True
)

mostrar_rejilla = st.sidebar.checkbox(
    "Mostrar rejilla",
    True
)

# =========================================================
# FUNCIONES
# =========================================================

def traslacion(P, a, b):

    return P + np.array([a,b])

def rotacion(P, theta, x0, y0):

    t = np.radians(theta)

    A = np.array([
        [np.cos(t), -np.sin(t)],
        [np.sin(t),  np.cos(t)]
    ])

    centro = np.array([x0,y0])

    return (P - centro) @ A.T + centro

def escala(P, k):

    return k * P

def refx(P):

    A = np.array([
        [1,0],
        [0,-1]
    ])

    return P @ A.T

def refy(P):

    A = np.array([
        [-1,0],
        [0,1]
    ])

    return P @ A.T

# =========================================================
# APLICAR
# =========================================================

def aplicar_transformaciones(P):

    P_new = P.copy()

    if usar_esc:
        P_new = escala(P_new, k)

    if usar_rot:
        P_new = rotacion(
            P_new,
            theta,
            x0,
            y0
        )

    if usar_refx:
        P_new = refx(P_new)

    if usar_refy:
        P_new = refy(P_new)

    if usar_tras:
        P_new = traslacion(
            P_new,
            a,
            b
        )

    return P_new

# =========================================================
# TRANSFORMAR
# =========================================================

P_new = aplicar_transformaciones(P)

if usar_figura2:
    P2_new = aplicar_transformaciones(P2)

# =========================================================
# GRÁFICA
# =========================================================

fig, ax = plt.subplots(figsize=(9,9))

# ---------------------------------------------------------
# FIGURA ORIGINAL
# ---------------------------------------------------------

P_c = np.vstack([P, P[0]])

ax.plot(
    P_c[:,0],
    P_c[:,1],
    'k--',
    linewidth=2,
    label="Original"
)

# ---------------------------------------------------------
# FIGURA TRANSFORMADA
# ---------------------------------------------------------

P_new_c = np.vstack([P_new, P_new[0]])

ax.plot(
    P_new_c[:,0],
    P_new_c[:,1],
    'b-',
    linewidth=3,
    label="Transformada"
)

# =========================================================
# FIGURA SECUNDARIA
# =========================================================

if usar_figura2:

    P2_c = np.vstack([P2, P2[0]])

    ax.plot(
        P2_c[:,0],
        P2_c[:,1],
        'g--',
        linewidth=2,
        label="Figura 2"
    )

    P2_new_c = np.vstack([P2_new, P2_new[0]])

    ax.plot(
        P2_new_c[:,0],
        P2_new_c[:,1],
        'r-',
        linewidth=3,
        label="Figura 2 transformada"
    )

# =========================================================
# VÉRTICES
# =========================================================

if mostrar_vertices:

    ax.scatter(
        P[:,0],
        P[:,1],
        s=100,
        color='black'
    )

    ax.scatter(
        P_new[:,0],
        P_new[:,1],
        s=100,
        color='blue'
    )

# =========================================================
# COORDENADAS
# =========================================================

if mostrar_coordenadas:

    for i, p in enumerate(P):

        ax.text(
            p[0],
            p[1],
            f"A{i+1}{tuple(np.round(p,2))}",
            fontsize=9
        )

    for i, p in enumerate(P_new):

        ax.text(
            p[0],
            p[1],
            f"B{i+1}{tuple(np.round(p,2))}",
            fontsize=9
        )

# =========================================================
# CENTRO
# =========================================================

ax.scatter(
    [x0],
    [y0],
    color='red',
    s=150,
    label="Centro"
)

# =========================================================
# EJES
# =========================================================

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.set_xlim(-15,15)
ax.set_ylim(-15,15)

ax.set_aspect('equal')

ax.grid(
    mostrar_rejilla,
    linestyle='--',
    alpha=0.5
)

ax.legend()

st.pyplot(fig)

# =========================================================
# MEDIDAS
# =========================================================

st.header("Análisis geométrico")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Figura original")

    st.write("Cantidad de vértices:")
    st.write(len(P))

    st.write("Coordenadas:")
    st.write(P)

with col2:

    st.subheader("Figura transformada")

    st.write("Cantidad de vértices:")
    st.write(len(P_new))

    st.write("Coordenadas:")
    st.write(np.round(P_new,2))

# =========================================================
# MATRIZ DE ROTACIÓN
# =========================================================

if usar_rot:

    st.subheader("Matriz de rotación")

    t = np.radians(theta)

    A = np.array([
        [np.cos(t), -np.sin(t)],
        [np.sin(t),  np.cos(t)]
    ])

    st.write(np.round(A,3))

# =========================================================
# EXPLICACIÓN AUTOMÁTICA
# =========================================================

st.header("Interpretación automática")

texto = []

if usar_tras:
    texto.append(
        f"La figura fue trasladada ({a}, {b})."
    )

if usar_rot:
    texto.append(
        f"La figura fue rotada {theta}° alrededor de ({x0}, {y0})."
    )

if usar_esc:
    texto.append(
        f"La figura fue escalada con razón k={k}."
    )

if usar_refx:
    texto.append(
        "La figura fue reflejada respecto al eje X."
    )

if usar_refy:
    texto.append(
        "La figura fue reflejada respecto al eje Y."
    )

for t in texto:
    st.write("-", t)

# =========================================================
# EXPORTAR
# =========================================================

config = {
    "traslacion_x": a,
    "traslacion_y": b,
    "rotacion": theta,
    "escala": k,
    "centro_rotacion": [x0,y0]
}

st.download_button(
    "Descargar configuración",
    json.dumps(config, indent=4),
    "configuracion.json"
)
