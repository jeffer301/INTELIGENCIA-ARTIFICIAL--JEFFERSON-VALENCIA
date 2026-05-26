# Investigación: Algoritmos de Búsqueda y Teoría de Juegos

Este proyecto presenta la implementación de algoritmos de búsqueda informada (A*), el estudio de funciones heurísticas avanzadas y modelos estratégicos de la Teoría de Juegos. Mostrando ejemplos de cada uno de estos.

---

## 1. Algoritmo de Búsqueda A* (A-Star)
Es un algoritmo de búsqueda heurística informado, diseñado para encontrar el camino de menor coste en un grafo. A diferencia de BFS, utiliza una **función de costo** para decidir qué camino tomar.

Utiliza la función:  ```f(n) = g(n) + h(n)```

* **```f(n)```**: Costo total estimado. El algoritmo expande primero el nodo con el valor más bajo.
* **```g(n)```**: Costo real acumulado desde el inicio hasta el nodo actual.
* **```h(n)```**: Estimación heurística (distancia estimada hasta el final).



### 🛠️ Características de la Implementación
* **Generación de Laberinto Perfecto:** Implementación de *Recursive Backtracking* para asegurar que el laberinto sea cohesivo, sin áreas encerradas o inaccesibles.
* **Visualización Dinámica:** Animación en tiempo real usando `matplotlib` que muestra el proceso de exploración (nodos visitados) y el trazado final de la ruta óptima.
* **Heurística Manhattan:** Optimizada para movimiento en rejilla de 4 direcciones.

---

## 2. Heurística en Inteligencia Artificial
La heurística es la "brújula" que guía a la IA. Sirve para **reducir drásticamente el espacio de búsqueda**

Esta teoria nos permite encontrar soluciones sin tener que explorar cada posibilidad.

### 🔍 ¿Cómo funciona?
Asigna un valor numérico a cada estado representando una "estimación" del costo restante. 
usamos la formula: 

```d = |x_1 - x_2| + |y_1 - y_2|```

### 🚀 Ejemplos Implementados en Python

* **A. Distancia de Manhattan (8-Puzzle):** Mide la distancia vertical y horizontal absoluta de cada pieza respecto a su destino.
* **B. Distancia de Chebyshev (Movimiento en 8 direcciones):** Ideal para drones o robots que permiten desplazamientos diagonales, calculando el máximo de las diferencias en los ejes ```x``` e ```y```.



---

## 3. Teoría de Juegos
La teoria de juegos analiza la toma de decisiones estratégicas entre múltiples participantes, donde el resultado para cada uno depende de las acciones de los demás.

Esta teoria nos sirve para predecir el comportamiento humano y encontrar la estrategia óptima en escenarios de conflicto o cooperación.

### 🔍 ¿Cómo funciona?

Para que exista un "juego" bajo esta teoría, deben estar presentes estos componentes:

* **Jugadores:** Quienes toman las decisiones (personas, empresas, países).

* **Estrategias:** El conjunto de opciones disponibles para cada jugador.

* **Pagos (Payoffs):** El beneficio o pérdida que recibe cada jugador según la combinación de decisiones tomadas.

* **Reglas:** El marco que define cuándo se mueve cada uno y qué información tienen.


### 🎮 Ejemplos Implementados

* **Dilema del Prisionero:** Explora cómo la traición puede parecer racional incluso cuando la cooperación beneficia a ambos.
* **Halcón-Paloma:** Modela la evolución de estrategias agresivas vs. cooperativas ante un recurso compartido.
* **Equilibrio de Nash:** Estado en el que ningún jugador puede mejorar su ganancia cambiando solo su propia estrategia.

---

## ⚙️ Instalación y Ejecución

1. **Descargar Archivos.py**
2. **Instalar dependencias**: Utilizar Cmd o powershell(con permisos de administrador) utilizando el siguiente codigo
   ```bash
   pip install numpy matplotlib
3. **Ejecutar los archivos.py**


## 📈 Conclusión del Proyecto
Gracias a esta investigacion podemos ver que el algoritmo A* es una de las mejores soluciones que podemos utilzar para explorar grafos, gracias al uso de la heurística.
en la teoria de juegos podemos ver la racionalidad de las personas y predecir cuales podrian ser sus posibles acciones
