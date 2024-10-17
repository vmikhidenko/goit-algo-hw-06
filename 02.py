import networkx as nx
import matplotlib.pyplot as plt

# Створення графа (з першого завдання)
G = nx.Graph()

# Визначення станцій кожної лінії
red_line = ['Akademmistechko', 'Zhytomyrska', 'Sviatoshyn', 'Nyvky', 'Beresteiska', 'Shuliavska',
            'Polytekhnichnyi Instytut', 'Vokzalna', 'Universytet', 'Teatralna', 'Khreshchatyk',
            'Arsenalna', 'Dnipro', 'Hydropark', 'Livoberezhna', 'Darnytsia', 'Chernihivska', 'Lisova']

blue_line = ['Heroiv Dnipra', 'Minska', 'Obolon', 'Pochaina', 'Tarasa Shevchenka', 'Kontraktova Ploshcha',
             'Poshtova Ploshcha', 'Maidan Nezalezhnosti', 'Ploshcha Lva Tolstoho', 'Olimpiiska',
             'Palats "Ukrayina"', 'Lybidska', 'Demiivska', 'Holosiivska', 'Vasylkivska',
             'Vystavkovyi Tsentr', 'Ipodrom', 'Teremky']

green_line = ['Syrets', 'Dorohozhychi', 'Lukianivska', 'Zoloti Vorota', 'Palats Sportu', 'Klovska',
              'Pecherska', 'Druzhby Narodiv', 'Vydubychi', 'Slavutych', 'Osokorky', 'Pozniaky',
              'Kharkivska', 'Vyrlytsia', 'Boryspilska', 'Chervonyi Khutir']

# Додавання вершин до графа
G.add_nodes_from(red_line)
G.add_nodes_from(blue_line)
G.add_nodes_from(green_line)

# Додавання ребер між станціями
G.add_edges_from([(red_line[i], red_line[i+1]) for i in range(len(red_line)-1)])
G.add_edges_from([(blue_line[i], blue_line[i+1]) for i in range(len(blue_line)-1)])
G.add_edges_from([(green_line[i], green_line[i+1]) for i in range(len(green_line)-1)])

# Додавання пересадочних вузлів
G.add_edge('Teatralna', 'Zoloti Vorota')  # Пересадка між червоною та зеленою лініями
G.add_edge('Khreshchatyk', 'Maidan Nezalezhnosti')  # Пересадка між червоною та синьою лініями
G.add_edge('Ploshcha Lva Tolstoho', 'Palats Sportu')  # Пересадка між синьою та зеленою лініями

# Реалізація алгоритму DFS
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in set(graph.neighbors(vertex)) - set(path):
                stack.append((neighbor, path + [neighbor]))
    return None

# Реалізація алгоритму BFS
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    visited = set()
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex == goal:
            return path
        visited.add(vertex)
        for neighbor in set(graph.neighbors(vertex)) - set(path):
            queue.append((neighbor, path + [neighbor]))
    return None

# Приклад використання алгоритмів для пошуку шляху між двома станціями
start_station = 'Akademmistechko'
end_station = 'Chervonyi Khutir'

dfs_path = dfs_paths(G, start_station, end_station)
bfs_path = bfs_paths(G, start_station, end_station)

print(f"Шлях DFS від {start_station} до {end_station}:")
print(dfs_path)

print(f"\nШлях BFS від {start_station} до {end_station}:")
print(bfs_path)

# Візуалізація графа та шляхів
def visualize_path(graph, path, title):
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(graph, k=0.3, iterations=50)
    nx.draw_networkx_nodes(graph, pos, node_size=500, node_color='lightblue')
    nx.draw_networkx_edges(graph, pos)
    nx.draw_networkx_labels(graph, pos, font_size=8)
    
    # Підсвічування шляху
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(graph, pos, nodelist=path, node_color='red')
        nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=2)
    
    plt.title(title)
    plt.axis('off')
    plt.show()

print("\nВізуалізація шляху DFS:")
visualize_path(G, dfs_path, "Шлях DFS")

print("Візуалізація шляху BFS:")
visualize_path(G, bfs_path, "Шлях BFS")
