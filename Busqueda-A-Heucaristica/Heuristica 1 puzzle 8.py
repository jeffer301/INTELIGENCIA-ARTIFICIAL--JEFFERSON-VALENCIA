import random
import heapq

# Estado objetivo definido por el usuario
GOAL = [1, 2, 3, 4, 5, 6, 7, 8, 0] # 0 representa el espacio vacío

def get_manhattan_distance(state):
    """Calcula la distancia de Manhattan total del estado actual."""
    distance = 0
    for i, value in enumerate(state):
        if value != 0:
            target_idx = GOAL.index(value)
            curr_row, curr_col = divmod(i, 3)
            target_row, target_col = divmod(target_idx, 3)
            distance += abs(curr_row - target_row) + abs(curr_col - target_col)
    return distance

def get_neighbors(state):
    """Genera los posibles movimientos desde el estado actual."""
    neighbors = []
    blank_idx = state.index(0)
    row, col = divmod(blank_idx, 3)
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Arriba, Abajo, Izquierda, Derecha
    
    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_state = list(state)
            target_idx = r * 3 + c
            new_state[blank_idx], new_state[target_idx] = new_state[target_idx], new_state[blank_idx]
            neighbors.append(tuple(new_state))
    return neighbors

def is_solvable(state):
    """Verifica si un puzzle aleatorio tiene solución (basado en inversiones)."""
    inversions = 0
    flat_state = [n for n in state if n != 0]
    for i in range(len(flat_state)):
        for j in range(i + 1, len(flat_state)):
            if flat_state[i] > flat_state[j]:
                inversions += 1
    return inversions % 2 == 0

def print_board(state):
    """Imprime el tablero de forma legible."""
    for i in range(0, 9, 3):
        row = [str(x) if x != 0 else " " for x in state[i:i+3]]
        print(f"| {' | '.join(row)} |")
    print("-" * 13)

def solve():
    # Generar un estado inicial aleatorio que sea soluble
    start_state = list(GOAL)
    random.shuffle(start_state)
    while not is_solvable(start_state) or start_state == GOAL:
        random.shuffle(start_state)
    
    start_state = tuple(start_state)
    
    # A* Algorithm: (prioridad, g_cost, estado, camino)
    queue = [(get_manhattan_distance(start_state), 0, start_state, [])]
    visited = {start_state: 0}
    
    print("--- ESTADO INICIAL ---")
    print_board(start_state)
    
    while queue:
        _, g_cost, current_state, path = heapq.heappop(queue)
        
        if current_state == tuple(GOAL):
            print(f"¡Solucionado en {len(path)} pasos!\n")
            for i, step in enumerate(path):
                print(f"Paso {i+1}:")
                print_board(step)
            print("--- OBJETIVO ALCANZADO ---")
            return

        for neighbor in get_neighbors(current_state):
            new_g_cost = g_cost + 1
            if neighbor not in visited or new_g_cost < visited[neighbor]:
                visited[neighbor] = new_g_cost
                f_cost = new_g_cost + get_manhattan_distance(neighbor)
                heapq.heappush(queue, (f_cost, new_g_cost, neighbor, path + [neighbor]))

if __name__ == "__main__":
    solve()