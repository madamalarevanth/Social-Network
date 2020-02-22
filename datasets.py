import networkx as nx 
import matplotlib.pyplot as plt 


def plot_deg_dist(G):
	all_degrees = nx.degree(G).values()
	unique_degrees = list(set(all_degrees))

	count_of_degrees = []

	for i in unique_degrees:
		x= all_degrees.count(i)
		count_of_degrees.append(x)

		plt.plot(unique_degrees, count_of_degrees,'yo-')
		plt.xlabel('Degrees')
		plt.ylabel('no of degrees')
		plt.title(Degree Dist)
		plt.show()

#G= nx.read_edgelist('dataset/facebook_combined.txt')
#G= nx.read_pajek('dataset/football.net')
#G= nx.read_graphml('dataset/vecwiki-20091230-manual-coding.graphml')
#G= nx.read_gexf('dataset/EuroSiS_Generale_Pays.graphml')
G = nx.read_gml('dataset/karate.gml')

#print(nx.info(G))

#print( nx.number_of_nodes(G) )
#print( nx.number_of_edges(G) )

#print(nx.is_directed(G))

#nx.draw(G)
#plt.show()

plot_deg_dist(G)