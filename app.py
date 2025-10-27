import streamlit as st

# Título de la app
st.title("¡Mi primera app!")

st.success("Mensaje de éxito ✅") 
st.error("Mensaje de error ❌") 
st.warning("Advertencia ⚠️") 
st.info("Información ℹ️") 

# Texto simple
st.write("Hola, soy [TU NOMBRE] y esta es mi primera aplicación con Streamlit.")

# Un input interactivo
nombre = st.text_input("¿Cómo te llamas?")

# Respuesta condicional
if nombre:
    st.write(f"¡Hola, {nombre}! Bienvenido/a a mi app")

# Un botón
if st.button("Presiona aquí"):
    st.balloons()  # Animación de globos
    st.success("¡Funciona perfectamente!")
