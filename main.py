import sys
from collections import defaultdict

def find_hamiltonian_path(graph, n):
    def backtrack(path, visited):
        if len(path) == n:
            return True
        last = path[-1]
        for neighbor in graph[last]:
            if neighbor not in visited:
                path.append(neighbor)
                visited.add(neighbor)
                if backtrack(path, visited):
                    return True
                path.pop()
                visited.remove(neighbor)
        return False

    for start in range(n):
        path = [start]
        visited = set([start])
        if backtrack(path, visited):
            return path
    return None

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    d = int(input_data[idx]); idx += 1  # 0 for undirected, 1 for directed
    graph = defaultdict(list)
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        graph[u].append(v)
        if d == 0:  # undirected
            graph[v].append(u)
    path = find_hamiltonian_path(graph, n)
    if path:
        print(' '.join(map(str, path)))
    else:
        print('Não existe caminho Hamiltoniano')
    return graph, n, path, d

if __name__ == "__main__":
    graph, n, path, d = main()
    # A visualização do grafo agora deve ser feita pelo arquivo view.py


