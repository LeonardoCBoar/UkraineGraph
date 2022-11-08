import networkx
import matplotlib
import csv

# Instantiate Graph object
ukraine = networkx.Graph()

# Read city data from csv file
ukraine_matrix_file = open("Ukraine.csv", 'r')
csv_reader = csv.reader(ukraine_matrix_file, delimiter=',')

# Iterate trough the file, generating the graph matrix
ukraine_matrix = []
for line in ukraine_matrix_file:
    city_connections = []

    for number in line.replace('\n', '').replace(' ', '').split(','):
        city_connections.append(int(number))

    ukraine_matrix.append(city_connections)

# Add nodes from the matrix
for city_index in range(len(ukraine_matrix)):
    ukraine.add_node(city_index+1)

# Add edges between nodes
for city_index, city in enumerate(ukraine_matrix):
    for connection in city:
        ukraine.add_edge(city_index+1, connection)

print(networkx.node_connectivity(ukraine))
print(networkx.edge_connectivity(ukraine))

# Render graph on screen
networkx.draw_networkx(ukraine, with_labels=True)
matplotlib.pyplot.show()

