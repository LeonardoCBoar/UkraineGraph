import math

import networkx

class Metrics:
    def __init__(self, average_distance: float, diameter: float, node_connectivity: int, edge_connectivity: int):
        self.average_distance = average_distance
        self.diameter = diameter
        self.node_connectivity = node_connectivity
        self.edge_connectivity = edge_connectivity
    
    def print(self, title=""):
        print(f"\n {title.upper()}")
       
        print(f"Average Distance: {self.average_distance} km")
        print(f"Diameter: {self.diameter} km")
        print(f"Node Connectivity: {self.node_connectivity} nodes")
        print(f"Edge Connectivity: {self.edge_connectivity} edge")


def calculate_metrics(graph: networkx.Graph, city_list: list):
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

    node_connectivity = networkx.node_connectivity(graph)
    edge_connectivity = networkx.edge_connectivity(graph)

    return Metrics(
        average_distance,
        diameter,
        node_connectivity,
        edge_connectivity
    )