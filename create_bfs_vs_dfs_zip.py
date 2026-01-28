import os
import zipfile

# Nom du projet
project_name = "BFS_vs_DFS"

# Crée le dossier du projet
if not os.path.exists(project_name):
    os.makedirs(project_name)

# Contenu des fichiers
files_content = {
    "bfs_dfs.py": """from collections import deque
import random
import time

def bfs(graph, start):
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
        print(f"Sommet {node}: distance = {distance[node]}, parent = {parent[node]}")""",

    "example.py": """from bfs_dfs import measure_performance
import matplotlib.pyplot as plt

def main():
    sizes, bfs_times, dfs_times = measure_performance()
    plt.plot(sizes, bfs_times, marker='o', label='BFS')
    plt.plot(sizes, dfs_times, marker='x', label='DFS')
    plt.xlabel('Taille du graphe (nombre de sommets)')
    plt.ylabel('Temps (secondes)')
    plt.title('Comparaison des performances BFS vs DFS')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
""",

    "README.md": """# BFS vs DFS - Comparaison des algorithmes sur graphes aléatoires
Projet Python pour implémenter et comparer BFS et DFS sur des graphes aléatoires.
"""
}

# Crée les fichiers dans le dossier du projet
for filename, content in files_content.items():
    with open(os.path.join(project_name, filename), 'w', encoding='utf-8') as f:
        f.write(content)

# Crée un fichier ZIP
zip_filename = f"{project_name}.zip"
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(project_name):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, '.')
            zipf.write(file_path, arcname)

print(f"✓ Dossier '{project_name}' créé avec succès")
print(f"✓ Fichier ZIP '{zip_filename}' créé avec succès")