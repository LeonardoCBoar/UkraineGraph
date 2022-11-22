import networkx
import matplotlib
import csv

import distances

# Instantiate Graph object
ukraine = networkx.Graph()


for city_index, city in enumerate(distances.distances):
    ukraine.add_node(city_index+1)

for city_index, city in enumerate(distances.distances):
    for paths in city:
        ukraine.add_edge(city_index+1, paths[0], weight=paths[1])


pos = networkx.spring_layout(ukraine, seed=7)
networkx.draw_networkx_nodes(ukraine, pos, node_size=700)
networkx.draw_networkx_edges(ukraine, pos, width=6)
edge_labels = networkx.get_edge_attributes(ukraine, "weight")
networkx.draw_networkx_edge_labels(ukraine, pos, edge_labels)


print(networkx.node_connectivity(ukraine))
print(networkx.edge_connectivity(ukraine))


matplotlib.pyplot.show()

