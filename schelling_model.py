import networkx as nx 
import matplotlib.pyplot as plt
import random 

N=10
G =nx.grid_2d_graph(N,N)
pos= dict((n,n) for n in G.nodes())
labels = dict( ((i,j),i*10+j) for i,j in G.nodes())


def display_graph(G):
    nodes_g = nx.draw_networkx_nodes(G,pos, node_color = 'green', nodelist= type_1_node_list)
    nodes_r = nx.draw_networkx_nodes(G,pos, node_color = 'red',  nodelist= type_2_node_list)
    nodes_w = nx.draw_networkx_nodes(G,pos, node_color = 'white', nodelist= empty_cells)

    nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_labels(G,pos,labels= labels)
    plt.show()

def get_boundary_nodes(G):
     boundary_nodes_list= []
     for ((u,v),d) in G.nodes(data = True):
         if u ==0 or u == N-1 or v ==0 or v == N-1 :
             boundary_nodes_list.append((u,v))
             #print( u,v, "appended")
     return boundary_nodes_list

def get_neigh_for_internal(u,v):
    return [(u-1,v),(u+1,v),(u,v+1),(u,v-1),(u+1,v+1),(u-1,v-1)]

def get_neigh_for_boundary(u,v):
    # global N
    # print 'uv', u, v

    if u ==0 and v==0:
        return [(0,1),(1,1),(1,0)]
    elif u == N-1 and v== N-1:
        return [(N-2,N-2),(N-1,N-2),(N-2,N-1)]
    elif u == N-1 and v== 0:
        return [(u-1,v),(u-1,v+1),(u,v+1)]
    elif u == 0 and v== N-1:
        return [(u+1,v),(u+1,v-1),(u,v-1)]
    elif u == 0 :
        return [(u,v+1),(u,v-1),(u+1,v),(u+1,v-1),(u+1,v+1)]
    elif u == N-1:
        return [(u-1,v),(u,v-1),(u,v+1),(u-1,v+1),(u-1,v-1)]
    elif v== N-1:
        return [(u,v-1),(u-1,v),(u+1,v),(u-1,v-1),(u+1,v-1)]
    elif v == 0 :
        return [(u-1,v),(u+1,v),(u,v+1),(u-1,v+1),(u+1,v+1)]
    
def get_unsatisfied_nodes_list(G,boundary_nodes_list,internal_nodes_list):
    unsatisfied_nodes_list =[]
    threshold =3
    for u,v in G.nodes():
        type_of_this_node = G.nodes[(u,v)]['type']
        if type_of_this_node == 0 :
            continue
        else:
            similar_nodes =0
            if (u,v) in internal_nodes_list:
                neigh = get_neigh_for_internal(u,v)
            elif (u,v) in boundary_nodes_list:
                neigh = get_neigh_for_boundary(u,v)
        
            for each in neigh:
                if G.nodes[each]['type'] == type_of_this_node :
                    similar_nodes= similar_nodes+1

            if similar_nodes <= threshold :
                unsatisfied_nodes_list.append((u,v))
    
    return unsatisfied_nodes_list   

def make_a_node_satisfied(unsatisfied_nodes_list,empty_cells):
    if len(unsatisfied_nodes_list) != 0 :
        node_to_shift = random.choice(unsatisfied_nodes_list)
        new_position = random.choice(empty_cells)

        G.nodes[new_position]['type'] = G.nodes[node_to_shift]['type']
        G.nodes[node_to_shift]['type']=0
        labels[node_to_shift],labels[new_position] = labels[new_position],labels[node_to_shift]
    else:
        pass




#main 


#Add diagonal Edges
for ((u,v),d) in G.nodes(data=True) :
    if (u+1 <= N-1) and (v+1 <= N-1) :
        G.add_edge((u,v),(u+1,v+1))
    
for ((u,v),d) in list(G.nodes(data=True)) :
    if (u+1 <= N-1) and (v-1 >= 0) :
        G.add_edge((u,v),(u+1,v-1))


#nx.draw(G,pos, with_labels = False)  
#nx.draw_networkx_labels(G,pos,labels= labels)
#plt.show()  

for n in G.nodes():
    G.nodes[n]['type'] = random.randint(0,2)

type_1_node_list = [ n for n,d in G.nodes(data = True) if d['type']== 1]
type_2_node_list = [ n for n,d in G.nodes(data = True) if d['type']== 2]
empty_cells = [ n for n,d in G.nodes(data = True) if d['type']== 0]


display_graph(G)

boundary_nodes_list = get_boundary_nodes(G)
internal_nodes_list = list(set(G.nodes)- set(boundary_nodes_list))

#print(boundary_nodes_list)
#print(internal_nodes_list)


for i in range(1000):
#print unsatisfied nodes
    unsatisfied_nodes_list = get_unsatisfied_nodes_list(G,boundary_nodes_list,internal_nodes_list)
    print(unsatisfied_nodes_list)

    make_a_node_satisfied(unsatisfied_nodes_list,empty_cells)

    type_1_node_list = [ n for n,d in G.nodes(data = True) if d['type']== 1]
    type_2_node_list = [ n for n,d in G.nodes(data = True) if d['type']== 2]
    empty_cells = [ n for n,d in G.nodes(data = True) if d['type']== 0]

display_graph(G)