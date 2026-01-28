from bfs_dfs import measure_performance
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
