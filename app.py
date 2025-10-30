import streamlit as st

# Título principal
st.title("🧮 Calculadora de IMC (Índice de Masa Corporal)")

# --- Entradas del usuario ---
# Ingreso de peso en kg
peso = st.number_input("Ingresa tu peso (kg):", min_value=0.0, step=0.1)

# Ingreso de altura en metros
altura = st.number_input("Ingresa tu altura (m):", min_value=0.0, step=0.01)

# --- Cálculo del IMC ---
# Verificamos que ambos valores sean mayores que 0 para evitar errores
if peso > 0 and altura > 0:
    imc = peso / (altura ** 2)  # Fórmula del IMC
    imc_redondeado = round(imc, 2)

    # --- Clasificación según la OMS ---
    if imc < 18.5:
        categoria = "Bajo peso"
        color = "blue"
    elif imc < 25:
        categoria = "Peso normal"
        color =
