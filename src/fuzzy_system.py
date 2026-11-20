from skfuzzy import control as ctrl

from src.membership import build_variables
from src.rules import build_rules
import matplotlib.pyplot as plt


class FuzzyTrafficController:
    """
    Controlador de semáforo basado en lógica difusa Mamdani.
    """

    def __init__(self):
        # Construir variables difusas
        self.variables = build_variables()

        # Construir las 27 reglas
        self.rules = build_rules(self.variables)

        # Crear sistema de control
        self.control_system = ctrl.ControlSystem(self.rules)

        # Crear simulador
        self.simulator = ctrl.ControlSystemSimulation(
            self.control_system
        )

    def calculate(self, volume, waiting_time, pedestrian_density):
        """
        Calcula la duración de la luz verde.

        Parámetros:
            volume (float): Volumen vehicular (0-100).
            waiting_time (float): Tiempo de espera (0-60).
            pedestrian_density (float): Densidad peatonal (0-100).

        Retorna:
            float: Duración calculada en segundos.
        """

        # Validar entradas
        self._validate_inputs(
            volume,
            waiting_time,
            pedestrian_density
        )

        # Asignar entradas al simulador
        self.simulator.input["volumen"] = volume
        self.simulator.input["espera"] = waiting_time
        self.simulator.input["densidad"] = pedestrian_density

        # Ejecutar inferencia difusa
        self.simulator.compute()

        # Obtener resultado defuzzificado
        return float(self.simulator.output["verde"])

    @staticmethod
    def _validate_inputs(volume, waiting_time, pedestrian_density):
        """
        Verifica que las entradas sean numéricas, finitas
        y estén dentro de sus respectivos universos.
        """

        inputs = {
            "volumen": (volume, 0, 100),
            "espera": (waiting_time, 0, 60),
            "densidad": (pedestrian_density, 0, 100),
        }

        for name, (value, minimum, maximum) in inputs.items():

            if isinstance(value, bool):
                raise ValueError(
                    f"El valor de {name} debe ser numérico."
                )

            try:
                numeric_value = float(value)
            except (TypeError, ValueError):
                raise ValueError(
                    f"El valor de {name} debe ser numérico."
                ) from None

            if not numeric_value == numeric_value or numeric_value in (
                float("inf"),
                float("-inf")
            ):
                raise ValueError(
                    f"El valor de {name} debe ser finito."
                )

            if not minimum <= numeric_value <= maximum:
                raise ValueError(
                    f"{name} debe estar entre {minimum} y {maximum}."
                )

    
    
def get_output_visualization(self):
    """
    Genera la visualización de la salida difusa,
    incluyendo la agregación de reglas y el centroide.
    """

    output_variable = self.variables["verde"]

    # Visualización nativa de scikit-fuzzy
    output_variable.view(sim=self.simulator)

    fig = plt.gcf()
    fig.tight_layout()

    return fig

