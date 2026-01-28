from collections import deque
import random
import time

def bfs(graph, start):
    """
    Breadth-First Search (BFS) - Parcours en largeur.
    
    Args:
        graph (dict): Représentation du graphe sous forme de dictionnaire d'adjacence
        start: Nœud de départ
        
    Returns:
        tuple: (visited, distance, parent) - Nœuds visités, distances depuis le départ, parents
    """
    visited = {node: False for node in graph}
    distance = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}

    queue = deque([start])
    visited[start] = True
    distance[start] = 0

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 1
                parent[neighbor] = node
                queue.append(neighbor)
    return visited, distance, parent

def dfs_iterative(graph, start):
    """
    Depth-First Search (DFS) - Parcours en profondeur (version itérative).
    
    Args:
        graph (dict): Représentation du graphe sous forme de dictionnaire d'adjacence
        start: Nœud de départ
        
    Returns:
        dict: Dictionnaire des nœuds visités
    """
    visited = {node: False for node in graph}
    stack = [start]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for neighbor in reversed(graph[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)
    return visited

def generate_random_graph(n, p=0.01):
    """
    Génère un graphe aléatoire avec n nœuds.
    
    Args:
        n (int): Nombre de nœuds
        p (float): Probabilité qu'une arête existe entre deux nœuds (default: 0.01)
        
    Returns:
        dict: Graphe repré
    """
    Mesure et compare les performances de BFS et DFS sur des graphes de différentes tailles.
    
    Returns:
        tuple: (sizes, bfs_times, dfs_times) - Tailles des graphes et temps d'exécution
    """senté sous forme de dictionnaire d'adjacence
    """
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                graph[i].append(j)
                graph[j].append(i)
    return graph

def measure_performance():
    sizes = [100, 500, 1000, 2000, 5000]
    bfs_times = []
    dfs_times = []

    print("Comparaison des performances:")
    print("-" * 60)
    print(f"{'Taille':<10} {'BFS (s)':<12} {'DFS (s)':<12} {'Ratio':<10}")
    print("-" * 60)

    for n in sizes:
        graph = generate_random_graph(n, p=0.01)
        start_time = time.time()
        bfs(graph, 0)
        bfs_time = time.time() - start_time

        start_time = time.time()
        dfs_iterative(graph, 0)
        dfs_time = time.time() - start_time

        bfs_times.append(bfs_time)
        dfs_times.append(dfs_time)
        ratio = bfs_time / dfs_time if dfs_time > 0 else 0

        print(f"{n:<10} {bfs_time:<12.6f} {dfs_time:<12.6f} {ratio:<10.4f}")

    return sizes, bfs_times, dfs_times

if __name__ == "__main__":
    graph_example = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 4, 5],
        3: [1, 4],
        4: [1, 2, 3],
        5: [2]
    }
    visited, distance, parent = bfs(graph_example, 0)
    print("Distances depuis le sommet 0:")
    for node in sorted(distance.keys()):
        print(f"Sommet {node}: distance = {distance[node]}, parent = {parent[node]}")