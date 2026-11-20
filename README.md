
# Sistema de Semáforo Inteligente mediante Lógica Difusa

Sistema de control de tráfico desarrollado en Python mediante un modelo de inferencia difusa Mamdani. Permite calcular el tiempo de duración de la luz verde a partir de tres variables de entrada: volumen vehicular, tiempo de espera y densidad peatonal.

## Características

- Modelo de inferencia difusa Mamdani.
- 3 variables de entrada y 1 variable de salida.
- 27 reglas difusas.
- Funciones de pertenencia triangulares.
- Defuzzificación mediante método del centroide.
- Interfaz gráfica interactiva con Streamlit.
- Visualización de funciones de pertenencia.
- Validación de entradas.
- Pruebas automatizadas con Pytest.

## Tecnologías utilizadas

- Python
- NumPy
- SciPy
- Scikit-Fuzzy
- Matplotlib
- Streamlit
- Pytest

## Variables del sistema

| Variable | Tipo | Rango |
|---|---|---|
| Volumen vehicular | Entrada | 0 - 100 |
| Tiempo de espera | Entrada | 0 - 60 |
| Densidad peatonal | Entrada | 0 - 100 |
| Tiempo de luz verde | Salida | 0 - 120 segundos |

## Arquitectura del proyecto

```text
SISTEMA_SEMAFORO_DIFUSO/
├── original/
├── src/
│   ├── membership.py
│   ├── rules.py
│   ├── fuzzy_system.py
│   └── visualization.py
├── tests/
│   └── test_fuzzy_system.py
├── results/
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Instalación

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
cd SISTEMA_SEMAFORO_DIFUSO
```

Crear entorno virtual:

```bash
python -m venv .venv
```

Activar en Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar dependencias:

```bash
python -m pip install -r requirements.txt
```

## Ejecución

Iniciar la aplicación:

```bash
python -m streamlit run app.py
```

La aplicación estará disponible normalmente en:

```text
http://localhost:8501
```

## Pruebas

Ejecutar las pruebas automatizadas:

```bash
python -m pytest -v
```

## Ejemplo de funcionamiento

Entrada:

- Volumen vehicular: 20
- Tiempo de espera: 25
- Densidad peatonal: 40

Resultado:

- Tiempo de luz verde: 60.00 segundos.

## Estado del proyecto

- [x] Implementación de variables difusas.
- [x] Implementación de las 27 reglas.
- [x] Motor de inferencia Mamdani.
- [x] Validación de entradas.
- [x] Interfaz web con Streamlit.
- [x] Visualización de funciones de pertenencia.
- [x] Pruebas automatizadas: 14 aprobadas.
- [ ] Documentación visual.
- [ ] Publicación en GitHub.

## Propósito académico

Proyecto desarrollado con fines educativos para estudiar la aplicación de sistemas expertos y lógica difusa en el control inteligente del tráfico.
