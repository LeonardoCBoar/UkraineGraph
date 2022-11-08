import networkx
import matplotlib
import csv

# Instancia objeto do Grafo
ukraine = networkx.Graph()

# Matrix de adjacencia
ukraine_matrix_file = open("Ukraine.csv", 'r')
csv_reader = csv.reader(ukraine_matrix_file, delimiter=',')

ukraine_matrix = []
for line in ukraine_matrix_file:
    ukraine_matrix.append(line.replace('\n', '').split(','))


for city_index in range(len(ukraine_matrix)):
    ukraine.add_node(city_index+1)

for city_index, city in enumerate(ukraine_matrix):
    for connection in city:
        ukraine.add_edge(city_index+1, connection)


# Conecta nós 2,3
ukraine.add_edge(2, 3)

# Renderiza nós na tela
networkx.draw_networkx(ukraine, with_labels=True)
matplotlib.pyplot.show()

networkx.node_connectivity(ukraine)
networkx.edge_connectivity(ukraine)
