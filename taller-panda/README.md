<div align="center">

# 🐼 Taller Práctico de Pandas y Operaciones Matemáticas

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jeffer301/INTELIGENCIA-ARTIFICIAL--JEFFERSON-VALENCIA/blob/main/taller-panda/taller_pandas.ipynb)

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-2.2.2-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/NumPy-2.0.2-013243?style=for-the-badge&logo=numpy&logoColor=white"/>
<img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white"/>

**Taller de Inteligencia Artificial — Corte II**  
Programa de Ingeniería de Sistemas · Universidad del Pacífico · Semestre 8

</div>

---

## 👥 Integrantes

| Nombre |
|--------|
| Jefferson Manuel Valencia Riascos |
| Isnildo Equia Perteaga |
| Sebastian Rojas Cabrera |
| Yeison Stiven Lozano Angulo |

---

## 📋 Tabla de Contenidos

- [🎯 Objetivo](#-objetivo)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [🗃️ Dataset](#️-dataset)
- [🔍 Descripción del Taller](#-descripción-del-taller)
- [▶️ Cómo Ejecutar](#️-cómo-ejecutar)
- [📊 Columnas Generadas](#-columnas-generadas)

---

## 🎯 Objetivo

Aplicar los conceptos fundamentales de **análisis de datos** utilizando la librería **Pandas** en Python, ejecutando operaciones matemáticas, estadísticas y manipulación de columnas sobre un dataset de productos tecnológicos.

---

## 📁 Estructura del Proyecto

```
taller-panda/
│
├── 📓 taller_pandas.ipynb   # Notebook principal con la solución completa
├── 📄 productos.csv         # Dataset fuente con los 60 productos
└── 📄 README.md             # Este archivo
```

---

## 🗃️ Dataset

El dataset contiene **60 productos** (tecnología y oficina) y se carga directamente desde GitHub:

```python
url = 'https://raw.githubusercontent.com/jeffer301/INTELIGENCIA-ARTIFICIAL--JEFFERSON-VALENCIA/refs/heads/main/taller-panda/productos.csv'
df = pd.read_csv(url, encoding='utf-8-sig')
```

No es necesario descargar ni subir ningún archivo — el notebook lo importa automáticamente desde este repositorio.

### Columnas originales

| Columna | Tipo | Descripción |
|---------|------|-------------|
| `Producto` | `object` | Nombre del producto |
| `Precio` | `int64` | Precio unitario en COP |
| `Cantidad` | `int64` | Unidades en inventario |
| `Costo_Envio` | `int64` | Costo de envío en COP |
| `Categoria` | `object` | Tecnología / Oficina |

---

## 🔍 Descripción del Taller

### Punto 1 — Creación y Exploración del DataFrame
Se carga el dataset y se explora su estructura con `head()`, `tail()`, `dtypes`, `shape` y `describe()` para entender la distribución y tipos de datos.

### Punto 2 — Operaciones Matemáticas entre Columnas
Se calculan dos nuevas columnas:
```python
df['Total_Venta'] = df['Precio'] * df['Cantidad']
df['Costo_Total'] = df['Total_Venta'] + df['Costo_Envio']
```
Se identifican los productos con mayor y menor venta, y se calcula el promedio general.

### Punto 3 — Porcentajes y Análisis
Se generan indicadores financieros y se analiza la participación de cada producto en el total de ventas:
```python
df['IVA']               = df['Total_Venta'] * 0.19
df['Ganancia_Estimada'] = df['Total_Venta'] * 0.25
df['Perdida_Estimada']  = df['Total_Venta'] * 0.0005
df['Porcentaje_Ventas'] = (df['Total_Venta'] / df['Total_Venta'].sum()) * 100
```

### Punto 4 — Estadística Descriptiva
Se calculan las medidas de tendencia central y dispersión:

| Medida | Columna | Qué indica |
|--------|---------|-----------|
| Media, Mediana, Moda | `Precio` | Comportamiento del precio en el catálogo |
| Desviación estándar | `Cantidad` | Qué tan desbalanceado está el inventario |
| Máximo y mínimo | `Total_Venta` | Rango de desempeño entre productos |

### Punto 5 — Filtrado
```python
# Solo productos de tecnología
df[df['Categoria'] == 'Tecnología']

# Ranking de mayor a menor venta
df.sort_values('Total_Venta', ascending=False)
```

### 🌟 Punto Adicional — Exportar a Excel
```python
df_final.to_excel('resultados_taller_pandas.xlsx', index=False, sheet_name='Análisis de Productos')
```

---

## ▶️ Cómo Ejecutar

La forma más rápida es hacer clic en el badge de arriba **Open in Colab**. El notebook carga el dataset automáticamente desde GitHub, sin necesidad de subir ningún archivo.

También puedes clonarlo localmente:

```bash
git clone https://github.com/jeffer301/INTELIGENCIA-ARTIFICIAL--JEFFERSON-VALENCIA.git
cd INTELIGENCIA-ARTIFICIAL--JEFFERSON-VALENCIA/taller-panda
pip install pandas numpy openpyxl jupyter
jupyter notebook taller_pandas.ipynb
```

---

## 📊 Columnas Generadas

Al finalizar el notebook el DataFrame tendrá **11 columnas**:

| Columna | Fórmula |
|---------|---------|
| `Total_Venta` | `Precio × Cantidad` |
| `Costo_Total` | `Total_Venta + Costo_Envio` |
| `IVA` | `Total_Venta × 0.19` |
| `Ganancia_Estimada` | `Total_Venta × 0.25` |
| `Perdida_Estimada` | `Total_Venta × 0.0005` |
| `Porcentaje_Ventas` | `(Total_Venta / Total) × 100` |

---

<div align="center">

**Universidad del Pacífico · Ingeniería de Sistemas · 2026**

</div>
