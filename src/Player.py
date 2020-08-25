#imports
import pygame
import numpy as np
from mapa import mapa
from Nodo import Nodo
# THIS CALASS ALLOW VREATE THE PACMAN
# HOW A NEW AGENTE
import networkx as nx
import matplotlib.pyplot as plt
class Player():
    def __init__(self):
        #CODENADAS DE POOSICION
        self.x = None
        self.y = None
        self.i = None
        self.j = None
        # meta
        self.goal = None
        self.spinaca_positoin = None
        self.radius = 10
        #booleano que me permite saber que busqueda aplicar
        self.A_start = False 
       #el costo de cada movimiento se establece como una variable
        self.costo_mov = 1
       #se crea una lista en la cual se guarda todos los nodos visitados
        self.visited = []
        self.espinaca = False
        self.arbol_panic = nx.Graph()
        self.cont =0
        self.graph_three = False #allowgraph tree

    #ACTUALIZAR EL POSICIONAMIENTO
    def update_space(self,i = 0,j = 0):
        mapa.matrix[self.i,self.j] = " "
        self.i = i
        self.j = j
        mapa.pacman = (self.i, self.j)
        mapa.matrix[self.i, self.j] = "P"

    #ACTUALIZAR ESCALA
    def update(self):
        self.x = self.j * 30 + 15
        self.y = self.i * 30 + 15

    #DIBUJAR PACMAN
    def draw_pacman(self,screen):
        pygame.draw.circle(screen,(255,255,0),(self.x,self.y),self.radius)
    
    #SELECTOR DE BUSQUEDA
    def search(self, screen):
        if not self.espinaca:
            return self.general_move(screen)
        else:
            win = self.general_move(screen)
            if(not win ):
               return self.general_move(screen) 
            else:
                return win
        

    #this funcition allow  execute the search to misspacman
    def general_search(self):
        # mirar si es meta
        # expandir
        #   verificar si mi movimiento es posible
        #   4 hijos (arriba, abajo, iz, der)
        #   esrtaria comprobando la posicion en i,j del nodo para sus movimientos

        # matriz de estaods local
        local_matrix = np.copy(mapa.matrix)
        genera_origen = True # si debo generar el origen o debo heredarlo

        #nodo de inicio
        nodo = Nodo((self.i,self.j),None,0,None)
        #cola por prioridad heuristica
        cola = []
        #condicion de quiebre
        iteerar = True
        # threee
        #arbol_pacman = Tree(player.visited)
        #arbol_pacman.printer("Pacman")
        

        self.arbol_panic.add_node (str(nodo))


        local_matrix[nodo.pos[0] ,nodo.pos[1] ] = "V"

        #iterar sobre la matriz 
        
        
        while(iteerar):

            # verificar si estoy en la meta
            if(mapa.matrix[ nodo.pos[0],nodo.pos[1] ] == "M" ):
                #print("DIRECCION",nodo.origin)
                iteerar = False
                return nodo.origin

            # expandir nodos (ENCOLAR)
            # ARRIBA 
            if(mapa.matrix[nodo.pos[0] - 1,nodo.pos[1] ] != "X" and mapa.matrix[nodo.pos[0] - 1,nodo.pos[1] ] != "G"):
                if(local_matrix[nodo.pos[0] - 1,nodo.pos[1] ] != "V"):
                    
                    #puedo explorar
                    # generar o heredar origen
                    if(genera_origen):
                        save_origen = "arriba"
                    else:
                        save_origen = nodo.origin

                    # heuristica condicional
                    if (self.A_start):
                        valor = self.get_heuristic((nodo.pos[0] - 1,nodo.pos[1]) ) + nodo.movC + self.costo_mov
                    else:
                        valor = self.get_heuristic((nodo.pos[0] - 1,nodo.pos[1]) )

                    #crear nbodo
                    nodoArr = Nodo((nodo.pos[0] - 1,nodo.pos[1] ),nodo,valor,save_origen)
                    #costo acomulado de moverse
                    nodoArr.movC = nodo.movC + self.costo_mov

                    # arbol
                    self.arbol_panic.add_node (str(nodoArr))
                    self.arbol_panic.add_edge(str(nodo),str(nodoArr))

                    #encolar INSERT SORT
                    cola = Nodo.insertN( nodoArr, cola)
                    #contador de colores
                    self.cont +=1
                    #visitar el nodo
                    local_matrix[nodo.pos[0] - 1,nodo.pos[1] ] = "V"

                    
                        

            # DERECHA 
            if(mapa.matrix[nodo.pos[0] ,nodo.pos[1] + 1 ] != "X" and mapa.matrix[nodo.pos[0] ,nodo.pos[1] +1] != "G"):
                if(local_matrix[nodo.pos[0] ,nodo.pos[1] + 1 ] != "V"):

                    #puedo explorar
                    # generar o heredar origen
                    if(genera_origen):
                        save_origen = "derecha"
                    else:
                        save_origen = nodo.origin

                    # heuristica condicional
                    if (self.A_start):
                        valor = self.get_heuristic((nodo.pos[0] ,nodo.pos[1] + 1) ) + nodo.movC + self.costo_mov
                    else:
                        valor = self.get_heuristic((nodo.pos[0] ,nodo.pos[1] + 1) )

                    #crear nbodo
                    nodoArr = Nodo((nodo.pos[0] ,nodo.pos[1] + 1),nodo,valor,save_origen)
                    #costo acomulado de moverse
                    nodoArr.movC = nodo.movC + self.costo_mov

                    # arbol
                    self.arbol_panic.add_node (str(nodoArr))
                    self.arbol_panic.add_edge(str(nodo),str(nodoArr))
                    
                    #encolar
                    cola = Nodo.insertN( nodoArr, cola)
                    #contador de colores
                    self.cont +=1
                    #visitar el nodo
                    local_matrix[nodo.pos[0] ,nodo.pos[1] + 1] = "V"
                        

            # ABAJO 
            if(mapa.matrix[nodo.pos[0] + 1,nodo.pos[1] ] != "X" and mapa.matrix[nodo.pos[0] + 1,nodo.pos[1] ] != "G"):
                if(local_matrix[nodo.pos[0] + 1,nodo.pos[1] ] != "V"):

                    #puedo explorar
                    # generar o heredar origen
                    if(genera_origen):
                        save_origen = "abajo"
                    else:
                        save_origen = nodo.origin

                    # heuristica condicional
                    if (self.A_start):
                        valor = self.get_heuristic((nodo.pos[0] + 1,nodo.pos[1]) ) + nodo.movC + self.costo_mov
                    else:
                        valor = self.get_heuristic((nodo.pos[0] + 1,nodo.pos[1] ) )

                    #crear nbodo
                    nodoArr = Nodo((nodo.pos[0] + 1,nodo.pos[1] ),nodo,valor,save_origen)
                    #costo acomulado de moverse
                    nodoArr.movC = nodo.movC + self.costo_mov

                    # arbol
                    self.arbol_panic.add_node (str(nodoArr))
                    self.arbol_panic.add_edge(str(nodo),str(nodoArr))
                    
                    #encolar
                    cola = Nodo.insertN( nodoArr, cola)
                    #contador de colores
                    self.cont +=1
                    #visitar el nodo
                    local_matrix[nodo.pos[0] + 1,nodo.pos[1] ] = "V"
               
            
            # IZQUIERDA 
            if(mapa.matrix[nodo.pos[0] ,nodo.pos[1] - 1 ] != "X" and mapa.matrix[nodo.pos[0] ,nodo.pos[1] - 1] != "G"):
                if(local_matrix[nodo.pos[0] ,nodo.pos[1] - 1 ] != "V"):
                                        
                    #puedo explorar
                    # generar o heredar origen
                    if(genera_origen):
                        save_origen = "izquierda"
                    else:
                        save_origen = nodo.origin

                    # heuristica condicional
                    if (self.A_start):
                        valor = self.get_heuristic((nodo.pos[0] ,nodo.pos[1] - 1) ) + nodo.movC + self.costo_mov
                    else:
                        valor = self.get_heuristic((nodo.pos[0] ,nodo.pos[1] - 1) )

                    #crear nbodo
                    nodoArr = Nodo((nodo.pos[0] ,nodo.pos[1] - 1),nodo,valor,save_origen)
                    #costo acomulado de moverse
                    nodoArr.movC = nodo.movC + self.costo_mov

                    # arbol
                    self.arbol_panic.add_node (str(nodoArr))
                    self.arbol_panic.add_edge(str(nodo),str(nodoArr))
                    
                    #encolar
                    cola = Nodo.insertN( nodoArr, cola)
                    #contador de colores
                    self.cont +=1
                    #visitar el nodo
                    local_matrix[nodo.pos[0] ,nodo.pos[1] - 1] = "V"
                    
            
            # print(local_matrix)
            # print(cola)
            # input()
            #en caso de que no se pueda mover porque no hay solucion
            if(cola == []):
                print("SIN salida")
                #iteerar = False
                return nodo.origin
            
            ## cambios iterativos
            nodo = cola[0] # se convierte en el primer nodo con prioridad
            genera_origen = False # se comienza a generar 
            cola = cola[1:] # resto de la cola


    # execute the move
    def general_move(self,screen):
        # se extrae el movimiento a realizar para llegar a la
        # solcuion

        #Restore the Misspacman position
        mapa.matrix[self.goal[0],self.goal[1]] = "M"
        #Restore the 

        self.visited.append((self.i, self.j))#nodos visitados
        direction = self.general_search()

        #limpiar pos anterior
        mapa.matrix[self.i,self.j] = " " 

        ## cambiar posicion
        if(direction ==  "arriba"):
            self.i -=1
        elif (direction ==  "abajo"):
            self.i +=1
        elif(direction ==  "izquierda"):
            self.j -=1
        elif(direction ==  "derecha"):
            self.j +=1
       
       
        #UPDATE
        # Cambia la variable estatica para mapa
        mapa.pacman = (self.i,self.j)  # -> ventaja, se utiliza para visualizar sin cargar

        # donde existe el pacman 
        # se coloca una 'P', para que el mapeo grafico lo 
        # reconozca
        mapa.matrix[self.i, self.j] = "P"
        if((self.i,self.j) == self.spinaca_positoin):
            self.espinaca = True
            mapa.espinaca_indicador = False

        #redimenciona las varialbes de dibujo
        self.update()

        if(self.graph_three):
            colors = ["red"] + ["blue"] * (self.cont-1) + ['yellow']
            nx.draw(self.arbol_panic,with_labels=True,node_color=colors)
            plt.draw()
            plt.show()
            # si se encuentra con el pacman o lo alcanza
            self.arbol_panic = None
            self.arbol_panic = nx.Graph()
            self.cont = 0


        if(self.i,self.j ) == self.goal:
            self.visited.append((self.i,self.j))
            return True
            

            
    #es distancia entre puntos divida en dos 
    # para prevenir la divicion que se realiza al 
    # tomar la espinaca
    def get_heuristic(self,coordinates):
        x_1 = self.goal[1]
        y_1 = self.goal[0]
        x_2 = coordinates[1]
        y_2 = coordinates[0]
        # distacia entre puntos
        distance = ((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2)
        distance = np.sqrt(distance)
        # return distance / 2
        if (self.A_start):
            # distancia a el fantasma
            x_1 = mapa.ghost[1]
            y_1 = mapa.ghost[0]
            x_2 = coordinates[1] 
            y_2 = coordinates[0]
            distancia_g = ((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2)
            distancia_g = np.sqrt(distancia_g)
            distance += distancia_g*2
            
        if(coordinates in self.visited):
            distance += 2
        #     #corrobora que el nodo no sea uno ya visitado si es un nodo visitado el costo de devolverse es mayor al movimiento normal
        return (distance/2.0)

   
