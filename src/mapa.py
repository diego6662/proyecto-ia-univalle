import pygame
import numpy as np
class mapa():
    """
    Podria tener 16 bloques de ancho y 24 a lo largo en bloques de 30x30
    """
    wall = open("resources/mapa4.txt").read()
    walls = wall.split("\n")
    row,column = len(walls) - 1,len(walls[0])
    matrix = np.zeros((row,column),dtype = str)
    pacman = (0,0)
    ghost = (999,999)
    for i in range(row):
        for j in range(column):
            matrix[i,j] = walls[i][j]

    def __init__(self):
        self.x_miss_pacman = None
        self.y_miss_pacman = None
        self.block = None
        
    def construir_mapa(self,walls,player,ghost):
        muros = []
        x = 0
        y = 0
        iter_row = 0
        iter_col = 0
        for row in walls:
            for wall in row:
                if wall == "X":
                    muros.append(pygame.Rect(x,y,30,30))
                elif wall == "P":
                    player.x = x + 15
                    player.y = y + 15
                    player.i = iter_row
                    player.j = iter_col
                elif wall == "G":
                    ghost.x = x + 15 
                    ghost.y = y + 15
                    ghost.i = iter_row
                    ghost.j = iter_col
                elif wall == "M":
                    player.goal = (iter_row,iter_col)
                    self.x_miss_pacman = x + 15
                    self.y_miss_pacman = y + 15
                x += 30 
                iter_col += 1
            x = 0
            iter_col = 0
            y += 30
            iter_row += 1
        self.block = muros
    def draw_wall(self,screen):
        for i in self.block:
            pygame.draw.rect(screen,(0,0,255),i)
        pygame.draw.circle(screen,(255,192,203),(self.x_miss_pacman,self.y_miss_pacman),10)       
