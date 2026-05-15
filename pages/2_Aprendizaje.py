import streamlit as st

st.title("Aprendizaje")

st.header("Traslación")

st.write("""
Una traslación mueve todos los puntos de una figura
la misma distancia y en la misma dirección.
""")

st.latex(r"(x,y)\rightarrow(x+a,y+b)")

st.header("Rotación")

st.write("""
Una rotación gira una figura alrededor de un punto.
""")

st.latex(r"(x,y)\rightarrow(x\cos\theta-y\sin\theta,\ x\sin\theta+y\cos\theta)")

st.header("Reflexión")

st.write("""
Una reflexión produce una imagen especular.
""")

st.header("Homotecia")

st.write("""
Una homotecia cambia el tamaño de la figura.
""")

st.latex(r"(x,y)\rightarrow(kx,ky)")
