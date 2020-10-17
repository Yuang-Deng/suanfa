import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

edgelist = []
nodelist = {}

fe=open("SCC.in","r")
edge=fe.read().splitlines()[1:]
for line in edge:
    edgelist.append((line.split(' ')[0],line.split(' ')[1]))
G.add_edges_from(edgelist)

fn=open("ConnectedComponents.out","r")
nodes=fn.read().splitlines()
for line in nodes:
    nodelist[line.split('-')[0]]=int(line.split('-')[1])/10

values = [nodelist.get(node) for node in G.nodes()]

# Need to create a layout when doing
# separate calls to draw nodes and edges
# pos = nx.spring_layout(G)
# nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
#                        node_color = values, node_size = 500)
# nx.draw_networkx_labels(G, pos)
# nx.draw_networkx_edges(G, pos=nx.random_layout(G), edgelist=edgelist, arrows=True,width=0.3,style='solid',font_size=8)
nx.draw_networkx(G,node_size=100, font_size=5, pos=nx.random_layout(G), edgelist=edgelist, arrows=True, width=0.3, style='solid', node_color=values)
plt.show()