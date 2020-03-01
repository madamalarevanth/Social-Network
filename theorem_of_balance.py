import networkx as nx 
import matplotlib.pyplot as plt 
import random 
import itertools

#implementation 

def get_signs_of_tris(tris_list,G):
    all_signs = []
    for i in range(len(tris_list)):
        temp=[]
        temp.append(G[tris_list[i][0]][tris_list[i][1]]['sign'])
        temp.append(G[tris_list[i][1]][tris_list[i][2]]['sign'])
        temp.append(G[tris_list[i][2]][tris_list[i][0]]['sign'])
        all_signs.append(temp)
    return all_signs


def count_unstable(all_signs):
    unstable = 0
    stable=0
    for i in range(len(all_signs)):
        if all_signs[i].count('+')==3 or all_signs[i].count('+') ==1:
            stable += 1
        elif all_signs[i].count('+')==2 or all_signs[i].count('+') ==0  :
            unstable += 1
    print("number of stable triangles",stable)
    print("number of unstable triangles",unstable)
    return unstable


def move_tri_to_stable(G,tris_list,all_signs):
    #find unstable triangle 
    found_unstable = False
    while found_unstable == False :
        index= random.randint(0,len(tris_list)-1)
        if all_signs[index].count('+') == 2 or all_signs[index].count('+') == 0 :
            found_unstable= True
        else:
            continue
    
    #move unstable triangle to stable state 
    r=random.randint(1,3)
    if all_signs[index].count('+') == 2:
        if r==1:
            if G[tris_list[index][0]][tris_list[index][1]]['sign']  == '+':
               G[tris_list[index][0]][tris_list[index][1]]['sign']  = '-' 
            elif G[tris_list[index][0]][tris_list[index][1]]['sign']  == '-':
               G[tris_list[index][0]][tris_list[index][1]]['sign']  = '+' 
        
        elif r==2:
            if G[tris_list[index][1]][tris_list[index][2]]['sign']  == '+':
               G[tris_list[index][1]][tris_list[index][2]]['sign']  = '-' 
            elif G[tris_list[index][1]][tris_list[index][2]]['sign']  == '-':
               G[tris_list[index][1]][tris_list[index][2]]['sign']  = '+' 
            
        elif r==3:
            if G[tris_list[index][2]][tris_list[index][0]]['sign']  == '+':
               G[tris_list[index][2]][tris_list[index][0]]['sign']  = '-' 
            elif G[tris_list[index][2]][tris_list[index][0]]['sign']  == '-':
               G[tris_list[index][2]][tris_list[index][0]]['sign']  = '+' 
    
    if all_signs[index].count('+') == 0:
        if r==1:
            G[tris_list[index][0]][tris_list[index][1]]['sign']  = '+'
        
        elif r==2:
            G[tris_list[index][1]][tris_list[index][2]]['sign']  = '+'
            
        elif r==3:
            G[tris_list[index][2]][tris_list[index][0]]['sign']  = '+'
           
    return G


def see_coalition(G):
    first_coalition =[]
    second_coalition =[]

    r = random.choice(nodes)
    first_coalition.append(r)

    processed_nodes=[]
    to_be_processed =[r]
    
    for each in to_be_processed:
        if each not in processed_nodes:
            neigh = G.neighbors(each)

            for i in range(len(neigh)):
                if G[each][ neigh[i]]['sign'] =='+':
                    if neigh[i] not in first_coalition:
                        first_coalition.append(neigh[i])
                    
                    if neigh[i] not in to_be_processed:
                        to_be_processed.append(neigh[i])
                
                elif G[each][neigh[i]]['sign'] == '-':
                    if neigh[i] not in second_coalition:
                        second_coalition.append(neigh[i])
                        processed_nodes.append(neigh[i])
                
            processed_nodes.append(each)
    
    return first_coalition, second_coalition



#1. create a graph with n nodes, where nodes are the countries.
G = nx.Graph()
n=5
G.add_nodes_from([i for i in range(1,n+1)])
mapping = {1:'Alexandra',2:'Anterim', 3:'Bercy', 4:'Bearland', 5:'Eplex',6:'Gripa', 7:'Ikly',8:'Jemra',9:'Lema',10:'Umesi',11:'Mexim',12:'Socialcity',13:'Tersi',14:'Xopia' ,15:'Tamara'}
nx.relabel_nodes(G,mapping)

#2. make it a complete graph by adding all possible edges, also assign '+' or '-' signs asweights to all the edges randomly  
signs = ['+','-']
for i in G.nodes():
    for j in G.nodes():
        if i != j:
            G.add_edge(i,j,sign = random.choice(signs))


#3. Display the network 
edge_labels = nx.get_edge_attributes(G,'sign')
pos= nx.circular_layout(G)
nx.draw(G,pos,node_size = 5000)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,font_size=20, font_color= 'red' )
plt.show()

#4.1. Get a list of all the triangles in network
nodes = G.nodes()
tris_list = [list(x) for x in itertools.combinations(nodes,3)]

#4.2. store the sign details of all triangles 
all_signs = get_signs_of_tris(tris_list,G) #[['+','-','-'],[]]

#4.3.count the number of unstable triangles in the network 
unstable = count_unstable(all_signs)

unstable_track =[unstable]

#5. while the number of unstable triangles is not zero, do the following.
while unstable !=0:
    #5.1. choose a triangle in the graph that is unstable 
    #5.2. Make the triangle stable 
    move_tri_to_stable(G,tris_list,all_signs)
    all_signs = get_signs_of_tris(tris_list,G)

    #5.3. Count the number of unstable traingles
    unstable = count_unstable(all_signs)
    unstable_track.append(unstable)

plt.bar([i for i in range(len(unstable_track))],unstable_track)
plt.show()

#6 Now that there is no unstable triangles in the network 
#6.1. choose a random node. Add it to the first coalition 
#6.2. Also put all the friends of this nodes to the first coalition 
#6.3. put all the enemies of the node in the second coalition 
#6.4. Repeat 6.2 and 6.3 for all the unprocessed nodes 

first, second = see_coalition(G)
print("first coalition",first ,"second_coalition",second)

#display the network with coalition 
pos = nx.circular_layout()
nx.draw_networkx_nodes(g,pos,nodelist=first,node_color='red',node_size=5000)
nx.draw_networkx_nodes(g,pos,nodelist=second,node_color='blue',node_size=5000)

nx.draw_networkx_labels(G,pos,font_size=10)
nx.draw_networkx_edges(G,pos)
edge_labels = nx.get_edge_attributes(G,'sign')
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,font_size=20)
plt.show()