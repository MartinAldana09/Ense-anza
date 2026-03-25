import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import json
import time

st.set_page_config(page_title="Simulador PRO", layout="wide")

st.title("🚀 Simulador PRO de Transformaciones Geométricas")

# -------- FIGURAS --------
def triangulo():
    return np.array([[1,1],[4,1],[2,3]], dtype=float)

def cuadrado():
    return np.array([[1,1],[3,1],[3,3],[1,3]], dtype=float)

def pentagono():
    return np.array([[0,2],[2,4],[4,2],[3,0],[1,0]], dtype=float)

figura_nombre = st.selectbox("Figura", ["Triángulo","Cuadrado","Pentágono"])

P = triangulo() if figura_nombre=="Triángulo" else cuadrado() if figura_nombre=="Cuadrado" else pentagono()

# -------- CONTROLES --------
st.sidebar.header("🎛️ Parámetros")

a = st.sidebar.number_input("Traslación X", value=0.0)
b = st.sidebar.number_input("Traslación Y", value=0.0)
k = st.sidebar.number_input("Escala k", value=1.0)
theta = st.sidebar.number_input("Rotación θ", value=0.0)

# centro de rotación
st.sidebar.subheader("📍 Centro de rotación")
x0 = st.sidebar.number_input("x₀", value=0.0)
y0 = st.sidebar.number_input("y₀", value=0.0)

# zoom
zoom = st.sidebar.slider("Zoom", 2, 20, 10)

# -------- CHECKBOX --------
st.sidebar.header("Transformaciones")
usar_tras = st.sidebar.checkbox("Traslación", True)
usar_esc = st.sidebar.checkbox("Escala")
usar_rot = st.sidebar.checkbox("Rotación")
usar_refx = st.sidebar.checkbox("Reflexión X")
usar_refy = st.sidebar.checkbox("Reflexión Y")

# -------- ANIMACIÓN --------
st.sidebar.header("🎬 Animación")
animar = st.sidebar.checkbox("Activar animación")
velocidad = st.sidebar.slider("Velocidad", 0.1, 5.0, 1.0)

# -------- TRANSFORMACIONES --------
def traslacion(P,a,b):
    return P + np.array([a,b]), np.eye(2), np.array([a,b])

def escala(P,k):
    A = k*np.eye(2)
    return P@A.T, A, np.array([0,0])

def rotacion(P,theta,x0,y0):
    t = np.radians(theta)
    A = np.array([[np.cos(t), -np.sin(t)],
                  [np.sin(t),  np.cos(t)]])
    P_shift = P - np.array([x0,y0])
    P_rot = P_shift @ A.T + np.array([x0,y0])
    return P_rot, A, np.array([x0,y0]) - A @ np.array([x0,y0])

def refx(P):
    A = np.array([[1,0],[0,-1]])
    return P@A.T, A, np.array([0,0])

def refy(P):
    A = np.array([[-1,0],[0,1]])
    return P@A.T, A, np.array([0,0])

# -------- PROCESO --------
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

# -------- ANIMACIÓN LOOP --------
if animar:
    theta += velocidad
    a += 0.05*velocidad

P_new, A_total, b_total, pasos = aplicar(P)

# -------- GRAFICA --------
fig, ax = plt.subplots(figsize=(6,6))

ax.plot(*np.vstack((P,P[0])).T, 'k--', label="Original")
ax.plot(*np.vstack((P_new,P_new[0])).T, 'b-', label="Transformada")

ax.set_xlim(-zoom,zoom)
ax.set_ylim(-zoom,zoom)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.6)

ax.scatter([x0],[y0], color='red', label="Centro rotación")

ax.legend()
st.pyplot(fig)

# -------- MATRICES PASO A PASO --------
st.subheader("🧮 Transformaciones paso a paso")

for nombre,A,b_vec in pasos:
    st.write(f"### {nombre}")
    st.write("A =")
    st.write(A)
    st.write("b =")
    st.write(b_vec)
    st.latex(r"T(x)=Ax+b")

# -------- TOTAL --------
st.subheader("🔷 Transformación total")

st.write("A total:")
st.write(A_total)

st.write("b total:")
st.write(b_total)

st.latex(r"T(x)=Ax+b")

# -------- GUARDAR --------
config = {"figura":figura_nombre,"a":a,"b":b,"k":k,"theta":theta}

st.download_button("Guardar configuración", json.dumps(config), "config.json")

# refresco animación
if animar:
    time.sleep(0.05)
    st.rerun()
