from Nodo import Nodo

import networkx as nx
import matplotlib.pyplot as plt


odo = Nodo((1,2),None,2,None)
odo2 = Nodo((3,4),None,23,None)

g = nx.Graph()

g.add_node(str(odo))
g.add_node(str(odo2))
g.add_edge(str(odo),str(odo2))




nx.draw(g,with_labels=True)
        
plt.draw()
plt.show()

