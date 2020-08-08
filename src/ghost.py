import pygame
import numpy as np

class Ghost(pygame.sprite.Sprite):
    def __init__(self,space):
        super().__init__
        self.x = None
        self.y = None
        self.i = None
        self.j = None
        self.visited = []
        self.space = space
    def update_space(self,i = 0,j = 0):
        self.space[self.i,self.j] = " "
        self.i = i
        self.j = j
        self.space[self.i, self.j] = "G"
    def return_space(self):
        return self.space
    def change_space(self,space):
        self.space = space
    def update(self):
        self.x = self.j * 30 + 15
        self.y = self.i * 30 + 15
    def draw_ghost(self, screen,move = None):
        pygame.draw.circle(screen,(0,255,255),(self.x, self.y),10)
       
    def deep_search(self):
        i,j = self.i,self.j
        self.visited.append((i,j))
        if self.space[i,j] == 'P':
            print('Game over')
            return True
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
    def deep_move(self,coordinates):
        if (coordinates in self.visited) or self.space[coordinates[0],coordinates[1]] == 'X':
            return 999
        else:
            return 1
