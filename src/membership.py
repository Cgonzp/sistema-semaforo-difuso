import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def build_variables():
    """
    Construye las variables difusas del sistema de semáforo
    y define sus funciones de pertenencia.
    """

    # ==============================
    # 1. Variables difusas
    # ==============================

    volumen = ctrl.Antecedent(np.arange(0, 101, 1), "volumen")
    espera = ctrl.Antecedent(np.arange(0, 61, 1), "espera")
    densidad = ctrl.Antecedent(np.arange(0, 101, 1), "densidad")
    verde = ctrl.Consequent(np.arange(0, 121, 1), "verde")

    # ==============================
    # 2. Funciones de pertenencia
    # ==============================

    # Volumen vehicular
    volumen["bajo"] = fuzz.trimf(volumen.universe, [0, 0, 40])
    volumen["medio"] = fuzz.trimf(volumen.universe, [20, 50, 80])
    volumen["alto"] = fuzz.trimf(volumen.universe, [60, 100, 100])

    # Tiempo de espera
    espera["corta"] = fuzz.trimf(espera.universe, [0, 0, 20])
    espera["media"] = fuzz.trimf(espera.universe, [10, 30, 50])
    espera["larga"] = fuzz.trimf(espera.universe, [40, 60, 60])

    # Densidad peatonal
    densidad["baja"] = fuzz.trimf(densidad.universe, [0, 0, 30])
    densidad["media"] = fuzz.trimf(densidad.universe, [20, 50, 80])
    densidad["alta"] = fuzz.trimf(densidad.universe, [70, 100, 100])

    # Tiempo de luz verde
    verde["corta"] = fuzz.trimf(verde.universe, [0, 0, 40])
    verde["media"] = fuzz.trimf(verde.universe, [30, 60, 90])
    verde["larga"] = fuzz.trimf(verde.universe, [80, 120, 120])

    # ==============================
    # 3. Retornar las variables
    # ==============================

    return {
        "volumen": volumen,
        "espera": espera,
        "densidad": densidad,
        "verde": verde,
    }