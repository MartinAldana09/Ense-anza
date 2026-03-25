import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import json

st.set_page_config(page_title="Simulador Geométrico", layout="wide")

st.title("🔷 Simulador de Transformaciones Geométricas")

# -------- FIGURAS --------
def triangulo():
    return np.array([[1,1],[4,1],[2,3]])

def cuadrado():
    return np.array([[1,1],[3,1],[3,3],[1,3]])

def pentagono():
    return np.array([[0,2],[2,4],[4,2],[3,0],[1,0]])

figura_nombre = st.selectbox("Selecciona figura", ["Triángulo","Cuadrado","Pentágono"])

if figura_nombre == "Triángulo":
    P = triangulo()
elif figura_nombre == "Cuadrado":
    P = cuadrado()
else:
    P = pentagono()

# -------- SIDEBAR --------
st.sidebar.header("⚙️ Parámetros")

a = st.sidebar.slider("Traslación X", -10.0, 10.0, 0.0)
b = st.sidebar.slider("Traslación Y", -10.0, 10.0, 0.0)
k = st.sidebar.slider("Escala (k)", 0.1, 5.0, 1.0)
theta = st.sidebar.slider("Rotación θ", -180, 180, 0)

st.sidebar.header("🔘 Transformaciones")

usar_tras = st.sidebar.checkbox("Traslación", True)
usar_esc = st.sidebar.checkbox("Escala")
usar_rot = st.sidebar.checkbox("Rotación")
usar_refx = st.sidebar.checkbox("Reflexión eje X")
usar_refy = st.sidebar.checkbox("Reflexión eje Y")

# -------- TRANSFORMACIONES --------
def traslacion(P,a,b):
    return P + np.array([a,b])

def homotecia(P,k):
    return P * k

def rotacion(P,theta):
    t = np.radians(theta)
    A = np.array([[np.cos(t), -np.sin(t)],
                  [np.sin(t),  np.cos(t)]])
    return P @ A.T, A

def reflexion_x(P):
    A = np.array([[1,0],[0,-1]])
    return P @ A.T, A

def reflexion_y(P):
    A = np.array([[-1,0],[0,1]])
    return P @ A.T, A

# -------- APLICAR TRANSFORMACIONES --------
P_new = P.copy()
A_total = np.eye(2, dtype=float)
b_total = np.array([0.0, 0.0])

pasos = []

if usar_esc:
    P_new = homotecia(P_new,k)
    A_total = k * A_total
    pasos.append(f"Escala: (x,y)→({k:.2f}x,{k:.2f}y)")

if usar_rot:
    P_new, A = rotacion(P_new,theta)
    A_total = A @ A_total
    pasos.append(f"Rotación θ={theta}°")

if usar_refx:
    P_new, A = reflexion_x(P_new)
    A_total = A @ A_total
    pasos.append("Reflexión eje X")

if usar_refy:
    P_new, A = reflexion_y(P_new)
    A_total = A @ A_total
    pasos.append("Reflexión eje Y")

if usar_tras:
    P_new = traslacion(P_new,a,b)
    b_total += np.array([a,b])
    pasos.append(f"Traslación: (x,y)→(x+{a:.2f},y+{b:.2f})")

# -------- GRAFICA --------
fig, ax = plt.subplots()

ax.plot(*np.vstack((P,P[0])).T, 'k--', label="Original")
ax.plot(*np.vstack((P_new,P_new[0])).T, 'b-', label="Transformada")

ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.grid()
ax.legend()

st.pyplot(fig)

# -------- FORMULAS --------
st.subheader("📐 Transformaciones aplicadas")
for p in pasos:
    st.write(p)

st.latex(r"(x,y) \rightarrow (x+a, y+b)")
st.latex(r"(x,y) \rightarrow (kx, ky)")
st.latex(r"(x,y) \rightarrow (x\cos\theta - y\sin\theta,\; x\sin\theta + y\cos\theta)")

# -------- MATRICES --------
st.subheader("🧮 Representación algebraica")

st.write("Matriz A:")
st.write(A_total)

st.write("Vector b:")
st.write(b_total)

st.latex(r"T(x) = A x + b")

# -------- GUARDAR CONFIG --------
st.subheader("💾 Guardar configuración")

config = {
    "figura": figura_nombre,
    "a": a,
    "b": b,
    "k": k,
    "theta": theta
}

st.download_button(
    label="Descargar configuración",
    data=json.dumps(config, indent=4),
    file_name="configuracion.json"
)
