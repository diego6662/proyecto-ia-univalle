import pygame
import numpy as np
from mapa import mapa
class Ghost(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__
        self.x = None
        self.y = None
        self.i = None
        self.j = None
        self.visited = []
        
    def update_space(self,i = 0,j = 0):
        mapa.matrix[self.i,self.j] = " "
        self.i = i
        self.j = j
        mapa.ghost = (self.i,self.j) 
        mapa.matrix[self.i, self.j] = "G"
    def return_space(self):
        return self.space
    def change_space(self,space):
        self.space = space
    def update(self):
        self.x = self.j * 30 + 15
        self.y = self.i * 30 + 15
    def draw_ghost(self, screen,move = None):
        pygame.draw.circle(screen,(0,255,255),(self.x, self.y),10)
       
    def deep_search(self,i = None,j = None,recursion = None):
        if i == None and j == None:
            i,j = self.i,self.j
            if i == mapa.pacman[0] and j == mapa.pacman[1]:
                print('game over')
                return True
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


    def deep_move(self,coordinates,recursion = 7):
        if recursion == 0:
            if mapa.matrix[coordinates[0], coordinates[1]] == 'P':
                return -999999
            elif (coordinates in self.visited):
                return 99
            elif mapa.matrix[coordinates[0],coordinates[1]] == 'X':
                return 9999
            else:
                return 1
        else:
            if mapa.matrix[coordinates[0], coordinates[1]] == 'P':
                return -999999
            elif (coordinates in self.visited):
                return 99 + self.deep_search(coordinates[0],coordinates[1],recursion)
            elif mapa.matrix[coordinates[0],coordinates[1]] == 'X':
                return 9999
            else:
                return 1 + self.deep_search(coordinates[0],coordinates[1],recursion)
 
 
