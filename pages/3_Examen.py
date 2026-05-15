import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Evaluación",
    layout="wide"
)

st.title("Evaluación: Transformaciones en el Plano")

st.write("""
En esta sección debe utilizar el simulador como:

- papel milimetrado
- graficador
- herramienta de experimentación
- apoyo para justificar respuestas

Se recomienda:

- superponer figuras
- probar transformaciones
- verificar coordenadas
- analizar si el orden cambia el resultado
""")

st.divider()

# =========================================================
# FUNCIÓN PARA GRAFICAR
# =========================================================

def graficar_figuras(
    P1,
    P2=None,
    nombre1="Figura 1",
    nombre2="Figura 2"
):

    fig, ax = plt.subplots(figsize=(7,7))

    P1_c = np.vstack([P1, P1[0]])

    ax.plot(
        P1_c[:,0],
        P1_c[:,1],
        'b-',
        linewidth=2,
        label=nombre1
    )

    ax.scatter(P1[:,0], P1[:,1], color='blue')

    for i, p in enumerate(P1):
        ax.text(p[0], p[1], f"A{i+1}")

    if P2 is not None:

        P2_c = np.vstack([P2, P2[0]])

        ax.plot(
            P2_c[:,0],
            P2_c[:,1],
            'r--',
            linewidth=2,
            label=nombre2
        )

        ax.scatter(P2[:,0], P2[:,1], color='red')

        for i, p in enumerate(P2):
            ax.text(p[0], p[1], f"B{i+1}")

    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.grid(True, linestyle='--', alpha=0.5)

    ax.set_xlim(-2,12)
    ax.set_ylim(-2,12)

    ax.set_aspect('equal')

    ax.legend()

    st.pyplot(fig)

# =========================================================
# EJERCICIO 1
# =========================================================

st.header("Ejercicio 1 — Dos caminos diferentes")

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

A = np.array([
    [0.5,1.5],
    [3.5,1.5],
    [0.5,4.5]
])

B = np.array([
    [3,1],
    [9,1],
    [3,7]
])

st.subheader("Visualización")

graficar_figuras(
    A,
    B,
    "Triángulo A",
    "Triángulo B"
)

st.subheader("Pregunta a)")

st.write("""
Observe cuidadosamente ambas figuras.

Utilice el simulador para:

- comparar tamaños
- verificar distancias
- analizar coordenadas
- probar transformaciones

Escriba qué relación observa entre A y B.
""")

respuesta_a = st.text_area(
    "Respuesta a)",
    placeholder="""
Ejemplo de formato:

'El triángulo B parece una homotecia de razón 2 aplicada al triángulo A.'
""",
    height=150
)

if st.button("Verificar análisis", key="a"):

    if len(respuesta_a) > 30:

        st.success("""
Buen análisis.

La idea es identificar:

- cambios de tamaño
- posibles traslaciones
- relaciones entre coordenadas
- composiciones de transformaciones
""")

    else:

        st.warning("""
La respuesta es demasiado corta.

Justifique observando coordenadas y transformaciones.
""")

# =========================================================
# PREGUNTA B
# =========================================================

st.subheader("Pregunta b)")

st.write("""
Encuentre DOS secuencias diferentes de transformaciones
que lleven el triángulo A sobre el triángulo B.

Debe indicar:

- tipo de transformación
- parámetros
- orden
- coordenadas intermedias

Use el simulador para probar sus ideas.
""")

respuesta_b = st.text_area(
    "Respuesta b)",
    placeholder="""
Ejemplo:

1. Homotecia de razón ...
2. Traslación con vector ...

Coordenadas intermedias:
(...)
""",
    height=220
)

if st.button("Validar secuencia", key="b"):

    if len(respuesta_b) > 80:

        st.success("""
La respuesta tiene suficiente desarrollo.

Verifique:

- orden correcto
- parámetros claros
- coordenadas coherentes
- justificación geométrica
""")

    else:

        st.warning("""
Falta desarrollo.

Explique mejor las transformaciones y el orden.
""")

# =========================================================
# PREGUNTA C
# =========================================================

st.subheader("Pregunta c)")

st.write("""
Compare las dos secuencias encontradas.

Explique:

- cuál parece más eficiente
- si el orden cambia el resultado
- por qué ocurre eso
""")

respuesta_c = st.text_area(
    "Respuesta c)",
    placeholder="""
Ejemplo:

'El orden sí cambia el resultado porque...'
""",
    height=180
)

