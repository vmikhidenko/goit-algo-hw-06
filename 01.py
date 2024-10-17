import networkx as nx
import matplotlib.pyplot as plt

# Створюємо порожній граф
G = nx.Graph()

# Визначаємо станції кожної лінії метрополітену
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

# Додаємо станції до графа
G.add_nodes_from(red_line)
G.add_nodes_from(blue_line)
G.add_nodes_from(green_line)

# Додаємо ребра між сусідніми станціями на червоній лінії
G.add_edges_from([(red_line[i], red_line[i+1]) for i in range(len(red_line)-1)])

# Додаємо ребра між сусідніми станціями на синій лінії
G.add_edges_from([(blue_line[i], blue_line[i+1]) for i in range(len(blue_line)-1)])

# Додаємо ребра між сусідніми станціями на зеленій лінії
G.add_edges_from([(green_line[i], green_line[i+1]) for i in range(len(green_line)-1)])

# Додаємо пересадочні вузли
G.add_edge('Teatralna', 'Zoloti Vorota')  # Пересадка між червоною та зеленою лініями
G.add_edge('Khreshchatyk', 'Maidan Nezalezhnosti')  # Пересадка між червоною та синьою лініями
G.add_edge('Ploshcha Lva Tolstoho', 'Palats Sportu')  # Пересадка між синьою та зеленою лініями

# Візуалізуємо граф
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, k=0.3, iterations=50)
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, font_size=8)
plt.axis('off')
plt.show()

# Аналіз основних характеристик
print(f"Кількість станцій (вершин): {G.number_of_nodes()}")
print(f"Кількість сполучень (ребер): {G.number_of_edges()}")

# Розрахунок ступеня кожної вершини
degrees = dict(G.degree())
print("\nСтупінь кожної станції:")
for station, degree in degrees.items():
    print(f"{station}: {degree}")
