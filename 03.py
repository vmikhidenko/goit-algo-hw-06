import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Створення графа (з першого завдання) та додавання ваг
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

# Функція для додавання ребер з вагами
def add_weighted_edges(line_stations, weight=2):
    edges = [(line_stations[i], line_stations[i+1], weight) for i in range(len(line_stations)-1)]
    G.add_weighted_edges_from(edges)

# Додавання ребер з вагами між станціями
add_weighted_edges(red_line)
add_weighted_edges(blue_line)
add_weighted_edges(green_line)

# Додавання пересадочних вузлів з більшими вагами (наприклад, 4 хвилини)
G.add_edge('Teatralna', 'Zoloti Vorota', weight=4)  # Пересадка між червоною та зеленою лініями
G.add_edge('Khreshchatyk', 'Maidan Nezalezhnosti', weight=4)  # Пересадка між червоною та синьою лініями
G.add_edge('Ploshcha Lva Tolstoho', 'Palats Sportu', weight=4)  # Пересадка між синьою та зеленою лініями

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    # Ініціалізація
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_vertices = {vertex: None for vertex in graph.nodes}
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Якщо знайдений більший шлях, пропускаємо
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor in graph.neighbors(current_vertex):
            edge_weight = graph[current_vertex][neighbor]['weight']
            distance = current_distance + edge_weight
            
            # Якщо знайдено коротший шлях до сусіда
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, previous_vertices

# Знаходження найкоротших шляхів між усіма парами вершин
all_shortest_paths = {}
for start_station in G.nodes:
    distances, previous_vertices = dijkstra(G, start_station)
    all_shortest_paths[start_station] = distances

# Приклад: Виведемо найкоротший шлях та його вартість між двома станціями
def get_shortest_path(graph, previous_vertices, start, end):
    path = []
    current = end
    while current != start:
        if previous_vertices[current] is None:
            return None  # Шляху немає
        path.insert(0, current)
        current = previous_vertices[current]
    path.insert(0, start)
    return path

start_station = 'Akademmistechko'
end_station = 'Chervonyi Khutir'

# Отримуємо відстані та попередні вершини від стартової станції
distances, previous_vertices = dijkstra(G, start_station)
shortest_path = get_shortest_path(G, previous_vertices, start_station, end_station)
total_distance = distances[end_station]

print(f"Найкоротший шлях від {start_station} до {end_station}:")
print(" -> ".join(shortest_path))
print(f"Загальний час у дорозі: {total_distance} хвилин")

# Візуалізація графа та найкоротшого шляху
def visualize_shortest_path(graph, path, title):
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(graph, k=0.3, iterations=50, seed=42)
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

visualize_shortest_path(G, shortest_path, f"Найкоротший шлях від {start_station} до {end_station}")
