import math

import networkx

class Metrics:
    def __init__(self, average_distance: float, diameter: float, node_connectivity: int, edge_connectivity: int, subgraphs_count: int):
        self.average_distance = average_distance
        self.diameter = diameter
        self.node_connectivity = node_connectivity
        self.edge_connectivity = edge_connectivity
        self.subgraphs_count = subgraphs_count
    
    def print(self, title=""):
        print(f"\n{title.upper()}")
       
        print(f"Distancia média entre os vértices: {self.average_distance:.3f} km")
        print(f"Diametro: {self.diameter:.3f} km")
        print(f"Conectividade de vértice: {self.node_connectivity} nodes")
        print(f"Conectividade de aresta: {self.edge_connectivity} edge")
        print(f"Subgrafos: {self.subgraphs_count}")


def calculate_metrics(graph: networkx.Graph, city_list: list) -> Metrics:
    city_distances = networkx.floyd_warshall(graph)

    total_distance = 0
    considered_pairs = 0
    diameter = 0

    for origin in city_list:
        if (origin not in city_list):
            continue

        for target in city_list:
            if (origin == target or (target not in city_list)):
                continue

            distance = city_distances[origin][target]

            # Ignore disconnected nodes with infinite distances
            if (math.isinf(distance)):
                continue

            considered_pairs += 1
            total_distance += distance

            if (distance > diameter):
                diameter = distance

    average_distance = total_distance/considered_pairs

    node_connectivity = float(networkx.node_connectivity(graph))
    edge_connectivity = float(networkx.edge_connectivity(graph))
    subgraphs_count = networkx.number_connected_components(graph)

    return Metrics(
        average_distance,
        diameter,
        node_connectivity,
        edge_connectivity,
        subgraphs_count
    )

def calculate_average_metrics(average_list: list) -> Metrics:
    summed_diameter = 0
    summed_average_distance = 0
    summed_node_connectivity = 0
    summed_edge_connectivity = 0
    summed_subgraphs_count = 0

    for metrics in average_list:
        summed_diameter += metrics.diameter
        summed_average_distance += metrics.average_distance
        summed_node_connectivity += metrics.node_connectivity
        summed_edge_connectivity += metrics.edge_connectivity
        summed_subgraphs_count += metrics.subgraphs_count
    
    count = len(average_list)
    return Metrics(
        summed_diameter / count,
        summed_average_distance / count,
        summed_node_connectivity / count,
        summed_edge_connectivity / count,
        summed_subgraphs_count / count
    )