import streamlit as st

# Título de la aplicación
st.title("🧮 Calculadora de IMC (Índice de Masa Corporal)")

# --- Entradas del usuario ---
# Ingreso del peso en kilogramos
peso = st.number_input("Ingresa tu peso (kg):", min_value=0.0, step=0.1)

# Ingreso de la altura en metros
altura = st.number_input("Ingresa tu altura (m):", min_value=0.0, step=0.01)

# --- Cálculo del IMC ---
# Verificamos que los valores sean mayores que cero para evitar división por cero
if peso > 0 and altura > 0:
    imc = peso / (altura ** 2)  # Fórmula del IMC
    imc_redondeado = round(imc, 2)

    # --- Determinamos la categoría del IMC ---
    if imc < 18.5:
        categoria = "Bajo peso"
        color = "blue"
    elif imc < 25:
        categoria = "Peso normal"
        color = "green"
    elif imc < 30:
        categoria = "Sobrepeso"
        color = "orange"
    else:
        categoria = "Obesidad"
        color = "red"

    # --- Mostramos el resultado ---
    st.metric(label="Tu IMC",