if st.button("Revisar argumentación", key="c"):

    if len(respuesta_c) > 60:

        st.success("""
La argumentación tiene buena estructura.

Recuerde justificar usando propiedades
de las transformaciones geométricas.
""")

    else:

        st.warning("""
Debe justificar más claramente sus ideas.
""")

st.divider()

# =========================================================
# EJERCICIO 2
# =========================================================

st.header("Ejercicio 2 — La transformación perdida")

st.write("""
Un estudiante aplicó varias transformaciones a un cuadrado.
""")

st.write("""
Paso 1:
Traslación con vector (2,-1)

Paso 2:
Transformación desconocida T

Paso 3:
Homotecia de razón k=3
""")

C = np.array([
    [0,0],
    [1,0],
    [1,1],
    [0,1]
])

C_final = np.array([
    [6,3],
    [9,3],
    [9,6],
    [6,6]
])

st.subheader("Superposición de figuras")

graficar_figuras(
    C,
    C_final,
    "Cuadrado original",
    "Resultado final"
)

st.subheader("Pregunta")

st.write("""
Determine cuál podría ser
la transformación desconocida T.

Debe indicar:

- tipo
- parámetros
- explicación
- justificación
""")

respuesta2 = st.text_area(
    "Respuesta ejercicio 2",
    placeholder="""
Ejemplo:

'T parece ser una reflexión respecto...'
""",
    height=220
)

if st.button("Validar ejercicio 2"):

    if len(respuesta2) > 70:

        st.success("""
Buen trabajo.

Utilice el simulador para comprobar:

- distancias
- orientación
- tamaño
- posición
""")

    else:

        st.warning("""
La respuesta necesita más análisis geométrico.
""")

st.divider()

# =========================================================
# EJERCICIO 3
# =========================================================

st.header("Ejercicio 3 — Creando un vitral")

st.write("""
La figura base es:
""")

st.latex(r"P=(0,0)")
st.latex(r"Q=(2,0)")
st.latex(r"R=(0,3)")

P_base = np.array([
    [0,0],
    [2,0],
    [0,3]
])

st.subheader("Figura original")

graficar_figuras(
    P_base,
    None,
    "Figura original"
)

st.write("""
Aplique en orden:

1. Reflexión respecto al eje X
2. Traslación con vector (3,2)

Use el simulador para encontrar
las coordenadas finales.
""")

respuesta3 = st.text_area(
    "Respuesta ejercicio 3",
    placeholder="""
Escriba las coordenadas así:

P'=(...)
Q'=(...)
R'=(...)

Luego explique qué ocurrió.
""",
    height=250
)

if st.button("Validar ejercicio 3"):

    if len(respuesta3) > 80:

        st.success("""
La respuesta tiene suficiente desarrollo.

Compruebe en el simulador:

- reflexión
- traslación
- coordenadas finales
- orientación de la figura
""")

    else:

        st.warning("""
Falta justificar mejor el procedimiento.
""")

st.divider()

# =========================================================
# EJERCICIO 4
# =========================================================

st.header("Ejercicio 4 — Deshaciendo transformaciones")

st.write("""
Una figura sufrió esta secuencia:

1. Rotación π/3 antihoraria
2. Homotecia k=1/2
3. Traslación (-2,3)

Escriba la secuencia inversa completa.
""")

respuesta4 = st.text_area(
    "Secuencia inversa",
    placeholder="""
Ejemplo:

1. ...
2. ...
3. ...

Explique por qué cada paso deshace el anterior.
""",
    height=250
)

if st.button("Revisar secuencia inversa"):

    if len(respuesta4) > 100:

        st.success("""
Muy buena argumentación.

Recuerde:

- la inversa de una traslación
  usa el vector opuesto

- la inversa de una rotación
  usa el ángulo contrario

- la inversa de una homotecia
  usa razón recíproca
""")

    else:

        st.warning("""
Explique con más detalle
cómo se deshace cada transformación.
""")

st.divider()

st.header("Conclusión")

st.write("""
El simulador funciona como:

- plano cartesiano
- laboratorio geométrico
- herramienta de validación
- espacio de exploración matemática

La idea no es solo obtener respuestas,
sino comprender:

- cómo actúan las transformaciones
- cómo se combinan
- cómo cambia una figura
- por qué el orden importa
""")
