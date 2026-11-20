
import streamlit as st
from src.visualization import plot_membership
import matplotlib.pyplot as plt

from src.fuzzy_system import FuzzyTrafficController


# Configuración de la página
st.set_page_config(
    page_title="Sistema de Semáforo Difuso",
    page_icon="🚦",
    layout="wide"
)


# Estilos visuales
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
    }

    .metric-card {
        background-color: #1e2530;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
    }

    div[data-testid="stMetric"] {
        background-color: #1e2530;
        padding: 18px;
        border-radius: 12px;
    }
</style>
""", unsafe_allow_html=True)


# Inicializar controlador
@st.cache_resource
def load_controller():
    return FuzzyTrafficController()


controller = load_controller()


# Encabezado
st.title("🚦 Sistema Inteligente de Semáforo")
st.caption(
    "Control de tráfico mediante lógica difusa Mamdani"
)

st.divider()


# Distribución principal
col_inputs, col_results = st.columns([1, 1])


with col_inputs:
    st.subheader("Parámetros de entrada")

    volume = st.slider(
        "Volumen vehicular",
        min_value=0,
        max_value=100,
        value=20,
        help="Nivel de volumen vehicular."
    )

    waiting_time = st.slider(
        "Tiempo de espera",
        min_value=0,
        max_value=60,
        value=25,
        help="Tiempo de espera acumulado."
    )

    pedestrian_density = st.slider(
        "Densidad peatonal",
        min_value=0,
        max_value=100,
        value=40,
        help="Nivel de densidad peatonal."
    )

    calculate = st.button(
        "Calcular tiempo de luz verde",
        type="primary",
        use_container_width=True
    )


with col_results:
    st.subheader("Resultado del controlador")

    if calculate:
        try:
            green_time = controller.calculate(
                volume,
                waiting_time,
                pedestrian_density
            )

            st.metric(
                label="Tiempo de luz verde",
                value=f"{green_time:.2f} segundos"
            )

            st.success("Cálculo realizado correctamente.")

            st.progress(
                min(green_time / 120, 1.0),
                text="Duración respecto al máximo de 120 segundos"
            )

            st.write("**Entradas procesadas:**")

            st.write(f"- Volumen vehicular: {volume}")
            st.write(f"- Tiempo de espera: {waiting_time}")
            st.write(f"- Densidad peatonal: {pedestrian_density}")

        except (ValueError, RuntimeError) as error:
            st.error(f"Error durante el cálculo: {error}")

    else:
        st.info(
            "Configura los parámetros y presiona el botón "
            "para ejecutar el controlador."
        )


st.divider()

# Información del sistema
st.subheader("Información del modelo")

col1, col2, col3 = st.columns(3)

col1.metric("Entradas", "3")
col2.metric("Reglas difusas", "27")
col3.metric("Salidas", "1")

st.caption(
    "Modelo Mamdani | Defuzzificación por centroide | "
    "Proyecto académico de inteligencia artificial"
)


st.divider()

st.subheader("Visualización de funciones de pertenencia")

if calculate:
    variables_to_plot = [
        ("volumen", volume),
        ("espera", waiting_time),
        ("densidad", pedestrian_density)
    ]

    for variable_name, input_value in variables_to_plot:
        st.markdown(f"#### {variable_name.capitalize()}")

        figure = plot_membership(
            controller.variables[variable_name],
            input_value
        )

        st.pyplot(figure)
        plt.close(figure)
    st.markdown("#### Resultado de la inferencia difusa")

    output_figure = controller.get_output_visualization()

    st.pyplot(output_figure)

    plt.close(output_figure)