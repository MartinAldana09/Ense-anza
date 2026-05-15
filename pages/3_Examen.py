import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Evaluación",
    layout="wide"
)

st.title("Evaluación Interactiva: Transformaciones en el Plano")

st.write("""
Esta evaluación está diseñada para ayudarte a comprender:

- Traslaciones
- Rotaciones
- Reflexiones
- Homotecias
- Composición de transformaciones
- Interpretación geométrica
""")

# =========================================================
# DATOS ESTUDIANTE
# =========================================================

st.subheader("Información del estudiante")

nombre = st.text_input("Nombre")
curso = st.text_input("Curso")

st.divider()

# =========================================================
# FUNCIONES GRAFICAR
# =========================================================

def dibujar(P1, P2=None, titulo="Plano"):

    fig, ax = plt.subplots(figsize=(7,7))

    P1_c = np.vstack([P1, P1[0]])

    ax.plot(
        P1_c[:,0],
        P1_c[:,1],
        'k--',
        linewidth=2,
        label="Figura original"
    )

    for i, p in enumerate(P1):
        ax.text(p[0], p[1], f"A{i+1}", fontsize=12)

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
            ax.text(p[0], p[1], f"B{i+1}", fontsize=12)

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
# INTRODUCCIÓN
# =========================================================

st.header("Situación")

st.write("""
Un diseñador gráfico está usando transformaciones geométricas
para mover figuras en el plano cartesiano.

Tu objetivo será descubrir qué transformación ocurrió
y luego intentar reproducirla usando el simulador.
""")

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

st.subheader("Triángulos")

col1, col2 = st.columns(2)

with col1:

    st.write("Triángulo original")

    st.latex(r"A_1=\left(\frac12,\frac32\right)")
    st.latex(r"A_2=\left(\frac72,\frac32\right)")
    st.latex(r"A_3=\left(\frac12,\frac92\right)")

with col2:

    st.write("Triángulo transformado")

    st.latex(r"B_1=(3,1)")
    st.latex(r"B_2=(9,1)")
    st.latex(r"B_3=(3,7)")

dibujar(A, B)

# =========================================================
# PREGUNTA 1
# =========================================================

st.divider()

st.header("Pregunta 1")

st.write("""
¿Qué parece haber ocurrido con el tamaño del triángulo?
""")

respuesta1 = st.radio(
    "Seleccione una opción",
    [
        "El triángulo disminuyó",
        "El triángulo conservó exactamente el mismo tamaño",
        "El triángulo aumentó de tamaño",
        "El triángulo desapareció"
    ],
    key="p1"
)

if st.button("Validar pregunta 1"):

    if respuesta1 == "El triángulo aumentó de tamaño":

        st.success("""
Correcto.

El triángulo destino es más grande.
Parece existir una homotecia o escala.
""")

    else:

        st.error("""
Incorrecto.

Observa que las longitudes aumentaron.
""")

# =========================================================
# PREGUNTA 2
# =========================================================

st.divider()

st.header("Pregunta 2")

st.write("""
¿Qué transformación mueve una figura sin cambiar
su tamaño ni su orientación?
""")

respuesta2 = st.radio(
    "Seleccione la transformación",
    [
        "Rotación",
        "Homotecia",
        "Traslación",
        "Reflexión"
    ],
    key="p2"
)

if st.button("Validar pregunta 2"):

    if respuesta2 == "Traslación":

        st.success("""
Excelente.

La traslación solo mueve la figura.
""")

    else:

        st.warning("""
No exactamente.

Piensa cuál transformación solo desplaza
todos los puntos la misma distancia.
""")

# =========================================================
# PREGUNTA 3
# =========================================================

st.divider()

st.header("Pregunta 3")

st.write("""
Si una figura rota 90° antihorario alrededor del origen,
¿qué ocurre?
""")

respuesta3 = st.radio(
    "Seleccione una opción",
    [
        "La figura cambia de tamaño",
        "La figura gira",
        "La figura desaparece",
        "La figura se refleja"
    ],
    key="p3"
)

if st.button("Validar pregunta 3"):

    if respuesta3 == "La figura gira":

        st.success("""
Perfecto.

Una rotación produce un giro alrededor de un punto.
""")

    else:

        st.error("""
Incorrecto.

Una rotación produce un giro.
""")

# =========================================================
# PREGUNTA 4
# =========================================================

st.divider()

st.header("Pregunta 4")

st.write("""
¿Qué hace una reflexión respecto al eje X?
""")

respuesta4 = st.radio(
    "Seleccione una opción",
    [
        "Duplica el tamaño",
        "Mueve la figura hacia arriba",
        "Produce una imagen especular",
        "Rota 180 grados"
    ],
    key="p4"
)

if st.button("Validar pregunta 4"):

    if respuesta4 == "Produce una imagen especular":

        st.success("""
Muy bien.

La reflexión crea un efecto espejo.
""")

    else:

        st.error("""
Incorrecto.

La reflexión produce una imagen especular.
""")

# =========================================================
# PREGUNTA 5
# =========================================================

st.divider()

st.header("Pregunta 5")

st.write("""
Si k = 2 en una homotecia,
¿qué sucede con la figura?
""")

respuesta5 = st.radio(
    "Seleccione una opción",
    [
        "La figura se hace dos veces más grande",
        "La figura gira",
        "La figura desaparece",
        "La figura se traslada"
    ],
    key="p5"
)

if st.button("Validar pregunta 5"):

    if respuesta5 == "La figura se hace dos veces más grande":

        st.success("""
Correcto.

La homotecia con k=2 duplica el tamaño.
""")

    else:

        st.warning("""
Incorrecto.

Recuerda que la homotecia cambia el tamaño.
""")

# =========================================================
# SIMULADOR
# =========================================================

st.divider()

st.header("Simulador para resolver el problema")

st.write("""
Intenta transformar el triángulo original
para hacerlo coincidir con el triángulo destino.
""")

# =========================================================
# PARÁMETROS
# =========================================================

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
# GRAFICAR RESULTADO
# =========================================================

fig, ax = plt.subplots(figsize=(8,8))

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

Has encontrado correctamente
la transformación.
""")

else:

    st.info("""
La figura todavía no coincide exactamente.

Sigue experimentando con:
- escala
- rotación
- traslación
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

st.write(A_mat)

st.write("Vector b")

st.write(b_vec)

st.latex(r"T(x)=Ax+b")

# =========================================================
# PREGUNTA FINAL
# =========================================================

st.divider()

st.header("Reflexión final")

respuesta_final = st.radio(
    "¿El orden de las transformaciones puede cambiar el resultado?",
    [
        "Sí",
        "No"
    ]
)

if st.button("Validar reflexión final"):

    if respuesta_final == "Sí":

        st.success("""
Correcto.

El orden sí importa.
Por ejemplo:
rotar y luego trasladar
no siempre da el mismo resultado
que trasladar y luego rotar.
""")

    else:

        st.error("""
Incorrecto.

El orden de las transformaciones
sí puede cambiar el resultado.
""")

# =========================================================
# FINAL
# =========================================================

st.divider()

if st.button("Enviar evaluación"):

    st.success(f"""
Evaluación enviada correctamente.

Estudiante: {nombre}
Curso: {curso}
""")
