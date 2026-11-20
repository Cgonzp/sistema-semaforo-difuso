from skfuzzy import control as ctrl


def build_rules(variables):
    """
    Construye las 27 reglas difusas del sistema de semáforo.

    Parámetros:
        variables (dict): Diccionario con las variables difusas.

    Retorna:
        list: Lista de reglas difusas.
    """

    # Recuperar variables difusas
    volumen = variables["volumen"]
    espera = variables["espera"]
    densidad = variables["densidad"]
    verde = variables["verde"]

    reglas = [

        # ==========================================
        # VOLUMEN BAJO
        # ==========================================

        ctrl.Rule(
            volumen["bajo"] & espera["corta"] & densidad["baja"],
            verde["corta"]
        ),
        ctrl.Rule(
            volumen["bajo"] & espera["corta"] & densidad["media"],
            verde["corta"]
        ),
        ctrl.Rule(
            volumen["bajo"] & espera["corta"] & densidad["alta"],
            verde["corta"]
        ),
        ctrl.Rule(
            volumen["bajo"] & espera["media"] & densidad["baja"],
            verde["media"]
        ),
        ctrl.Rule(
            volumen["bajo"] & espera["media"] & densidad["media"],
            verde["media"]
        ),
        ctrl.Rule(
            volumen["bajo"] & espera["media"] & densidad["alta"],
            verde["corta"]
        ),
        ctrl.Rule(
            volumen["bajo"] & espera["larga"] & densidad["baja"],
            verde["media"]
        ),
        ctrl.Rule(
            volumen["bajo"] & espera["larga"] & densidad["media"],
            verde["media"]
        ),
        ctrl.Rule(
            volumen["bajo"] & espera["larga"] & densidad["alta"],
            verde["media"]
        ),

        # ==========================================
        # VOLUMEN MEDIO
        # ==========================================

        ctrl.Rule(
            volumen["medio"] & espera["corta"] & densidad["baja"],
            verde["media"]
        ),
        ctrl.Rule(
            volumen["medio"] & espera["corta"] & densidad["media"],
            verde["media"]
        ),
        ctrl.Rule(
            volumen["medio"] & espera["corta"] & densidad["alta"],
            verde["corta"]
        ),
        ctrl.Rule(
            volumen["medio"] & espera["media"] & densidad["baja"],
            verde["media"]
        ),
        ctrl.Rule(
            volumen["medio"] & espera["media"] & densidad["media"],
            verde["media"]
        ),
        ctrl.Rule(
            volumen["medio"] & espera["media"] & densidad["alta"],
            verde["media"]
        ),
        ctrl.Rule(
            volumen["medio"] & espera["larga"] & densidad["baja"],
            verde["larga"]
        ),
        ctrl.Rule(
            volumen["medio"] & espera["larga"] & densidad["media"],
            verde["media"]
        ),
        ctrl.Rule(
            volumen["medio"] & espera["larga"] & densidad["alta"],
            verde["media"]
        ),

        # ==========================================
        # VOLUMEN ALTO
        # ==========================================

        ctrl.Rule(
            volumen["alto"] & espera["corta"] & densidad["baja"],
            verde["media"]
        ),
        ctrl.Rule(
            volumen["alto"] & espera["corta"] & densidad["media"],
            verde["media"]
        ),
        ctrl.Rule(
            volumen["alto"] & espera["corta"] & densidad["alta"],
            verde["corta"]
        ),
        ctrl.Rule(
            volumen["alto"] & espera["media"] & densidad["baja"],
            verde["larga"]
        ),
        ctrl.Rule(
            volumen["alto"] & espera["media"] & densidad["media"],
            verde["media"]
        ),
        ctrl.Rule(
            volumen["alto"] & espera["media"] & densidad["alta"],
            verde["media"]
        ),
        ctrl.Rule(
            volumen["alto"] & espera["larga"] & densidad["baja"],
            verde["larga"]
        ),
        ctrl.Rule(
            volumen["alto"] & espera["larga"] & densidad["media"],
            verde["larga"]
        ),
        ctrl.Rule(
            volumen["alto"] & espera["larga"] & densidad["alta"],
            verde["media"]
        ),
    ]

    return reglas