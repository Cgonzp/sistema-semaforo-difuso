
import matplotlib.pyplot as plt


def plot_membership(variable, input_value=None):
    """
    Genera el gráfico de las funciones de pertenencia
    de una variable difusa.
    """

    fig, ax = plt.subplots(figsize=(8, 4))

    for term_name, term in variable.terms.items():
        ax.plot(
            variable.universe,
            term.mf,
            label=term_name,
            linewidth=2
        )

    if input_value is not None:
        ax.axvline(
            input_value,
            linestyle="--",
            linewidth=2,
            label=f"Valor ingresado: {input_value}"
        )

    ax.set_title(f"Funciones de pertenencia: {variable.label}")
    ax.set_xlabel("Valor")
    ax.set_ylabel("Grado de pertenencia")
    ax.set_ylim(-0.05, 1.05)
    ax.grid(alpha=0.3)
    ax.legend()

    fig.tight_layout()

    return fig
