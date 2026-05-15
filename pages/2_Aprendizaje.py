import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Aprendizaje",
    layout="wide"
)

st.title("Aprendizaje de Transformaciones Geométricas")

st.write("""
Las transformaciones geométricas permiten mover, girar,
reflejar o cambiar el tamaño de figuras en el plano cartesiano.

En esta sección aprenderá:

- Traslaciones
- Rotaciones
- Reflexiones
- Homotecias

Cada tema incluye:
- explicación intuitiva
- ejemplos gráficos
- interpretación geométrica
- ejercicios interactivos
- validación automática
""")

st.divider()

# =========================================================
# FUNCIÓN GRAFICAR
# =========================================================

def graficar(P, P2, titulo1, titulo2):

    fig, ax = plt.subplots(figsize=(6,6))

    P_c = np.vstack([P, P[0]])
    P2_c = np.vstack([P2, P2[0]])

    ax.plot(
        P_c[:,0],
        P_c[:,1],
        'k--',
        linewidth=2,
        label=titulo1
    )

    ax.plot(
        P2_c[:,0],
        P2_c[:,1],
        'b-',
        linewidth=2,
        label=titulo2
    )

    ax.scatter(P[:,0], P[:,1], color='black')
    ax.scatter(P2[:,0], P2[:,1], color='blue')

    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.grid(True, linestyle='--', alpha=0.5)

    ax.set_xlim(-8,8)
    ax.set_ylim(-8,8)

    ax.set_aspect('equal')

    ax.legend()

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

st.write("""
Una traslación mueve todos los puntos
la misma distancia y en la misma dirección.

La figura:

- no gira
- no cambia de tamaño
- no cambia de forma

solo cambia de posición.
""")

st.subheader("Ejemplo intuitivo")

st.write("""
Imagine mover una silla dentro del salón.
La silla sigue igual,
solo cambia de lugar.
""")

st.subheader("Fórmula")

st.latex(r"(x,y)\rightarrow(x+a,y+b)")

a = 3
b = 2

P_tras = P + np.array([a,b])

graficar(
    P,
    P_tras,
    "Original",
    "Trasladada"
)

st.subheader("Interpretación")

st.write(f"""
Cada punto se desplazó:

- {a} unidades en x
- {b} unidades en y
""")

st.subheader("Ejercicio interactivo")

st.write("""
Un dron está en el punto:

(2,3)

Luego se mueve:

- 5 unidades a la derecha
- 2 unidades hacia abajo

¿Dónde termina?
""")

respuesta1 = st.radio(
    "Seleccione la respuesta correcta",
    [
        "(7,1)",
        "(5,5)",
        "(7,5)",
        "(2,1)"
    ],
    key="tras"
)

if st.button("Verificar traslación"):

    if respuesta1 == "(7,1)":
        st.success("""
Perfecto.

El movimiento fue:

x: 2 + 5 = 7
y: 3 - 2 = 1
""")
    else:
        st.error("""
Respuesta incorrecta.

Recuerde:
- derecha suma en x
- abajo resta en y
""")

st.divider()

# =========================================================
# ROTACIÓN
# =========================================================

st.header("Rotación")

st.write("""
Una rotación gira una figura
alrededor de un punto fijo.
""")

st.subheader("Ejemplo intuitivo")

st.write("""
Las aspas de un ventilador
realizan rotaciones.

Las manecillas de un reloj
también giran alrededor de un centro.
""")

st.subheader("Fórmula")

st.latex(
    r"(x,y)\rightarrow(x\cos\theta-y\sin\theta,\ x\sin\theta+y\cos\theta)"
)

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
    "Original",
    "Rotada"
)

st.subheader("Interpretación")

st.write("""
La figura giró 90 grados
en sentido antihorario
alrededor del origen.
""")

st.subheader("Ejercicio interactivo")

st.write("""
El punto:

(2,0)

se rota 90° antihorario
alrededor del origen.

¿Dónde queda?
""")

respuesta2 = st.radio(
    "Seleccione la respuesta correcta",
    [
        "(0,2)",
        "(2,2)",
        "(0,-2)",
        "(-2,0)"
    ],
    key="rot"
)

