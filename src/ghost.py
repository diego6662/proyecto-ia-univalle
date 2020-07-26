import pygame
import numpy as np

class Ghost(pygame.sprite.Sprite):
    def __init__(self,space):
        super().__init__
        self.x = None
        self.y = None
        self.i = None
        self.j = None
        self.velocity_x = 0
        self.velocity_y = 0
        self.image = None
        self.space = space
    def update_space(self,i = 0,j = 0):
        self.space[self.i,self.j] = " "
        self.i += i
        self.j += j
        self.space[self.i, self.j] = "G"
    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.image = pygame.Rect(self.x - 10,self.y - 10,20,20)
    def draw_ghost(self, screen,move = None):
        if move == None: 
            pygame.draw.circle(screen,(0,0,100),(self.x, self.y),10)
        
