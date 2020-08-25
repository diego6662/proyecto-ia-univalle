"""
    this class represent the Nodo of tree
"""
class Nodo():

    # Proposito: 
    #   Debe usar insert short para insertar el item, timedo su valAc, como 
    #   criterio de comparacion
    # item: -> nodo
    # lista: -> silta de duplas

    def insertN(item, lista):
        if(lista == []):
            return [item]
        elif(item < lista[0]):
            return [item] + lista
        else: 
            return [lista[0]] + Nodo.insertN(item,lista[1:])

    # pos : tupla -> posicion del pacman
    # padre: Nodo -> nodo padre
    # valAc: number -> valor a>comulado
    # origin: nodo -> nodo raiz
    def __init__(self, pos, padre, valAc, origin):
        self.pos = pos
        #self.padre = padre
        self.valAc = valAc
        self.origin = origin # este tributo es el origen de toda la rama
        self.movC = 0 #costo de moverse caso urgente

    # overloading oppes

    # >
    def __gt__ (self,nodo2):
        return self.valAc > nodo2.valAc
    # <
    def __lt__(self,nodo2):
        return self.valAc < nodo2.valAc

    # !=
    def  __eq__(self,nodo2):
        return (self.pos == nodo2.pos)

    def __repr__(self):         
        # return str(self.pos) 
        return  "[" + str(self.pos)+",V "+str(self.valAc) + "]"

    def __str__(self):
        # return str(self.pos) 
        return  "[" + str(self.pos)+",V "+str(self.valAc) + "]"

   

