# Taller No. 3 – Análisis Estadístico Descriptivo

**Universidad del Pacífico · Ingeniería de Sistemas · Inteligencia Artificial**  
**Estudiante:** Jefferson Manuel Valencia Riascos · **Semestre 8 – Corte II**

---

## Descripción

Análisis estadístico descriptivo completo sobre la variable **Apps Descargadas** a partir de una muestra de 50 usuarios de aplicaciones móviles en América Latina.

## Contenido del repositorio

| Archivo / Recurso | Descripción |
|---|---|
| [Tabla de frecuencias (Google Sheets)](https://docs.google.com/spreadsheets/d/1oH3DZo32_JmRHtZ4cB0NrZ3MgNn6TBfQITGUtvLhDaQ/edit?usp=sharing) | Tabla de distribución de frecuencias con fórmulas y 3 gráficos |
| `Taller Tabla de frecuencias Jefferson Valencia.pdf` | Informe técnico – puntos 6 y 7 del taller |

## Resultados principales

| Parámetro | Valor |
|---|---|
| n (observaciones) | 50 |
| Mínimo | 30 |
| Máximo | 132 |
| Rango | 102 |
| Número de clases | 5 (arbitrario) |
| Amplitud de clase | 21 |

### Tabla de frecuencias

| Intervalo | fi | hi | Fi | Hi |
|---|---|---|---|---|
| [30 – 51) | 11 | 22 % | 11 | 22 % |
| [51 – 72) | 10 | 20 % | 21 | 42 % |
| [72 – 93) | **14** | **28 %** | 35 | 70 % |
| [93 – 114) | 10 | 20 % | 45 | 90 % |
| [114 – 135] | 5 | 10 % | 50 | 100 % |

## Gráficos generados (en Google Sheets)

- **Figura 1 – Histograma de frecuencias:** muestra el intervalo modal [72–93) como la barra más alta con fi = 14.
- **Figura 2 – Polígono de frecuencias:** curva unimodal con pico en la marca de clase 82,5 y cola derecha.
- **Figura 3 – Ojiva:** curva acumulada en "S"; el 70 % de los usuarios descarga menos de 93 apps.

## Fórmulas Excel utilizadas

```
Marca de clase:       =(Li + Ls) / 2
fi (absoluta):        =COUNTIFS($D$2:$D$51,">="&Li,$D$2:$D$51,"<"&Ls)
hi (relativa):        =fi / COUNTA($D$2:$D$51)
Fi (acumulada):       =Fi_anterior + fi
Hi (rel. acumulada):  =Fi / COUNTA($D$2:$D$51)
Mínimo:               =MIN($D$2:$D$51)
Máximo:               =MAX($D$2:$D$51)
Rango:                =Máximo - Mínimo
Amplitud:             =ROUNDUP(Rango / k, 0)
```

## Conclusiones clave

- El intervalo **[72–93)** concentra el 28 % de los usuarios (intervalo modal).
- El **70 %** de los usuarios descarga menos de 93 apps.
- Solo el **10 %** supera las 114 apps (perfil de alto consumo minoritario).
- La distribución presenta **asimetría positiva moderada**.
