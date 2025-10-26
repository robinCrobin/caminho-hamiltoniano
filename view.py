import sys
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
from main import find_hamiltonian_path

def ler_grafo_stdin():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    d = int(input_data[idx]); idx += 1  # 0 para não orientado, 1 para orientado
    arestas = []
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        arestas.append((u, v))
    return n, m, d, arestas

def construir_grafo(n, arestas, direcionado):
    graph = defaultdict(list)
    for u, v in arestas:
        graph[u].append(v)
        if not direcionado:
            graph[v].append(u)
    return graph

def visualizar_grafo(graph, n, caminho=None, direcionado=False, nome_arquivo='assets/grafo_hamiltoniano.png'):
    G = nx.DiGraph() if direcionado else nx.Graph()
    G.add_nodes_from(range(n))
    for u in graph:
        for v in graph[u]:
            if direcionado or u < v:
                G.add_edge(u, v)
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 6))
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=700)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2, alpha=0.5, edge_color='gray', arrows=direcionado)
    if caminho and len(caminho) > 1:
        caminho_arestas = list(zip(caminho, caminho[1:]))
        nx.draw_networkx_edges(
            G, pos,
            edgelist=caminho_arestas,
            width=3, edge_color='red', style='solid', arrows=direcionado
        )
    plt.title('Grafo e Caminho Hamiltoniano' + ('' if not caminho else '\n(Destacado em vermelho)'))
    plt.axis('off')
    plt.tight_layout()
    import os
    pasta = os.path.dirname(nome_arquivo)
    if pasta and not os.path.exists(pasta):
        os.makedirs(pasta)
    plt.savefig(nome_arquivo, format='png')
    plt.close()

if __name__ == "__main__":
    n, m, d, arestas = ler_grafo_stdin()
    direcionado = (d == 1)
    graph = construir_grafo(n, arestas, direcionado)
    caminho = find_hamiltonian_path(graph, n)
    visualizar_grafo(graph, n, caminho, direcionado=direcionado)
    if caminho:
        print('Caminho Hamiltoniano encontrado:', ' '.join(map(str, caminho)))
    else:
        print('Não existe caminho Hamiltoniano')
    print('Imagem salva em assets/grafo_hamiltoniano.png')
