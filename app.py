import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import json
import time

st.set_page_config(page_title="Simulador PRO", layout="wide")

st.title(" Simulador PRO de Transformaciones Geométricas")

# -------- CREAR FIGURA --------
st.subheader("Crear figura")

modo_figura = st.radio("Tipo de figura", ["Predefinida", "Personalizada", "Círculo"])

def triangulo():
    return np.array([[1,1],[4,1],[2,3]], dtype=float)

def cuadrado():
    return np.array([[1,1],[3,1],[3,3],[1,3]], dtype=float)

def pentagono():
    return np.array([[0,2],[2,4],[4,2],[3,0],[1,0]], dtype=float)

if modo_figura == "Predefinida":
    figura_nombre = st.selectbox("Figura", ["Triángulo","Cuadrado","Pentágono"])
    P = triangulo() if figura_nombre=="Triángulo" else cuadrado() if figura_nombre=="Cuadrado" else pentagono()

elif modo_figura == "Personalizada":
    texto = st.text_area("Puntos (x,y):", "(1,1), (4,1), (2,3)")
    try:
        puntos = []
        pares = texto.replace(" ", "").split("),")
        for p in pares:
            p = p.replace("(", "").replace(")", "")
            x, y = map(float, p.split(","))
            puntos.append([x,y])
        P = np.array(puntos, dtype=float)
    except:
        st.error("Formato incorrecto. Usa: (x,y), (x,y)")
        st.stop()

else:
    st.subheader(" Parámetros del círculo")
    cx = float(st.number_input("Centro X", value=0.0))
    cy = float(st.number_input("Centro Y", value=0.0))
    r = float(st.number_input("Radio", value=2.0, min_value=0.1))

    t = np.linspace(0, 2*np.pi, 100)
    x = cx + r*np.cos(t)
    y = cy + r*np.sin(t)
    P = np.column_stack((x,y))

st.write("Puntos de la figura:")
st.write(P)

# -------- CONTROLES --------
st.sidebar.header(" Parámetros")

a = float(st.sidebar.number_input("Traslación X", value=0.0))
b = float(st.sidebar.number_input("Traslación Y", value=0.0))
k = float(st.sidebar.number_input("Escala k", value=1.0))
theta = float(st.sidebar.number_input("Rotación θ", value=0.0))

# centro rotación
st.sidebar.subheader(" Centro de rotación")
x0 = float(st.sidebar.number_input("x₀", value=0.0))
y0 = float(st.sidebar.number_input("y₀", value=0.0))

# -------- ZOOM (CORREGIDO) --------
st.sidebar.subheader(" Vista")

x_centro = float(st.sidebar.number_input("Centro vista X", value=0.0))
y_centro = float(st.sidebar.number_input("Centro vista Y", value=0.0))
escala = float(st.sidebar.number_input("Escala visual", value=10.0, min_value=1.0))

# -------- TRANSFORMACIONES --------
st.sidebar.header("Transformaciones")
usar_tras = st.sidebar.checkbox("Traslación", True)
usar_esc = st.sidebar.checkbox("Escala")
usar_rot = st.sidebar.checkbox("Rotación")
usar_refx = st.sidebar.checkbox("Reflexión X")
usar_refy = st.sidebar.checkbox("Reflexión Y")

# -------- ANIMACIÓN --------
st.sidebar.header(" Animación")
animar = st.sidebar.checkbox("Activar animación")
velocidad = float(st.sidebar.slider("Velocidad", 0.1, 5.0, 1.0))

# -------- FUNCIONES --------
def traslacion(P,a,b):
    return P + np.array([a,b]), np.eye(2), np.array([a,b])

def escala(P,k):
    A = k*np.eye(2)
    return P@A.T, A, np.array([0.0,0.0])

def rotacion(P,theta,x0,y0):
    t = np.radians(theta)
    A = np.array([[np.cos(t), -np.sin(t)],
                  [np.sin(t),  np.cos(t)]])
    P_shift = P - np.array([x0,y0])
    P_rot = P_shift @ A.T + np.array([x0,y0])
    return P_rot, A, np.array([x0,y0]) - A @ np.array([x0,y0])

def refx(P):
    A = np.array([[1,0],[0,-1]])
    return P@A.T, A, np.array([0.0,0.0])

def refy(P):
    A = np.array([[-1,0],[0,1]])
    return P@A.T, A, np.array([0.0,0.0])

# -------- APLICAR --------
def aplicar(P):
    P_new = P.copy()
    A_total = np.eye(2)
    b_total = np.array([0.0,0.0])
    pasos = []

    if usar_esc:
        P_new, A, b_vec = escala(P_new,k)
        A_total = A @ A_total
        b_total = A @ b_total + b_vec
        pasos.append(("Escala",A,b_vec))

    if usar_rot:
        P_new, A, b_vec = rotacion(P_new,theta,x0,y0)
        A_total = A @ A_total
        b_total = A @ b_total + b_vec
        pasos.append(("Rotación",A,b_vec))

    if usar_refx:
        P_new, A, b_vec = refx(P_new)
        A_total = A @ A_total
        b_total = A @ b_total + b_vec
        pasos.append(("Reflexión X",A,b_vec))

    if usar_refy:
        P_new, A, b_vec = refy(P_new)
        A_total = A @ A_total
        b_total = A @ b_total + b_vec
        pasos.append(("Reflexión Y",A,b_vec))

    if usar_tras:
        P_new, A, b_vec = traslacion(P_new,a,b)
        A_total = A @ A_total
        b_total = A @ b_total + b_vec
        pasos.append(("Traslación",A,b_vec))

    return P_new, A_total, b_total, pasos

# -------- ANIMACIÓN --------
if animar:
    theta += velocidad
    a += 0.05*velocidad

P_new, A_total, b_total, pasos = aplicar(P)

# -------- GRAFICA --------
fig, ax = plt.subplots(figsize=(6,6))

P_cerrado = np.vstack([P, P[0]])
P_new_cerrado = np.vstack([P_new, P_new[0]])

ax.plot(P_cerrado[:,0], P_cerrado[:,1], 'k--', label="Original")
ax.plot(P_new_cerrado[:,0], P_new_cerrado[:,1], 'b-', label="Transformada")

# zoom seguro
try:
    ax.set_xlim(x_centro - escala, x_centro + escala)
    ax.set_ylim(y_centro - escala, y_centro + escala)
except:
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)

# ejes tipo GeoGebra
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.6)

ax.scatter([x0],[y0], color='red', label="Centro rotación")

ax.legend()
st.pyplot(fig)

# -------- MATRICES --------
st.subheader(" Transformaciones paso a paso")

for nombre,A,b_vec in pasos:
    st.write(f"### {nombre}")
    st.write("A =")
    st.write(A)
    st.write("b =")
    st.write(b_vec)

st.subheader(" Transformación total")
st.write("A total:")
st.write(A_total)
st.write("b total:")
st.write(b_total)

st.latex(r"T(x)=Ax+b")

# -------- GUARDAR --------
config = {"a":a,"b":b,"k":k,"theta":theta}
st.download_button("Guardar configuración", json.dumps(config), "config.json")

# -------- LOOP --------
if animar:
    time.sleep(0.05)
    st.rerun()
