import networkx as nx
import matplotlib.pyplot as plt
from Nodo import Nodo 
G = nx.Graph()

a = Nodo((1,2),None,2,"Arribas")
b = Nodo((1,3),a,32,"Abajo")
azul = ["red"] + ["blue"]*1 

G.add_node(str(a),color="1,23,2")
G.add_node(str(b))
G.add_edge(str(a), str(b))
nx.draw(G,with_labels=True,node_color=azul)
plt.draw()
plt.show()
