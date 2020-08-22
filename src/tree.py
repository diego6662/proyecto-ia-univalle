import networkx as nx
import matplotlib.pyplot as plt
from Nodo import Nodo 
class Tree():
    def __init__(self,nodes):
        self.node = nodes
    def printer(self,title):
        titulo = f"arbol de recorrido del {title}"
        plt.title(title,text=titulo)
        G = nx.Graph()

        colors = ["red"] + ["blue"] * (len(self.node) - 2) + ['yellow']
        nodes = self.node
        G.add_node(str(nodes[0]))
        for i in range(1,len(self.node)):
            G.add_node(str(nodes[i]))
            G.add_edge(str(nodes[i - 1]),str(nodes[i]))
       
        nx.draw(G,with_labels=True,node_color=colors)
        
        plt.draw()
        plt.show()



