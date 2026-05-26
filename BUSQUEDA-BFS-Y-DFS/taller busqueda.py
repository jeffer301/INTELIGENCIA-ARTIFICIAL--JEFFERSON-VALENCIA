import time
import queue
import networkx as nx
import matplotlib.pyplot as plt
import psutil
import os

#crea la logica de la busqueda BFS

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


# crea la logica de la busqueda DFS

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

def generate_connected_random_graph(n, m):
    while True:
        G = nx.gnm_random_graph(n, m)
        if nx.is_connected(G):
            return G

def get_memory_usage():
    # Obtiene el uso de memoria en MB del proceso actual
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024

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

# genera los grafos de manera random
G = generate_connected_random_graph(30, 30)
pos = nx.spring_layout(G)


bfs_order = order_bfs(G, start_node=0)
dfs_order = order_dfs(G, start_node=0)



visualize_searches(bfs_order, dfs_order, G, pos, title1='BFS visualization', title2='DFS visualization', pause_time=0.5)
