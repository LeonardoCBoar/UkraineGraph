import time
import random
import copy

import networkx
import matplotlib

import distances
import metrics
import attacks



# Instantiate Graph object
ukraine = networkx.Graph()
city_count = len(distances.distances)
city_list = list()
paths_list = list()

for city_index in range(1, city_count+1):
    city_list.append(city_index)

# Create and populate graph
for city_index, city in enumerate(distances.distances):
    ukraine.add_node(city_index+1)

for city_index, city in enumerate(distances.distances):
    for paths in city:
        path = [city_index + 1, paths[0]]

        if ([path[1], path[0]] in paths_list):
            continue
        paths_list.append(path)
        ukraine.add_edge(city_index+1, paths[0], weight=paths[1])


original_metrics = metrics.calculate_metrics(ukraine, city_list)
original_metrics.print("Métricas Originais")

## Targeted Attacks

# Attack the city which most increases the metrics
diameter_targeted_node_metrics = original_metrics
most_diameter_critical_city = -1
avg_dist_targeted_node_metrics = original_metrics
most_avg_dist_critical_city = -1


for attacked_city in city_list:

    after_attack_metrics = attacks.attack_city(ukraine, city_list, attacked_city)

    if (after_attack_metrics.diameter > diameter_targeted_node_metrics.diameter):
        diameter_targeted_node_metrics = after_attack_metrics
        most_diameter_critical_city = attacked_city
    if (after_attack_metrics.average_distance > avg_dist_targeted_node_metrics.average_distance):
        avg_dist_targeted_node_metrics = after_attack_metrics
        most_avg_dist_critical_city = attacked_city

diameter_targeted_node_metrics.print(f"Ataque direcionado a cidade {most_diameter_critical_city}, o que mais aumenta o diâmetro")
avg_dist_targeted_node_metrics.print(f"Ataque direcionado a cidade {most_avg_dist_critical_city}, o que mais aumenta distancia média")

# Attack the path which most increases the metrics
diameter_targeted_edge_metrics = original_metrics
most_diameter_critical_path = -1
avg_dist_targeted_edge_metrics = original_metrics
most_avg_dist_critical_path = -1

for attacked_path in paths_list:
    after_attack_metrics = attacks.attack_path(ukraine, city_list, attacked_path)
    
    if (after_attack_metrics.diameter > diameter_targeted_edge_metrics.diameter):
        diameter_targeted_edge_metrics = after_attack_metrics
        most_diameter_critical_path = attacked_path
    if (after_attack_metrics.average_distance > avg_dist_targeted_edge_metrics.average_distance):
        avg_dist_targeted_edge_metrics = after_attack_metrics
        most_avg_dist_critical_path = attacked_path


diameter_targeted_edge_metrics.print(f"Ataque direcionado ao caminho {most_diameter_critical_path[0]} -> {most_diameter_critical_path[1]}, o  que mais aumenta o diâmetro ")
avg_dist_targeted_node_metrics.print(f"Ataque direcionado ao caminho {most_avg_dist_critical_path[0]} -> {most_avg_dist_critical_path[1]}, o que mais aumenta a distancia média")


## Random attacks

# Remove 5 random cities 100 times
random_city_attack_metrics = []
for _sample in range(100):
    attacked_ukraine = copy.deepcopy(ukraine)
    attacked_ukraine_city_list = copy.deepcopy(city_list)

    for _i in range(5):
        attacks.attack_random_city(attacked_ukraine, attacked_ukraine_city_list)

    after_random_attack_metrics = metrics.calculate_metrics(attacked_ukraine, attacked_ukraine_city_list)
    random_city_attack_metrics.append(after_random_attack_metrics)

average_random_city_attack_metrics = metrics.calculate_average_metrics(random_city_attack_metrics)
average_random_city_attack_metrics.print("Ataque aleatório a 5 cidades, média de 100 simulações")

# Remove 5 random paths 100 times
random_path_attack_metrics = []
for _sample in range(100):
    attacked_ukraine = copy.deepcopy(ukraine)
    attacked_ukraine_path_list = copy.deepcopy(paths_list)

    for _i in range(5):
        attacks.attack_random_path(attacked_ukraine, attacked_ukraine_path_list)

    after_random_attack_metrics = metrics.calculate_metrics(attacked_ukraine, city_list)
    random_path_attack_metrics.append(after_random_attack_metrics)

average_random_path_attack_metrics = metrics.calculate_average_metrics(random_path_attack_metrics)
average_random_path_attack_metrics.print("Ataque aleatório a 5 caminhos, média de 100 simulações")

# Render graph
pos = networkx.spring_layout(ukraine, seed=7)
networkx.draw_networkx_nodes(ukraine, pos)
networkx.draw_networkx_edges(ukraine, pos, width=6)
edge_labels = networkx.get_edge_attributes(ukraine, "weight")
networkx.draw_networkx_edge_labels(ukraine, pos, edge_labels)
networkx.draw_networkx_labels(ukraine, pos)

matplotlib.pyplot.show()

