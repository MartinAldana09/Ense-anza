import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import json

# =========================================================
# CONFIGURACIÓN
# =========================================================

st.set_page_config(
    page_title="Simulador PRO",
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

section[data-testid="stSidebar"] {
    background-color: #eaf2ff;
}

.stButton>button {
    width: 100%;
    border-radius: 12px;
    background-color: #003366;
    color: white;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TÍTULO
# =========================================================

st.title("Simulador PRO de Transformaciones Geométricas")

st.markdown("""
### Plataforma interactiva estilo GeoGebra

Con este simulador puede:

✅ Graficar múltiples figuras  
✅ Aplicar transformaciones geométricas  
✅ Superponer figuras  
✅ Visualizar coordenadas  
✅ Ver matrices de transformación  
✅ Trabajar como en GeoGebra  
✅ Analizar composiciones de transformaciones  
""")

st.divider()

# =========================================================
# FUNCIONES FIGURAS
# =========================================================

def triangulo():
    return np.array([
        [1,1],
        [4,1],
        [2.5,4]
    ], dtype=float)

def cuadrado():
    return np.array([
        [1,1],
        [4,1],
        [4,4],
        [1,4]
    ], dtype=float)

def rectangulo():
    return np.array([
        [0,0],
        [5,0],
        [5,2],
        [0,2]
    ], dtype=float)

def pentagono():
    return np.array([
        [0,2],
        [2,4],
        [4,3],
        [3,0],
        [1,0]
    ], dtype=float)

# =========================================================
# CREAR FIGURA
# =========================================================

st.sidebar.header("Figura principal")

tipo1 = st.sidebar.selectbox(
    "Seleccione figura",
    [
        "Triángulo",
        "Cuadrado",
        "Rectángulo",
        "Pentágono"
    ]
)

if tipo1 == "Triángulo":
    P = triangulo()

elif tipo1 == "Cuadrado":
    P = cuadrado()

elif tipo1 == "Rectángulo":
    P = rectangulo()

else:
    P = pentagono()

# =========================================================
# SEGUNDA FIGURA
# =========================================================

usar_segunda = st.sidebar.checkbox(
    "Agregar segunda figura"
)

P2 = None

if usar_segunda:

    st.sidebar.subheader("Segunda figura")

    tipo2 = st.sidebar.selectbox(
        "Seleccione segunda figura",
        [
            "Triángulo",
            "Cuadrado",
            "Rectángulo",
            "Pentágono"
        ]
    )

    if tipo2 == "Triángulo":
        P2 = triangulo() + np.array([6,0])

    elif tipo2 == "Cuadrado":
        P2 = cuadrado() + np.array([6,0])

    elif tipo2 == "Rectángulo":
        P2 = rectangulo() + np.array([6,0])

    else:
        P2 = pentagono() + np.array([6,0])

# =========================================================
# PARÁMETROS
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
    -360,
    360,
    0
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

st.sidebar.header("Centro de transformación")

x0 = st.sidebar.number_input(
    "Centro X",
    value=0.0
)

y0 = st.sidebar.number_input(
    "Centro Y",
    value=0.0
)

# =========================================================
# OPCIONES
# =========================================================

st.sidebar.header("Opciones")

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

mostrar_vertices = st.sidebar.checkbox(
    "Mostrar vértices",
    True
)

mostrar_nombres = st.sidebar.checkbox(
    "Mostrar nombres",
    True
)

# =========================================================
# FUNCIONES
# =========================================================

def trasladar(P, a, b):
    return P + np.array([a,b])

def rotar(P, theta, x0, y0):

    t = np.radians(theta)

    A = np.array([
        [np.cos(t), -np.sin(t)],
        [np.sin(t),  np.cos(t)]
    ])

    centro = np.array([x0,y0])

    return (P - centro) @ A.T + centro

def escalar(P, k, x0, y0):

    centro = np.array([x0,y0])

    return k*(P - centro) + centro

def reflejar_x(P):

    A = np.array([
        [1,0],
        [0,-1]
    ])

    return P @ A.T

def reflejar_y(P):

    A = np.array([
        [-1,0],
        [0,1]
    ])

    return P @ A.T

# =========================================================
# APLICAR TRANSFORMACIONES
# =========================================================

def transformar(P):

    P_new = P.copy()

    if usar_esc:
        P_new = escalar(
            P_new,
            k,
            x0,
            y0
        )

    if usar_rot:
        P_new = rotar(
            P_new,
            theta,
            x0,
            y0
        )

    if usar_refx:
        P_new = reflejar_x(P_new)

    if usar_refy:
        P_new = reflejar_y(P_new)

    if usar_tras:
        P_new = trasladar(
            P_new,
            a,
            b
        )

    return P_new

# =========================================================
# RESULTADOS
# =========================================================

P_new = transformar(P)

if P2 is not None:
    P2_new = transformar(P2)

# =========================================================
# COLUMNAS
# =========================================================

col1, col2 = st.columns([2,1])

# =========================================================
# GRÁFICA
# =========================================================

with col1:

    fig, ax = plt.subplots(figsize=(9,9))

    # -----------------------------------------------------
    # FIGURA ORIGINAL
    # -----------------------------------------------------

    P_c = np.vstack([P, P[0]])

    ax.plot(
        P_c[:,0],
        P_c[:,1],
        linewidth=3,
        linestyle='--',
        label="Figura original"
    )

    # -----------------------------------------------------
    # FIGURA TRANSFORMADA
    # -----------------------------------------------------

    Pn_c = np.vstack([P_new, P_new[0]])

    ax.plot(
        Pn_c[:,0],
        Pn_c[:,1],
        linewidth=3,
        label="Figura transformada"
    )

    # -----------------------------------------------------
    # SEGUNDA FIGURA
    # -----------------------------------------------------

    if P2 is not None:

        P2_c = np.vstack([P2, P2[0]])

        ax.plot(
            P2_c[:,0],
            P2_c[:,1],
            linewidth=2,
            linestyle=':',
            label="Segunda figura"
        )

        P2n_c = np.vstack([P2_new, P2_new[0]])

        ax.plot(
            P2n_c[:,0],
            P2n_c[:,1],
            linewidth=2,
            label="Segunda transformada"
        )

    # -----------------------------------------------------
    # VÉRTICES
    # -----------------------------------------------------

    if mostrar_vertices:

        ax.scatter(
            P[:,0],
            P[:,1],
            s=80
        )

        ax.scatter(
            P_new[:,0],
            P_new[:,1],
            s=80
        )

    # -----------------------------------------------------
    # NOMBRES
    # -----------------------------------------------------

    if mostrar_nombres:

        letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for i, p in enumerate(P):

            ax.text(
                p[0],
                p[1],
                letras[i],
                fontsize=12
            )

        for i, p in enumerate(P_new):

            ax.text(
                p[0],
                p[1],
                letras[i] + "'",
                fontsize=12
            )

    # -----------------------------------------------------
    # CENTRO
    # -----------------------------------------------------

    ax.scatter(
        [x0],
        [y0],
        s=120,
        marker='x',
        label="Centro"
    )

    # -----------------------------------------------------
    # ESTILO
    # -----------------------------------------------------

    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.grid(True, linestyle='--', alpha=0.5)

    ax.set_xlim(-15,15)
    ax.set_ylim(-15,15)

    ax.set_aspect('equal')

    ax.legend()

    st.pyplot(fig)

# =========================================================
# INFORMACIÓN
# =========================================================

with col2:

    st.subheader("Transformaciones activas")

    if usar_tras:
        st.success(f"Traslación ({a},{b})")

    if usar_rot:
        st.success(f"Rotación {theta}°")

    if usar_esc:
        st.success(f"Homotecia k={k}")

    if usar_refx:
        st.success("Reflexión eje X")

    if usar_refy:
        st.success("Reflexión eje Y")

    st.divider()

    st.subheader("Coordenadas originales")

    st.write(P)

    st.subheader("Coordenadas transformadas")

    st.write(np.round(P_new,2))

# =========================================================
# SUPERPOSICIÓN
# =========================================================

st.divider()

st.subheader("Análisis de superposición")

st.write("""
Observe cómo las figuras pueden:

- coincidir parcialmente
- reflejarse
- rotarse
- trasladarse
- cambiar de tamaño

igual que en GeoGebra.
""")

# =========================================================
# MATRIZ
# =========================================================

st.divider()

st.subheader("Transformación matricial")

st.latex(r"T(x)=Ax+b")

st.write("""
Las transformaciones geométricas pueden representarse
mediante matrices y vectores.
""")

# =========================================================
# EXPORTAR
# =========================================================

config = {
    "traslacion_x": a,
    "traslacion_y": b,
    "rotacion": theta,
    "escala": k,
    "centro_x": x0,
    "centro_y": y0
}

st.download_button(
    "Descargar configuración",
    json.dumps(config, indent=4),
    file_name="configuracion.json"
)
