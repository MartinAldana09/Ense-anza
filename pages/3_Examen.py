import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Evaluación",
    layout="wide"
)

st.title("Evaluación: Transformaciones en el Plano")

# =========================================================
# DATOS ESTUDIANTE
# =========================================================

st.subheader("Información del estudiante")

nombre = st.text_input("Nombre")
curso = st.text_input("Curso")

st.divider()

# =========================================================
# FUNCIONES
# =========================================================

def dibujar_figuras(P1, P2=None, titulo="Plano cartesiano"):

    fig, ax = plt.subplots(figsize=(6,6))

    P1_c = np.vstack([P1, P1[0]])

    ax.plot(
        P1_c[:,0],
        P1_c[:,1],
        'k--',
        linewidth=2,
        label="Figura original"
    )

    for i, p in enumerate(P1):
        ax.text(p[0], p[1], f"A{i+1}")

    if P2 is not None:

        P2_c = np.vstack([P2, P2[0]])

        ax.plot(
            P2_c[:,0],
            P2_c[:,1],
            'b-',
            linewidth=2,
            label="Figura transformada"
        )

        for i, p in enumerate(P2):
            ax.text(p[0], p[1], f"B{i+1}")

    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.grid(True, linestyle='--', alpha=0.5)

    ax.set_aspect('equal')

    ax.set_xlim(-2, 12)
    ax.set_ylim(-2, 10)

    ax.legend()

    st.pyplot(fig)

# =========================================================
# EJERCICIO 1
# =========================================================

st.header("Ejercicio 1")

st.write("""
Se tienen dos triángulos en el plano cartesiano.
""")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Triángulo A")

    st.latex(r"A_1=\left(\frac12,\frac32\right)")
    st.latex(r"A_2=\left(\frac72,\frac32\right)")
    st.latex(r"A_3=\left(\frac12,\frac92\right)")

with col2:

    st.subheader("Triángulo B")

    st.latex(r"B_1=(3,1)")
    st.latex(r"B_2=(9,1)")
    st.latex(r"B_3=(3,7)")

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

dibujar_figuras(A, B)

# =========================================================
# RESPUESTA
# =========================================================

st.subheader("Pregunta")

st.write("""
¿Qué relación observa entre las coordenadas del triángulo A y el triángulo B?
""")

respuesta1 = st.text_area(
    "Escriba su respuesta",
    height=150
)

# =========================================================
# VALIDACIÓN SIMPLE
# =========================================================

palabras_clave = [
    "escala",
    "homotecia",
    "traslación",
    "transformación",
    "doble",
    "2",
    "multiplica"
]

score = 0

texto = respuesta1.lower()

for palabra in palabras_clave:

    if palabra in texto:
        score += 1

# =========================================================
# FEEDBACK
# =========================================================

if st.button("Validar respuesta"):

    if score >= 3:

        st.success("""
La respuesta parece correcta.
Se identifican elementos importantes de la transformación.
""")

    else:

        st.warning("""
La respuesta parece incompleta.
Revise si describió correctamente:
- cambios de escala
- traslaciones
- relación entre coordenadas
""")

# =========================================================
# SIMULADOR DENTRO DEL EXAMEN
# =========================================================

st.divider()

st.header("Simulador para resolver el ejercicio")

st.write("""
Use el simulador para intentar transformar el triángulo A en el triángulo B.
""")

# ---------------------------------------------------------
# PARÁMETROS
# ---------------------------------------------------------

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
# FUNCIONES TRANSFORMACIÓN
# =========================================================

def escala(P, k):

    A = k * np.eye(2)

    return P @ A.T

# ---------------------------------------------------------

def traslacion(P, a, b):

    return P + np.array([a,b])

# ---------------------------------------------------------

def rotacion(P, theta):

    t = np.radians(theta)

    A = np.array([
        [np.cos(t), -np.sin(t)],
        [np.sin(t),  np.cos(t)]
    ])

    return P @ A.T

# =========================================================
# APLICAR
# =========================================================

P_new = A.copy()

P_new = escala(P_new, k)

P_new = rotacion(P_new, theta)

P_new = traslacion(P_new, a, b)

# =========================================================
# DIBUJAR RESULTADO
# =========================================================

fig, ax = plt.subplots(figsize=(7,7))

A_c = np.vstack([A, A[0]])
B_c = np.vstack([B, B[0]])
P_c = np.vstack([P_new, P_new[0]])

# ORIGINAL

ax.plot(
    A_c[:,0],
    A_c[:,1],
    'k--',
    linewidth=2,
    label="Original"
)

# DESTINO

ax.plot(
    B_c[:,0],
    B_c[:,1],
    'g-',
    linewidth=2,
    label="Destino"
)

# ESTUDIANTE

ax.plot(
    P_c[:,0],
    P_c[:,1],
    'b-',
    linewidth=2,
    label="Tu transformación"
)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.grid(True, linestyle='--', alpha=0.5)

ax.set_xlim(-2, 12)
ax.set_ylim(-2, 10)

ax.set_aspect('equal')

ax.legend()

st.pyplot(fig)

# =========================================================
# VERIFICAR SI COINCIDE
# =========================================================

error = np.linalg.norm(P_new - B)

if error < 0.01:

    st.success("""
Excelente.
La transformación coincide con el triángulo destino.
""")

else:

    st.info("""
La figura todavía no coincide exactamente con el destino.
Siga ajustando los parámetros.
""")

# =========================================================
# MATRICES
# =========================================================

st.subheader("Representación matricial")

t = np.radians(theta)

A_mat = k * np.array([
    [np.cos(t), -np.sin(t)],
    [np.sin(t),  np.cos(t)]
])

b_vec = np.array([a,b])

st.write("Matriz A")

st.write(A_mat)

st.write("Vector b")

st.write(b_vec)

st.latex(r"T(x)=Ax+b")

# =========================================================
# RESPUESTA FINAL
# =========================================================

st.subheader("Justificación")

respuesta_final = st.text_area(
    "Explique el procedimiento utilizado",
    height=200
)

if st.button("Enviar evaluación"):

    st.success("""
Evaluación enviada correctamente.
""")
