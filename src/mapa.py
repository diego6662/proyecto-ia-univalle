#imports
import pygame
import numpy as np
class mapa():
    """
    Podria tener 16 bloques de ancho y 24 a lo largo en bloques de 30x30px
    """
    # LECTURA DEL ARCHIVO
    wall = open("resources/mapa10.txt").read()
    #SPLITS THE COLS
    walls = wall.split("\n")
    # inicializa 
    row,column = len(walls) - 1,len(walls[0])
    #inicializar matriz de juego
    matrix = np.zeros((row,column),dtype = str)

    # statics de los personajes
    pacman = (0,0)
    ghost = (999,999)
    espinaca_indicador =True

    # ugualando el mapa cargado a el mapa generado
    for i in range(row):
        for j in range(column):
            matrix[i,j] = walls[i][j]

    def __init__(self):
        self.x_miss_pacman = None
        self.y_miss_pacman = None
        self.block = None
        self.espinaca = (0,0)

    def construir_mapa(self,walls,player,ghost):
        muros = []
        #posicion de la matriz sw subujo
        x = 0
        y = 0
        #posicion de la matriz real de estados
        iter_row = 0
        iter_col = 0

        #iteraciones
        for row in walls:
            for wall in row:
                # selectr de objetos para dibujo
                if wall == "X": #muros
                    muros.append(pygame.Rect(x,y,30,30))
                elif wall == "P":#pacman
                    player.x = x + 15
                    player.y = y + 15
                    player.i = iter_row
                    player.j = iter_col
                elif wall == "G":#fantasma
                    ghost.x = x + 15 
                    ghost.y = y + 15
                    ghost.i = iter_row
                    ghost.j = iter_col              
                elif wall == "M":#misspacman
                    player.goal = (iter_row,iter_col)
                    self.x_miss_pacman = x + 15
                    self.y_miss_pacman = y + 15
                elif wall == "S": #spinach
                    
                    self.espinaca=(x+15,y+15)
                    player.spinaca_positoin = (iter_row,iter_col)

                x += 30 # por el escalado 
                iter_col += 1
            
            x = 0
            iter_col = 0
            y += 30 # por el escalado
            iter_row += 1
        self.block = muros
    
    #dibujo de los muros
    def draw_wall(self,screen):
        for i in self.block:
            pygame.draw.rect(screen,(0,0,255),i)
        pygame.draw.circle(screen,(255,192,203),(self.x_miss_pacman,self.y_miss_pacman),10)        
        #pygame.draw.rect(screen,(69, 104, 4),(self.espinaca[0],self.espinaca[1],16, 20)) 
        if(mapa.espinaca_indicador):
            pygame.draw.polygon(screen,(59, 206, 0), [(self.espinaca[0] + 8,self.espinaca[1] + 8),(self.espinaca[0] - 8,self.espinaca[1] + 8),(self.espinaca[0] ,self.espinaca[1] -8)] )
               
        
