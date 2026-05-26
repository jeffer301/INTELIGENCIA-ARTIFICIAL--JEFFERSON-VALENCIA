# 📊 Análisis de Datos Estructurados y Data Wrangling con Pandas

## 📝 Descripción del Proyecto
Este módulo de desarrollo e investigación se enfoca en el uso de la librería **Pandas** como el estándar de la industria para el preprocesamiento, limpieza y manipulación de datos (*Data Wrangling*). El proyecto simula el ecosistema financiero y logístico de una tienda de tecnología utilizando variables sintéticas aleatorias controladas, aplicando técnicas de optimización mediante operaciones vectorizadas.

El desarrollo completo e interactivo se encuentra alojado en Google Colab, completamente integrado con este repositorio.
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jeffer301/actividad-panda/blob/main/Panda.ipynb)

## 🛠️ Stack Tecnológico Utilizado
* **Lenguaje:** Python 3.10+
* **Ecosistema Core:** * `Pandas` (Estructuras de datos bidimensionales y manipulación tabular)
    * `NumPy` (Generación de arreglos matriciales y simulación estocástica de datos)
* **Entorno de Desarrollo:** Jupyter Notebook / Google Colab cloud environment

---

## 🎯 Objetivos del Módulo
1.  **Abstracción de Datos:** Dominar las estructuras core de Pandas (`Series` y `DataFrames`) para modelar flujos de información del mundo real.
2.  **Optimización Vectorizada:** Reemplazar los ciclos imperativos iterativos tradicionales (`for`, `while`) por lógica vectorizada nativa, reduciendo drásticamente la complejidad computacional.
3.  **Pipeline de IA:** Comprender el rol crítico del formateo de datos y el manejo de valores nulos (`NaN`) en la fase de ingeniería de características (*Feature Engineering*) antes del entrenamiento de algoritmos de Machine Learning.

---

## 📚 Marco Teórico y Temas Investigados

### 1. Arquitectura de la Librería Pandas
Pandas es una librería open-source construida sobre **NumPy**, lo que significa que hereda su velocidad gracias al almacenamiento de datos en bloques de memoria contiguos y operaciones en código C compilado. 

### 2. Estructuras Core
* **Series:** Arreglos unidimensionales homogéneos con indexación explícita.
* **DataFrame:** Estructuras bidimensionales heterogéneas (tablas), compuestas por múltiples Series que comparten un mismo índice.

### 3. Operaciones Vectorizadas
A diferencia de los lenguajes tradicionales que recorren las matrices celda por celda, Pandas utiliza operaciones en paralelo (SIMD - Single Instruction, Multiple Data). Esto permite aplicar una función o cálculo matemático a una columna de millones de registros de manera simultánea.

### 4. El Rol de Pandas en la Inteligencia Artificial
En el ciclo de vida de un modelo de IA, el **80% del tiempo se consume en la limpieza de datos**. Pandas es la herramienta estándar para:
* **Tratamiento de Valores Nulos:** Identificación, eliminación o imputación de datos faltantes (`NaN`) mediante técnicas estadísticas (como el método `.fillna()`).
* **Codificación de Variables:** Transformación de datos categóricos (texto) a numéricos.
* **Normalización:** Escalamiento de rangos numéricos para evitar sesgos en algoritmos de redes neuronales.

---

## ⚙️ Arquitectura del Script Técnico
El desarrollo práctico (`Panda.ipynb`) ejecuta de manera secuencial los siguientes componentes lógicos:

* **Pipeline 1: Pipeline de Datos Sintéticos:** Estructuración de un diccionario dinámico combinando tipos de datos escalares, listas nativas y arreglos de distribución aleatoria de NumPy (`np.random.randint`) para simular la demanda de productos de hardware.
* **Pipeline 2: Tratamiento de Valores Faltantes:** Inserción intencional de datos nulos (`np.nan`) para demostrar el uso de filtros y reemplazo asíncrono de registros corruptos en inventario.
* **Pipeline 3: Lógica Aritmética Vectorizada:** Multiplicación matemática directa entre las series de `Precio_Unitario_USD` y `Cantidad_Vendida` para generar métricas financieras de rendimiento en tiempo de ejecución.
* **Pipeline 4: Ingesta de Datos Externos:** Simulación de consumo de bases de datos mediante la lectura de un flujo plano a través del motor `pd.read_csv`.

---

## 📊 Resultados y Outputs Obtenidos

A continuación se detallan las estructuras resultantes impresas por el intérprete:

### Matriz Base Generada de Forma Sintética:
<img width="1150" height="653" alt="image" src="https://github.com/user-attachments/assets/6532ee21-0766-43af-982e-155a11b7cf28" />

---

## 💡 Conclusiones Técnicas
* **Rendimiento a Escala:** La eliminación de bucles estructurados en Python para el cálculo de variables financieras nos ayuda a optimizar el uso de CPU y memoria RAM, permitiendo escalar el script a DataSets de nivel Enterprise.
* **Consistencia de Datos:** El manejo controlado de valores nulos mediante Pandas previene que los "pipelines" de Inteligencia Artificial sufran fallos de desbordamiento de memoria o asimetrías matemáticas durante el entrenamiento.
* **Interoperabilidad:** La versatilidad de la librería para mutar datos desde estructuras nativas de Python hasta formatos portables de archivos (`.csv`, `.json`, SQL) la convierten en el puente perfecto entre el Backend de software y los motores de analítica de datos.

---------------------------------------
## 👥 contribución

Este proyecto fue desarrollado íntegramente por:
* **Jefferson Manuel Valencia Riascos** - *Desarrollador Principal*
  
Si tienes alguna sugerencia o encontraste un error, puedes abrir un **Issue** en este repositorio.

## 📄 licencia

Este proyecto está bajo la **Licencia MIT**.
Cualquier persona puede usar, copiar y modificar este código, siempre que se mantenga la atribución al autor original.
