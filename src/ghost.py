#imports 
import pygame # allow graphic interfaz
import numpy as np # allow manager Matrix and use aritmethic operatios

#internal import to use the mapa
# como se importa mapa
# las variables estaticas de el se convierten en globales
# para que los objetos las visualicen

from mapa import mapa
from Nodo import Nodo # import the represento to generater the audio 


"""
    this class represent the Ghost enemy:
    implement srch: costo uniforme
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
    

    ## this function updte the position
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
        pygame.draw.circle(screen,(0,255,255),(self.x, self.y),10)
        pygame.draw.rect(screen,(0,255,255),(self.x - 10, self.y - 4,20,14))
   

    """
    Recibe: 
        nodo: Nodo - el nodo que se quiere expandir
        origen: boolean - si se puede heredar el origen
        cola: lista - es la cola de tipo prioridad
    
    Proposito:
        Debe devolver el origen del movimiento que da como resultado el 
        hallazgo de la meta
    
    """
    def uniform_search(self):
        # mirar si es meta
        # expandir
        #   verificar si mi movimiento es posible
        #   4 hijos (arriba, abajo, iz, der)
        #   esrtaria comprobando la posicion en ij del nodo para sus movimientos

        # matriz de estaods local
        local_matrix = np.copy( mapa.matrix)
        genera_origen = True # si debo generar el origen o debo heredarlo

        #nodo de inicio
        nodo = Nodo((self.i,self.j),None,0,None)
        #cola por prioridad
        cola = []
        #condicion de quiebre
        iteerar = True
        
        #iterar sobre la matriz 
        while(iteerar):

            # verificar si estoy en la meta
            if(mapa.matrix[nodo.pos[0],nodo.pos[1] ] == "P" ):
                
                iteerar = False
                return nodo.origin

            # expandir nodos (ENCOLAR)
            # ARRIBA 
            if(mapa.matrix[nodo.pos[0] - 1,nodo.pos[1] ] != "X"):
                if(local_matrix[nodo.pos[0] - 1,nodo.pos[1] ] != "V"):
                    
                    #puedo explorar
                    if(genera_origen):
                        cola = Nodo.insertN( Nodo((nodo.pos[0] - 1,nodo.pos[1] ),nodo,nodo.valAc + 1,"arriba"), cola)
                    else:
                        cola = Nodo.insertN( Nodo((nodo.pos[0] - 1,nodo.pos[1] ),nodo,nodo.valAc + 1,nodo.origin), cola)
                    #visitar el nodo
                    local_matrix[nodo.pos[0] - 1,nodo.pos[1] ] = "V" 
                        

            # DERECHA 
            if(mapa.matrix[nodo.pos[0] ,nodo.pos[1] + 1 ] != "X"):
                if(local_matrix[nodo.pos[0] ,nodo.pos[1] + 1 ] != "V"):

                    #puedo explorar
                    if(genera_origen):
                        cola = Nodo.insertN( Nodo((nodo.pos[0] ,nodo.pos[1] + 1),nodo,nodo.valAc + 1,"derecha"), cola)
                    else:
                        cola = Nodo.insertN( Nodo((nodo.pos[0] ,nodo.pos[1] + 1),nodo,nodo.valAc + 1,nodo.origin), cola)
                    #visitar el nodo
                    local_matrix[nodo.pos[0] ,nodo.pos[1] + 1] = "V" 
                        

            # ABAJO 
            if(mapa.matrix[nodo.pos[0] + 1,nodo.pos[1] ] != "X"):
                if(local_matrix[nodo.pos[0] + 1,nodo.pos[1] ] != "V"):

                    #puedo explorar
                    if(genera_origen):
                        cola = Nodo.insertN( Nodo((nodo.pos[0] + 1,nodo.pos[1] ),nodo,nodo.valAc + 1,"abajo"), cola)
                    else:
                        cola = Nodo.insertN( Nodo((nodo.pos[0] + 1,nodo.pos[1] ),nodo,nodo.valAc + 1,nodo.origin), cola)
                    #visitar el nodo
                    local_matrix[nodo.pos[0] + 1,nodo.pos[1]] = "V" 
                    
                        
            
            # IZQUIERDA 
            if(mapa.matrix[nodo.pos[0] ,nodo.pos[1] - 1 ] != "X"):
                if(local_matrix[nodo.pos[0] ,nodo.pos[1] - 1 ] != "V"):
                                        
                    #puedo explorar
                    if(genera_origen):
                        cola = Nodo.insertN( Nodo((nodo.pos[0] ,nodo.pos[1] - 1),nodo,nodo.valAc + 1,"izquierda"), cola)
                    else:
                        cola = Nodo.insertN( Nodo((nodo.pos[0] ,nodo.pos[1] - 1),nodo,nodo.valAc + 1,nodo.origin), cola)
                    #visitar el nodo
                    local_matrix[nodo.pos[0] ,nodo.pos[1] - 1] = "V" 
            

            #en caos de que no se pueda mover porque no hay solucion
            if(cola == []):
                print("SIN salida")
                #iteerar = False
                return ""
            
            ## cambios iterativos
            nodo = cola[0] # se convierte en el primer nodo con prioridad
            genera_origen = False # se comienza a generar 
            cola = cola[1:] # resto de la cola

    #movimiento 
    """
    Recibe:
        
    Proposito: mover al dantasma una casilla con respecto a la solución encontrada
    """
    def uniform_move(self,screen):
        # se extrae el movimiento a realizar para llegar a lka
        # solcuion
        
        direction = self.uniform_search()

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
        mapa.ghost = (self.i,self.j)  # -> ventaja, se utiliza para visualizar sin cargar

        # donde existe el fantasma 
        # se coloca una 'G', para que el mapeo grafico lo 
        # reconozca
        mapa.matrix[self.i, self.j] = "G"

        #redimenciona las varialbes de dibujo
        self.x = self.j * 30 + 15
        self.y = self.i * 30 + 15

        # si se encuentra con el pacman o lo alcanza
        
        return (self.i,self.j ) == mapa.pacman
            