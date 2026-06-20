# Taller Práctico No. 4 — Librerías NumPy, Matplotlib y Seaborn

**Universidad del Pacífico — Programa de Ingeniería de Sistemas**
**Asignatura: Inteligencia Artificial — Semestre 8, corte II**
**Caso de estudio seleccionado: CASO 2 — Control de Calidad en una Planta de Producción**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jeffer301/INTELIGENCIA-ARTIFICIAL--JEFFERSON-VALENCIA/blob/main/taller_practico_librerias_numpy_matplotlib_seaborn/Taller_NumPy_Matplotlib_Seaborn.ipynb)
[![Ver Notebook en GitHub](https://img.shields.io/badge/GitHub-Ver%20Notebook-181717?style=flat&logo=github&logoColor=white)](https://github.com/jeffer301/INTELIGENCIA-ARTIFICIAL--JEFFERSON-VALENCIA/blob/main/taller_practico_librerias_numpy_matplotlib_seaborn/Taller_NumPy_Matplotlib_Seaborn.ipynb)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat)
![Seaborn](https://img.shields.io/badge/Seaborn-65A6CE?style=flat)

> 🔗 **Abrir y ejecutar el taller directamente:** haz clic en el botón **"Open In Colab"** de arriba
> para correr el notebook en la nube, sin instalar nada en tu computador.

## 👥 Integrantes

| Nombre |
|--------|
| Jefferson Manuel Valencia Riascos |
| Isnildo Equia Perteaga |
| Sebastian Rojas Cabrera |
| Yeison Stiven Lozano Angulo |

## 1. Contexto

Una empresa manufacturera produce piezas metálicas y desea analizar los factores que influyen en
los defectos de fabricación, con el fin de ajustar sus parámetros de producción y reducir el
porcentaje de piezas defectuosas.

## 2. Generación de Datos Sintéticos

Se generó un dataset sintético de **500 registros** utilizando `numpy.random` (semilla fija
`np.random.seed(42)` para reproducibilidad), con las siguientes variables:

| Variable | Tipo | Generación |
|---|---|---|
| Temperatura de Producción | Numérica | `np.random.normal(180, 15, n)` — valor óptimo ≈180°C |
| Presión de Máquina | Numérica | `np.random.normal(50, 8, n)` — valor óptimo ≈50 psi |
| Tiempo de Operación | Numérica | `np.random.uniform(1, 12, n)` horas |
| Velocidad de Producción | Numérica | `np.random.normal(100, 20, n)` — valor óptimo ≈100 u/h |
| Defectuosa | Categórica (Sí/No) | Probabilidad condicionada a la desviación de temperatura y velocidad respecto a su valor óptimo |

El código completo de generación está en la sección 3 del notebook (`Taller_NumPy_Matplotlib_Seaborn.ipynb`).

## 3. Análisis Estadístico

Se calcularon, para cada variable numérica: **media, mediana, moda, desviación estándar, varianza,
mínimo y máximo**, usando NumPy/SciPy. La temperatura promedio resulta cercana a 180°C, confirmando
que el proceso opera en torno al punto óptimo, y su dispersión (desviación estándar) explica buena
parte de la variabilidad en la calidad de las piezas.

## 4. Visualización de Datos 

El notebook incluye **7 visualizaciones**, cada una con su interpretación:

1. Histograma de temperatura de producción.
2. Histograma de presión de máquina.
3. Gráfico de barras de piezas defectuosas vs. sanas.
4. Heatmap de correlación (Seaborn).
5. Boxplot de temperatura.
6. Pairplot de variables coloreado por condición de la pieza (Seaborn).
7. Boxplot comparativo de temperatura según defecto.

## 5. Análisis Exploratorio

**Hallazgos:**
- Las piezas defectuosas muestran, en promedio, mayor desviación de temperatura respecto al valor
  óptimo (180°C) que las piezas sanas.
- La velocidad de producción extrema (muy alta o muy baja) también se asocia con mayor proporción
  de defectos.
- La presión y el tiempo de operación, en los rangos generados, no muestran una asociación tan marcada.

**Variable más relevante:** Temperatura de Producción, seguida de Velocidad de Producción.

## 6. Conclusiones

1. Las piezas defectuosas tienden a producirse cuando la temperatura se aleja significativamente
   del valor óptimo de operación.
2. La velocidad de producción extrema también está asociada con un mayor porcentaje de defectos.
3. La presión de máquina, dentro del rango analizado, no muestra una relación tan clara con la
   aparición de defectos.
4. Existen valores atípicos de temperatura que coinciden con los lotes de mayor tasa de defectos,
   sugiriendo fallos puntuales del proceso o de calibración.
5. El control simultáneo de temperatura y velocidad parece ser más efectivo para reducir defectos
   que el control aislado de una sola variable.

## 7. Recomendaciones Empresariales

1. Implementar un sistema de monitoreo en tiempo real de temperatura y velocidad, con alertas
   cuando se alejen del rango óptimo.
2. Revisar y calibrar periódicamente las máquinas asociadas a los lotes con temperaturas atípicas.
3. Establecer rangos de control estadístico de proceso (SPC) para temperatura y velocidad,
   deteniendo la producción cuando se excedan los límites definidos.

## 8. Reflexión de IA

¿Cómo podrían utilizarse técnicas de Machine Learning o Inteligencia Artificial para automatizar
la toma de decisiones en este caso?

Podríamos entrenar modelos de Inteligencia Artificial dependiendo del método de clasificación
(árboles de decisión, random forest o redes neuronales) que nos interese elegir, para que estos
predigan la probabilidad de que una pieza resulte defectuosa usando los datos de temperatura,
presión, tiempo y velocidad registrados durante su fabricación. Estos modelos podrían activar
alertas automáticas o incluso detener la línea de producción casi en tiempo real cuando se detecte
que se cumplen los parámetros asociados a un alto riesgo de defecto, lo cual reduciría el
desperdicio de materiales y mejoraría la eficiencia del control de calidad.

## 9. Librerías utilizadas

- `numpy` — generación de datos y cálculos estadísticos.
- `pandas` — estructuración de datos en DataFrame.
- `matplotlib` — histogramas, barras, boxplots.
- `seaborn` — heatmap, boxplot, pairplot.
- `scipy.stats` — cálculo de la moda.

## 10. Cómo ejecutar

**Opción 1 — En la nube (recomendado):** haz clic en el badge **Open In Colab** al inicio de este README.

**Opción 2 — Localmente:**
```bash
pip install numpy pandas matplotlib seaborn scipy jupyter
jupyter notebook Taller_NumPy_Matplotlib_Seaborn.ipynb
```
Ejecutar todas las celdas en orden (`Kernel > Restart & Run All`).
