import time
import copy

import networkx
import matplotlib

import distances
import metrics




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
        paths_list.append([city_index+1, paths[0]])
        ukraine.add_edge(city_index+1, paths[0], weight=paths[1])


original_metrics = metrics.calculate_metrics(ukraine, city_list)
original_metrics.print("Original Metrics")

# Targeted Attacks

diameter_targeted_node_metrics = original_metrics
most_diameter_critical_city = -1

for attacked_city in city_list:
    # Remove each node, recalculate metrics, storing the node that generated the biggest increase in diameter

    after_attack_ukraine = copy.deepcopy(ukraine)
    after_attack_ukraine.remove_node(attacked_city)
    after_attack_city_list = copy.deepcopy(city_list)
    after_attack_city_list.remove(attacked_city)
    after_attack_metrics = metrics.calculate_metrics(after_attack_ukraine, after_attack_city_list)

    if (after_attack_metrics.diameter > diameter_targeted_node_metrics.diameter):
        diameter_targeted_node_metrics = after_attack_metrics
        most_diameter_critical_city = attacked_city

diameter_targeted_node_metrics.print(f"Diameter targeted attack at city {most_diameter_critical_city}")


diameter_targeted_edge_metrics = original_metrics
most_diameter_critical_path = -1

for attacked_path in paths_list:
    # Remove each node, recalculate metrics, storing the node that generated the biggest increase in diameter
    origin = attacked_path[0]
    target = attacked_path[1]
    after_attack_ukraine = copy.deepcopy(ukraine)
    after_attack_ukraine.remove_edge(origin, target)
    after_attack_metrics = metrics.calculate_metrics(after_attack_ukraine, city_list)

    if (after_attack_metrics.diameter > diameter_targeted_edge_metrics.diameter):
        diameter_targeted_edge_metrics = after_attack_metrics
        most_diameter_critical_path = attacked_path


diameter_targeted_edge_metrics.print(f"Diameter targeted attack at path {most_diameter_critical_path[0]} -> {most_diameter_critical_path[1]}")


# Render graph
pos = networkx.spring_layout(ukraine, seed=7)
networkx.draw_networkx_nodes(ukraine, pos)
networkx.draw_networkx_edges(ukraine, pos, width=6)
edge_labels = networkx.get_edge_attributes(ukraine, "weight")
networkx.draw_networkx_edge_labels(ukraine, pos, edge_labels)
networkx.draw_networkx_labels(ukraine, pos)




matplotlib.pyplot.show()

