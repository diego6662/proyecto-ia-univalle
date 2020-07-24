import pygame
import numpy as np
class Player(pygame.sprite.Sprite):
    def __init__(self,space):
        super().__init__()
        self.x = None
        self.y = None
        self.i = None
        self.j = None
        self.radius = 10
        self.velocity_x = 0
        self.velocity_y = 0
        self.image = None 
        self.space = space
    def update_space(self,i = 0,j = 0):
        self.space[self.i,self.j] = " "
        self.i += i
        self.j += j
        self.space[self.i, self.j] = "P"
    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.image = pygame.Rect(self.x - 10,self.y - 10,20,20)
        
    def draw_pacman(self,screen,direction = None):
        if direction == None:
            pygame.draw.circle(screen,(255,255,0),(self.x,self.y),self.radius)
        elif direction == "up":
            pygame.draw.circle(screen,(255,255,0),(self.x,self.y),self.radius)
            pygame.draw.polygon(screen,(0,0,0),[[self.x,self.y],[self.x - 5,self.y - 10],[self.x + 5,self.y - 10]])
            self.update_space(i = -1)
        elif direction == "down":
            pygame.draw.circle(screen,(255,255,0),(self.x,self.y),self.radius)
            pygame.draw.polygon(screen,(0,0,0),[[self.x,self.y],[self.x - 5,self.y + 10],[self.x + 5,self.y + 10]])
            self.update_space(i = 1)
        elif direction == "left":
            pygame.draw.circle(screen,(255,255,0),(self.x,self.y),self.radius)
            pygame.draw.polygon(screen,(0,0,0),[[self.x,self.y],[self.x - 10,self.y + 5],[self.x - 10,self.y - 5]])
            self.update_space(j = -1)
        elif direction == "rigth":
            pygame.draw.circle(screen,(255,255,0),(self.x,self.y),self.radius)
            pygame.draw.polygon(screen,(0,0,0),[[self.x,self.y],[self.x + 10,self.y + 5],[self.x + 10,self.y - 5]])
            self.update_space(j = 1)
        pygame.display.update()
        pygame.time.delay(8)
        pygame.draw.circle(screen,(255,255,0),(self.x,self.y),self.radius)

        
