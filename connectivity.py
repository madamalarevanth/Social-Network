import networkx as nx 
import random 
import matplotlib.pyplot as plt 
import numpy 
#add n number of nodes in the graph 
def add_nodes(n):
	G= nx.Graph()
	G.add_nodes_from(range(n))
	return G

#Add one random edge in the network
def add_random_edge(G):
	nodes =list(G.nodes())
	v1 = random.choice(nodes)
	v2 = random.choice(nodes)
	if v1!=v2:
		G.add_edge(v1,v2)
	return G

#keeps adding random edges in G till it becomes connected
def add_till_connectivity(G):
	while(nx.is_connected(G) == False):
		G=add_random_edge(G)
	return G

#Creates an instances of the entire process. 
#takes no of nodes and return number of nodes required for connectivity 
def create_instance(n):
	G= add_nodes(n)
	G=add_till_connectivity(G)
	return G.number_of_edges()

#average it over 4 instances
def create_average_instance(n):
	list1=[]
	for i in range(0,100):
		list1.append(create_instance(n))
	return numpy.average(list1)	

#plot the desired for diff number of edges
def plot_connectivity():
	x=[]
	y=[]
	i=10 #no of nodes
	while(i<=400):
		x.append(i)
		y.append(create_average_instance(i))
		i=i+10
	plt.xlabel("Num of Nodes")
	plt.ylabel("num of edges required to connect the graph")
	plt.plot(x,y)
	plt.show()

	x1=[]
	y1=[]
	i=10 #no of nodes
	while(i<=400):
		x1.append(i)
		y1.append(i*numpy.log(i))
		i=i+10
	plt.plot(x,y)
	plt.show()