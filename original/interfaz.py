import streamlit as st
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from io import BytesIO

# Configuración general
st.set_page_config(page_title="Sistema de Semáforo Difuso", layout="centered")
st.title("🚦 Sistema Difuso para Control de Semáforo")
st.markdown("""
Este sistema controla la duración del semáforo en verde en una intersección vial
utilizando lógica difusa. Las variables consideradas son:
- **Volumen de tráfico vehicular**
- **Tiempo de espera de los vehículos**
- **Densidad peatonal**

El sistema usa el método de defuzzificación **centroide** para obtener un valor numérico óptimo.
""")

# 1. Crear las variables difusas
volumen = ctrl.Antecedent(np.arange(0, 101, 1), 'volumen')
espera = ctrl.Antecedent(np.arange(0, 61, 1), 'espera')
densidad = ctrl.Antecedent(np.arange(0, 101, 1), 'densidad')
verde = ctrl.Consequent(np.arange(0, 121, 1), 'verde')

# 2. Definir conjuntos difusos
volumen['bajo'] = fuzz.trimf(volumen.universe, [0, 0, 40])
volumen['medio'] = fuzz.trimf(volumen.universe, [20, 50, 80])
volumen['alto'] = fuzz.trimf(volumen.universe, [60, 100, 100])

espera['corta'] = fuzz.trimf(espera.universe, [0, 0, 20])
espera['media'] = fuzz.trimf(espera.universe, [10, 30, 50])
espera['larga'] = fuzz.trimf(espera.universe, [40, 60, 60])

densidad['baja'] = fuzz.trimf(densidad.universe, [0, 0, 30])
densidad['media'] = fuzz.trimf(densidad.universe, [20, 50, 80])
densidad['alta'] = fuzz.trimf(densidad.universe, [70, 100, 100])

verde['corta'] = fuzz.trimf(verde.universe, [0, 0, 40])
verde['media'] = fuzz.trimf(verde.universe, [30, 60, 90])
verde['larga'] = fuzz.trimf(verde.universe, [80, 120, 120])

# 3. Definir reglas
reglas = [

    # 🔹 Volumen bajo
    # Espera corta
    ctrl.Rule(volumen['bajo'] & espera['corta'] & densidad['baja'], verde['corta']),
    ctrl.Rule(volumen['bajo'] & espera['corta'] & densidad['media'], verde['corta']),
    ctrl.Rule(volumen['bajo'] & espera['corta'] & densidad['alta'], verde['corta']),

    # Espera media
    ctrl.Rule(volumen['bajo'] & espera['media'] & densidad['baja'], verde['media']),
    ctrl.Rule(volumen['bajo'] & espera['media'] & densidad['media'], verde['media']),
    ctrl.Rule(volumen['bajo'] & espera['media'] & densidad['alta'], verde['media']),  # corregido

    # Espera larga
    ctrl.Rule(volumen['bajo'] & espera['larga'] & densidad['baja'], verde['media']),
    ctrl.Rule(volumen['bajo'] & espera['larga'] & densidad['media'], verde['media']),
    ctrl.Rule(volumen['bajo'] & espera['larga'] & densidad['alta'], verde['media']),


    # 🔸 Volumen medio
    # Espera corta
    ctrl.Rule(volumen['medio'] & espera['corta'] & densidad['baja'], verde['media']),
    ctrl.Rule(volumen['medio'] & espera['corta'] & densidad['media'], verde['media']),
    ctrl.Rule(volumen['medio'] & espera['corta'] & densidad['alta'], verde['corta']),

    # Espera media
    ctrl.Rule(volumen['medio'] & espera['media'] & densidad['baja'], verde['media']),
    ctrl.Rule(volumen['medio'] & espera['media'] & densidad['media'], verde['media']),
    ctrl.Rule(volumen['medio'] & espera['media'] & densidad['alta'], verde['media']),

    # Espera larga
    ctrl.Rule(volumen['medio'] & espera['larga'] & densidad['baja'], verde['larga']),
    ctrl.Rule(volumen['medio'] & espera['larga'] & densidad['media'], verde['larga']),  # sugerido
    ctrl.Rule(volumen['medio'] & espera['larga'] & densidad['alta'], verde['media']),


    # 🔺 Volumen alto
    # Espera corta
    ctrl.Rule(volumen['alto'] & espera['corta'] & densidad['baja'], verde['media']),
    ctrl.Rule(volumen['alto'] & espera['corta'] & densidad['media'], verde['media']),
    ctrl.Rule(volumen['alto'] & espera['corta'] & densidad['alta'], verde['corta']),

    # Espera media
    ctrl.Rule(volumen['alto'] & espera['media'] & densidad['baja'], verde['larga']),
    ctrl.Rule(volumen['alto'] & espera['media'] & densidad['media'], verde['media']),
    ctrl.Rule(volumen['alto'] & espera['media'] & densidad['alta'], verde['media']),

    # Espera larga
    ctrl.Rule(volumen['alto'] & espera['larga'] & densidad['baja'], verde['larga']),
    ctrl.Rule(volumen['alto'] & espera['larga'] & densidad['media'], verde['larga']),
    ctrl.Rule(volumen['alto'] & espera['larga'] & densidad['alta'], verde['larga']),  # corregido
]


# 4. Sistema de control y simulador
sistema = ctrl.ControlSystem(reglas)
simulador = ctrl.ControlSystemSimulation(sistema)

# 5. Entradas del usuario
st.sidebar.header("🔧 Ajustes de Entrada")
v_input = st.sidebar.slider("Volumen de tráfico (%)", 0, 100, 50)
e_input = st.sidebar.slider("Tiempo de espera (segundos)", 0, 60, 30)
d_input = st.sidebar.slider("Densidad peatonal (%)", 0, 100, 50)

simulador.input['volumen'] = v_input
simulador.input['espera'] = e_input
simulador.input['densidad'] = d_input
simulador.compute()
resultado = simulador.output['verde']

# 6. Mostrar resultados
st.subheader("📊 Resultado")
st.markdown(f"""
**Duración óptima del semáforo en verde:** `{resultado:.2f}` segundos

👉 Este valor fue calculado usando el método de defuzzificación **centroide**.
""")

#7 Mostrar gráfico del resultado
st.subheader("🔍 Visualización del resultado difuso")
verde.view(sim=simulador)  # Esto genera la figura internamente
fig = plt.gcf()            # Captura la figura actual de matplotlib
st.pyplot(fig)             # Muestra la figura en Streamlit


# 8. Explicación adicional opcional
with st.expander("📖 Ver explicación del sistema"):
    st.markdown("""
    - **Lógica difusa**: Permite manejar la incertidumbre en las entradas del sistema.
    - **Método centroide**: Calcula la media ponderada del área bajo la curva resultante.
    - **Reglas difusas**: Definidas para evaluar combinaciones de volumen, espera y densidad.
    """)

with st.expander("📜 Mostrar reglas del sistema"):
    for idx, r in enumerate(reglas, 1):
        st.markdown(f"**Regla {idx}:** {r}")