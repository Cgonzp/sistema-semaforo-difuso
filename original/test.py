import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

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

# 3. Definir reglas difusas
# Reglas completas (27 en total)
reglas = [
    # Volumen bajo
    ctrl.Rule(volumen['bajo'] & espera['corta'] & densidad['baja'], verde['corta']),
    ctrl.Rule(volumen['bajo'] & espera['corta'] & densidad['media'], verde['corta']),
    ctrl.Rule(volumen['bajo'] & espera['corta'] & densidad['alta'], verde['corta']),
    ctrl.Rule(volumen['bajo'] & espera['media'] & densidad['baja'], verde['media']),
    ctrl.Rule(volumen['bajo'] & espera['media'] & densidad['media'], verde['media']),
    ctrl.Rule(volumen['bajo'] & espera['media'] & densidad['alta'], verde['corta']),
    ctrl.Rule(volumen['bajo'] & espera['larga'] & densidad['baja'], verde['media']),
    ctrl.Rule(volumen['bajo'] & espera['larga'] & densidad['media'], verde['media']),
    ctrl.Rule(volumen['bajo'] & espera['larga'] & densidad['alta'], verde['media']),

    # Volumen medio
    ctrl.Rule(volumen['medio'] & espera['corta'] & densidad['baja'], verde['media']),
    ctrl.Rule(volumen['medio'] & espera['corta'] & densidad['media'], verde['media']),
    ctrl.Rule(volumen['medio'] & espera['corta'] & densidad['alta'], verde['corta']),
    ctrl.Rule(volumen['medio'] & espera['media'] & densidad['baja'], verde['media']),
    ctrl.Rule(volumen['medio'] & espera['media'] & densidad['media'], verde['media']),
    ctrl.Rule(volumen['medio'] & espera['media'] & densidad['alta'], verde['media']),
    ctrl.Rule(volumen['medio'] & espera['larga'] & densidad['baja'], verde['larga']),
    ctrl.Rule(volumen['medio'] & espera['larga'] & densidad['media'], verde['media']),
    ctrl.Rule(volumen['medio'] & espera['larga'] & densidad['alta'], verde['media']),

    # Volumen alto
    ctrl.Rule(volumen['alto'] & espera['corta'] & densidad['baja'], verde['media']),
    ctrl.Rule(volumen['alto'] & espera['corta'] & densidad['media'], verde['media']),
    ctrl.Rule(volumen['alto'] & espera['corta'] & densidad['alta'], verde['corta']),
    ctrl.Rule(volumen['alto'] & espera['media'] & densidad['baja'], verde['larga']),
    ctrl.Rule(volumen['alto'] & espera['media'] & densidad['media'], verde['media']),
    ctrl.Rule(volumen['alto'] & espera['media'] & densidad['alta'], verde['media']),
    ctrl.Rule(volumen['alto'] & espera['larga'] & densidad['baja'], verde['larga']),
    ctrl.Rule(volumen['alto'] & espera['larga'] & densidad['media'], verde['larga']),
    ctrl.Rule(volumen['alto'] & espera['larga'] & densidad['alta'], verde['media']),
]


# 4. Crear el sistema de control
controlador = ctrl.ControlSystem(reglas)
simulador = ctrl.ControlSystemSimulation(controlador)

# 5. Asignar valores de entrada
simulador.input['volumen'] = 20
simulador.input['espera'] = 25
simulador.input['densidad'] = 40

# 6. Calcular la salida
simulador.compute()

# 7. Mostrar resultado exacto del método 'centroid'
resultado = simulador.output['verde']
print(f"\n📌 Duración óptima del semáforo en verde: {resultado:.2f} segundos")
print("👉 Este valor fue calculado mediante el método de defuzzificación 'centroid' (centroide).")

# 8. Visualización gráfica
verde.view(sim=simulador)
plt.show()
