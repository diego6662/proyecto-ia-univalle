#imports 
import pygame # allow graphic interfaz
import numpy as np # allow manager Matrix and use aritmethic operatios

#internal import to use the mapa
# como se importa mapa
# las variables estaticas de el se convierten en globales
# para que los objetos las visualicen

from mapa import mapa


"""
    this class represent the Ghost enemy:
    implement srch: 
"""
class Ghost():
    def __init__(self):
        # la inicion el fantasma no posee posicion
        self.x = None
        self.y = None
        self.i = None
        self.j = None

        ## nodos viditados
        self.visited = []
    

    ## this function updte 
    ## (number, number) -> 
    ## copia 
    def update_space(self,i = 0,j = 0):
        # limpia la posición con respecto a la posicion 
        # presente para cambiarla
        mapa.matrix[self.i,self.j] = " " 

        # Actualzia las cordenadas con los parametros 
        # que se reciben
        self.i = i
        self.j = j

        # Cambia la variable estatica para mapa
        mapa.ghost = (self.i,self.j)  # -> ventaja, se utiliza para visualizar sin cargar

        # donde existe el fantasma 
        # se coloca una 'G', para que el mapeo grafico lo 
        # reconozca
        mapa.matrix[self.i, self.j] = "G"


    # genera el escalado para el dibujo en la parte grafica 
    # dandole al fantasma un perimetor de 30x30 y centrando su posicion
    def update(self):
        self.x = self.j * 30 + 15
        self.y = self.i * 30 + 15

    # Dibuja el fantasma en el mapa
    def draw_ghost(self, screen):
        #pygame.draw.circle(screen,(0,255,255),(self.x, self.y),10)
        pygame.draw.rect(screen,(0,255,255),(self.x - 5, self.y - 5,20,20))
    
    # Implement the deep search 
    def deep_search(self,i = None,j = None,recursion = None):        
        if i == None and j == None:
            
            i,j = self.i,self.j
            self.visited.append((i,j))
            possibility = [(i,j - 1),(i,j + 1),(i - 1,j),(i + 1,j)]
            deep_walk = [self.deep_move(possibility[0]),self.deep_move(possibility[1]) + 1,self.deep_move(possibility[2]) + 2,self.deep_move(possibility[3]) + 3]
            minimun = None
            index = None
            for i in range(4):
                if minimun == None:
                    minimun = deep_walk[i]
                    index = i
                elif deep_walk[i] < minimun:
                    minimun = deep_walk[i]
                    index = i
            if mapa.matrix[possibility[index][0],possibility[index][1]] == "P":
                self.update_space(possibility[index][0],possibility[index][1])
                return True
            self.update_space(possibility[index][0],possibility[index][1])
            return False
        else:
            possibility = [(i,j - 1),(i,j + 1),(i - 1,j),(i + 1,j)]
            deep_walk = [self.deep_move(possibility[0],recursion - 1),self.deep_move(possibility[1],recursion - 1) + 1,self.deep_move(possibility[2],recursion - 1) + 2,self.deep_move(possibility[3],recursion - 1) + 3]
            minimun = None
            index = None
            for i in range(4):
                if minimun == None:
                    minimun = deep_walk[i]
                    index = i
                elif deep_walk[i] < minimun:
                    minimun = deep_walk[i]
                    index = i
            return minimun 


    def deep_move(self,coordinates,recursion = 8):
        if recursion == 0:
            if (coordinates in self.visited):
                return 99
            elif mapa.matrix[coordinates[0],coordinates[1]] == 'X':
                return 9999
            else:
                return 1
        else:
            #if mapa.matrix[coordinates[0], coordinates[1]] == 'P':
             #   return -999999
            if (coordinates in self.visited):
                return 99 + self.deep_search(coordinates[0],coordinates[1],recursion)
            elif mapa.matrix[coordinates[0],coordinates[1]] == 'X':
                return 9999
            else:
                return 1 + self.deep_search(coordinates[0],coordinates[1],recursion)
 
 
