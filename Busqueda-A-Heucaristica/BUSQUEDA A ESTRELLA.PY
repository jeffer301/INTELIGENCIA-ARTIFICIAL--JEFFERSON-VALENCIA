import matplotlib.pyplot as plt
import numpy as np
import heapq
import random

# --- CONFIGURACIÓN ---
GRID_SIZE = 15 # Debe ser impar
if GRID_SIZE % 2 == 0: GRID_SIZE += 1

def generar_laberinto_perfecto(w, h):
    maze = np.ones((h, w)) # 1 es muro, 0 es pasillo
    
    def carve(cx, cy):
        maze[cy, cx] = 0
        dirs = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < w and 0 <= ny < h and maze[ny, nx] == 1:
                maze[cy + dy // 2, cx + dx // 2] = 0
                carve(nx, ny)

    # Empezar desde el centro para asegurar expansión
    carve(1, 1)
    
    # --- CONEXIÓN DE INICIO Y META ---
    # Forzamos que el inicio y la meta sean pasillos
    maze[0, 0] = 0
    maze[0, 1] = 0 # Abrir salida del inicio
    maze[h-1, w-1] = 0
    maze[h-1, w-2] = 0 # Abrir entrada a la meta
    
    return maze

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def resolver_a_star(mapa):
    start, goal = (0, 0), (GRID_SIZE - 1, GRID_SIZE - 1)
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    explored = []

    while open_set:
        current = heapq.heappop(open_set)[1]
        explored.append(current)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return True, explored, path[::-1]

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < GRID_SIZE and 0 <= neighbor[1] < GRID_SIZE:
                if mapa[neighbor[0], neighbor[1]] == 1: continue
                
                tentative_g = g_score[current] + 1
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f, neighbor))
    return False, explored, []

# --- EJECUCIÓN ---
grid = generar_laberinto_perfecto(GRID_SIZE, GRID_SIZE)
exito, historial, camino_final = resolver_a_star(grid)

# --- VISUALIZACIÓN ANIMADA ---
plt.ion()
fig, ax = plt.subplots(figsize=(8, 8))

# Copia para no arruinar el mapa original con colores de progreso
viz_grid = np.copy(grid)

for paso in historial:
    if paso != (0,0) and paso != (GRID_SIZE-1, GRID_SIZE-1):
        viz_grid[paso[0], paso[1]] = 0.5 # Color de exploración
    ax.clear()
    # Usamos 'inferno' o 'magma' para que el inicio y fin se vean claros
    ax.imshow(viz_grid, cmap='magma') 
    ax.set_title("A* Navegando Laberinto")
    plt.draw()
    plt.pause(0.005)

# Dibujar el camino final en un color resaltado
for p in camino_final:
    viz_grid[p[0], p[1]] = 0.8
ax.clear()
ax.imshow(viz_grid, cmap='magma')
ax.set_title("¡Ruta Óptima Encontrada!")
plt.ioff()
plt.show()