if st.button("Verificar rotación"):

    if respuesta2 == "(0,2)":
        st.success("""
Excelente.

Una rotación de 90° antihorario:

(x,y) → (-y,x)

Entonces:

(2,0) → (0,2)
""")
    else:
        st.error("""
Respuesta incorrecta.

Recuerde cómo gira el plano
en sentido antihorario.
""")

st.divider()

# =========================================================
# REFLEXIÓN
# =========================================================

st.header("Reflexión")

st.write("""
Una reflexión produce
una imagen especular.
""")

st.subheader("Ejemplo intuitivo")

st.write("""
Cuando una persona se mira
en un espejo,
aparece una reflexión.
""")

st.subheader("Reflexión respecto al eje X")

st.latex(r"(x,y)\rightarrow(x,-y)")

A_refx = np.array([
    [1,0],
    [0,-1]
])

P_ref = P @ A_refx.T

graficar(
    P,
    P_ref,
    "Original",
    "Reflejada"
)

st.subheader("Interpretación")

st.write("""
Las coordenadas x
permanecen iguales.

Las coordenadas y
cambian de signo.
""")

st.subheader("Ejercicio interactivo")

st.write("""
Refleje el punto:

(4,-3)

respecto al eje X.
""")

respuesta3 = st.radio(
    "Seleccione la respuesta correcta",
    [
        "(4,3)",
        "(-4,-3)",
        "(3,4)",
        "(-4,3)"
    ],
    key="ref"
)

if st.button("Verificar reflexión"):

    if respuesta3 == "(4,3)":
        st.success("""
Muy bien.

En una reflexión respecto al eje X:

- x permanece igual
- y cambia de signo
""")
    else:
        st.error("""
Respuesta incorrecta.

Observe qué coordenada
debe cambiar de signo.
""")

st.divider()

# =========================================================
# HOMOTECIA
# =========================================================

st.header("Homotecia")

st.write("""
Una homotecia cambia
el tamaño de una figura.
""")

st.subheader("Ejemplo intuitivo")

st.write("""
Cuando amplía una imagen
en el celular,
la figura conserva la forma,
pero cambia de tamaño.
""")

st.subheader("Fórmula")

st.latex(r"(x,y)\rightarrow(kx,ky)")

k = 2

P_hom = k * P

graficar(
    P,
    P_hom,
    "Original",
    "Homotecia"
)

st.subheader("Interpretación")

st.write("""
La figura aumentó
su tamaño al doble.
""")

st.subheader("Ejercicio interactivo")

st.write("""
Aplique una homotecia
de razón:

k = 3

al punto:

(2,1)

¿Cuál es el resultado?
""")

respuesta4 = st.radio(
    "Seleccione la respuesta correcta",
    [
        "(6,3)",
        "(5,3)",
        "(2,3)",
        "(3,1)"
    ],
    key="hom"
)

if st.button("Verificar homotecia"):

    if respuesta4 == "(6,3)":
        st.success("""
Correcto.

En una homotecia:

(x,y) → (kx,ky)

Entonces:

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

tabla = {
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
}

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

¿Qué ocurre si:

1. primero refleja la figura
2. luego la traslada?
""")

respuesta_final = st.radio(
    "Seleccione la afirmación correcta",
    [
        "El orden de las transformaciones no importa nunca",
        "La figura cambia completamente de forma",
        "El orden puede cambiar el resultado final",
        "La traslación cambia el tamaño de la figura"
    ]
)

if st.button("Verificar reto final"):

    if respuesta_final == "El orden puede cambiar el resultado final":
        st.success("""
Excelente análisis.

El orden de las transformaciones
sí puede modificar
la posición y orientación final.
""")
    else:
        st.error("""
Revise nuevamente cómo actúan
las composiciones de transformaciones.
""")

st.divider()

st.header("Conclusión")

st.write("""
Las transformaciones geométricas
son fundamentales en:

- matemáticas
- física
- ingeniería
- arquitectura
- diseño gráfico
- videojuegos
- animación

Comprenderlas permite analizar
cómo cambian las figuras
en el plano cartesiano.
""")
