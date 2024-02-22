import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations

def tsp_bruteforce(distances, start_city=0):
    num_cities = len(distances)
    cities = list(range(num_cities))
    best_order = None
    min_distance = float('inf')

    for order in permutations(cities):
        total_distance = calculate_total_distance(order, distances)
        if total_distance < min_distance:
            min_distance = total_distance
            best_order = order

    # Сдвигаем порядок, чтобы начать с выбранной стартовой вершины
    start_index = best_order.index(start_city)
    best_order = best_order[start_index:] + best_order[:start_index]

    return best_order, min_distance

def calculate_total_distance(order, distances):
    total_distance = 0
    for i in range(len(order) - 1):
        total_distance += distances[order[i]][order[i + 1]]
    return total_distance

def visualize_tsp_solution(cities, order, distances):
    G = nx.Graph()

    for i in range(len(cities)):
        G.add_node(i, pos=cities[i])

    for i in range(len(distances)):
        for j in range(i + 1, len(distances[i])):
            G.add_edge(i, j, weight=distances[i][j])

    pos = nx.get_node_attributes(G, 'pos')

    # Округляем веса рёбер до целых чисел
    labels = {(i, j): int(weight) for (i, j, weight) in G.edges(data='weight')}

    best_order = list(order) + [order[0]]

    plt.figure(figsize=(10, 8))

    # Рисуем граф с заданными координатами
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=8, font_color='black',
            font_weight='bold')

    # Рисуем рёбра с прозрачностью
    nx.draw_networkx_edges(G, pos, edgelist=[(best_order[i], best_order[i + 1]) for i in range(len(best_order) - 1)],
                           edge_color='red', width=2, alpha=0.7)

    # Отмечаем стартовую точку
    nx.draw_networkx_nodes(G, pos, nodelist=[best_order[0]], node_color='blue', node_size=700)

    # Подписываем веса рёбер
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='black')

    plt.title("Маршрут коммивояжера")
    plt.axis('off')
    plt.show()

# Пример с 8 городами и случайной матрицей весов (стоимостей перемещения)
np.random.seed(42)
cities_coordinates = np.random.randint(1, 100, (8, 2))
cities_distances = np.zeros((8, 8))

for i in range(8):
    for j in range(i + 1, 8):
        distance = np.linalg.norm(cities_coordinates[i] - cities_coordinates[j])
        cities_distances[i][j] = distance
        cities_distances[j][i] = distance

# Добавляем выбор стартовой вершины
start_city = int(input("Введите индекс стартовой вершины (от 0 до 7): "))
best_order, min_distance = tsp_bruteforce(cities_distances, start_city)
print("Лучший порядок посещения городов:", best_order)
print("Минимальное расстояние:", min_distance)

visualize_tsp_solution(cities_coordinates, best_order, cities_distances)
