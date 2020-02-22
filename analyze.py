import networkx as nx 
import matplotlib.pyplot as plt 


def plot_density():
    x= []
    y=[]
    for i in range(0,11):
        G= nx.read_gml('../week4/network/social_influence_'+str(i)+'.gml')
        x.append(i)
        y.append(nx.density(G))
    plt.xlabel('Time')
    plt.ylabel('Density')
    plt.title('Change in Denisty')
    plt.plot(x,y)
    plt.show()

def obesity(G):
    num =0 
    for each in G.nodes():
        if G.node[each]['name'] ==40:
            num=num+1

    return num

def plot_obesity():
    x= []
    y=[]
    for i in range(0,11):
        G= nx.read_gml('../week4/network/social_influence_'+str(i)+'.gml')
        x.append(i)
        y.append(obesity(G))
    plt.xlabel('Time')
    plt.ylabel('Obesity')
    plt.title('Change in Obesity')
    plt.plot(x,y)
    plt.show()

plot_density()
plot_obesity()