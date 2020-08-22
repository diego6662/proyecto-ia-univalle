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
        first = f"1-{nodes[0]}"
        G.add_node(first)
        for i in range(1,len(self.node)):
            actual_node = f"{i + 1}-{nodes[i]}"
            G.add_node(actual_node)
            past_node = f"{i}-{nodes[i - 1]}"

            G.add_edge(past_node,actual_node)
       
        nx.draw(G,with_labels=True,node_color=colors)
        
        plt.draw()
        plt.show()



