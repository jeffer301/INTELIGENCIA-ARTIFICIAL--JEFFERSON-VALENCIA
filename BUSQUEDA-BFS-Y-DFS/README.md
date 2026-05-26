# 🚀 Busqueda DFS yFBS

Este codigo nos permitira visualizar de manera directa la diferencia entre la busqueda DFS y BFS utilizando grafos. Ademas nos permite saber cuanta memoria que utiliza cada busqueda

## 📌 Tabla de Contenidos
- [Instalación](#-instalación)
- [Funcionamiento](#-Funcionamiento)
- [Contribución](#-contribución)
- [Licencia](#-licencia)

## 🛠️ Instalación

Pasos necesarios para poner en marcha el proyecto:

instalar las librerias:
```
pip install networkx matplotlib psutil
```
Ese comando se puede ejecutar en simbolo del sistema(cmd), powershell o desde la terminal de nuestro proyecto en python (en este caso desde la terminal de visual studio code)

### Librerias

NetworkX: Es la herramienta principal ya que nos permite crear, editar y estudiar los grafos

Matplotlib (pyplot): Es una librería de visualización de datos, que nos permite ver una animacion de como funcionan ambas busquedas en los nodos de los grafos

psutil: Se utiliza para acceder a los detalles del sistema y del hardware. Aquí la usamos específicamente para medir cuánta memoria RAM está consumiendo el proceso de Python mientras ejecuta las búsquedas.

### Librerias Estandar

Time: Nos Permite manejar pausas y retardos. La usamos para que la animación no sea instantánea y puedas apreciar el paso a paso de los algoritmos.

Queue: Proporciona una estructura de datos de tipo FIFO (First In, First Out). Es fundamental para la lógica del BFS, ya que permite gestionar el orden de los nodos a visitar.

OS: Sirve para interactuar con el sistema operativo. En este código, la usamos para identificar el ID del proceso actual y así poder medir su consumo de recursos con psutil.


## Funcionamiento

### LOGICA DE LA BUSQUEDA BFS

```
def order_bfs(graph, start_node):
    visited = set()
    q = queue.Queue()
    q.put(start_node)
    order = []

    while not q.empty():
        vertex = q.get()
        if vertex not in visited:
            order.append(vertex)
            visited.add(vertex)
            for node in graph[vertex]:
                if node not in visited:
                    q.put(node)
    return order
```
esta es la logica de la busqueda bfs, donde creamos una lista vacia y seguimos cuales son los nodos que visitamos con anterioridad para que no se repitan.
entonces utilizando "Queue" hacemos que el grafo explore por niveles, visitando primero los nodos vecinos cerca del punto de partida antes de pasar a los nodos que estan mas lejos

### LOGICA DE LA BUSQUEDA DFS

```
def order_dfs(graph, start_node, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []
    if start_node not in visited:
        order.append(start_node)
        visited.add(start_node)
        for node in graph[start_node]:
            if node not in visited:
                order_dfs(graph, node, visited, order)
    return order
```

Las variables "visited"(nodos visitados) y "order"(el historial) se crean vacías la primera vez que llamamos a la función. Hacemos una verificacion sobre los nodos visitados
Esta vez en lugar de explorar los nodos vecinos en una fila, este simplemente comienza a explorar hasta "estrellarse" con el nodo final. Esto recrea el recorrido de un laberinto


Crearemos un grafo random con el siguiente codigo
```
def generate_connected_random_graph(n, m):
    while True:
        G = nx.gnm_random_graph(n, m)
        if nx.is_connected(G):
            return G
```

 (n = nodos, m = aristas)

para la memoria usaremos el comando

```
def get_memory_usage():
    # Obtiene el uso de memoria en MB del proceso actual
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024
```

para la visualizacion de los nodos con colores diferentes para que sea mas facil distinguir DFS y BFS usaremos

```
def visualize_searches(order1, order2, G, pos, title1, title2, pause_time=1.0):
    # Obtenemos la longitud de recorrido más larga para sincronizar los pasos
    max_steps = max(len(order1), len(order2))
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    plt.ion()  # activa el modo interactivo

    for step in range(max_steps):
        axs[0].clear()
        axs[1].clear()
        
        # Obtener memoria actual
        memory_usage = get_memory_usage()
        
        # nodo actual para cada busqueda
        node1 = order1[step] if step < len(order1) else order1[-1]
        node2 = order2[step] if step < len(order2) else order2[-1]

        # crea los arreglos de colores
        node_colors1 = ['r' if n == node1 else 'g' if n in order1[:step+1] else 'lightgray' for n in G.nodes]
        node_colors2 = ['b' if n == node2 else 'g' if n in order2[:step+1] else 'lightgray' for n in G.nodes]

        # Títulos con información de memoria
        axs[0].set_title(f'{title1}\nMemoria: {memory_usage:.2f} MB')
        axs[1].set_title(f'{title2}\nMemoria: {memory_usage:.2f} MB')

        nx.draw(G, pos, with_labels=True, node_color=node_colors1, ax=axs[0])
        nx.draw(G, pos, with_labels=True, node_color=node_colors2, ax=axs[1])

        plt.draw()
        plt.pause(pause_time)
    plt.ioff()
    plt.show()
```


 
## 👥 contribución

Este proyecto fue desarrollado íntegramente por:
* **Jefferson Manuel Valencia Riascos** - *Desarrollador Principal*
* Estudiante de Ingeniería de Sistemas.

Si tienes alguna sugerencia o encontraste un error, puedes abrir un **Issue** en este repositorio.

## 📄 licencia

Este proyecto está bajo la **Licencia MIT**.
Cualquier persona puede usar, copiar y modificar este código, siempre que se mantenga la atribución al autor original.
