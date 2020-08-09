import pygame
import numpy as np
from mapa import mapa
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = None
        self.y = None
        self.i = None
        self.j = None
        self.goal = None
        self.radius = 10
        self.velocity_x = 0
        self.velocity_y = 0
        
     
    def update_space(self,i = 0,j = 0):
        mapa.matrix[self.i,self.j] = " "
        self.i = i
        self.j = j
        mapa.pacman = (self.i, self.j)
        mapa.matrix[self.i, self.j] = "P"

    def return_space(self):
        return self.space

    def change_space(self,space):
        self.space = space

    def update(self):
        self.x = self.j * 30 + 15
        self.y = self.i * 30 + 15

    def draw_pacman(self,screen,direction = None,i_move = 1, j_move = 1):
        pygame.draw.circle(screen,(255,255,0),(self.x,self.y),self.radius)
     
    def greedy_search(self,i = None,j = None,recursion = None):
        if i == None and j == None:
            i,j = self.i, self.j
            if i == self.goal[0] and j == self.goal[1] :
                print("you found a miss pacman")
                return True
            possiblilyties = [(i,j - 1),(i,j + 1),(i - 1,j),(i + 1,j)]
            best_way = [self.heuristic(possiblilyties[0]),self.heuristic(possiblilyties[1]),self.heuristic(possiblilyties[2]),self.heuristic(possiblilyties[3])]
             
            minimun = None
            index = None
            for ite in range(4):
                if minimun == None:
                    minimun = best_way[ite]
                    index = ite
                elif best_way[ite] < minimun :
                    minimun = best_way[ite]
                    index = ite
        
            self.update_space(possiblilyties[index][0],possiblilyties[index][1])
            return False        
        else:
            if i == self.goal[0] and j == self.goal[1]:
                return -999999
            possiblilyties = [(i,j - 1),(i,j + 1), (i - 1,j),(i + 1,j)]
            best_way = [self.heuristic(possiblilyties[0],recursion - 1),self.heuristic(possiblilyties[1],recursion - 1),self.heuristic(possiblilyties[2],recursion - 1),self.heuristic(possiblilyties[3],recursion - 1)]
            
            minimun = None
            index = None
            for ite in range(4):
                if minimun == None:
                    minimun = best_way[ite]
                    index = ite
                elif best_way[ite] < minimun :
                    minimun = best_way[ite]
                    index = ite
        
            return minimun

            

<<<<<<< HEAD
    def heuristic(self,coordinates,recursion = 4):
=======
    def heuristic(self,coordinates,recursion = 7):
>>>>>>> 32c821da84051cf26311b892e0064b346441fc22
        if recursion == 0:
            if mapa.matrix[coordinates[0], coordinates[1]] == "X":
                return 99999

            x_1 = self.goal[1]
            y_1 = self.goal[0]
            x_2 = coordinates[1]
            y_2 = coordinates[0]
            distance = ((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2)
            distance = np.sqrt(distance)
            return distance
        else:
            
            if mapa.matrix[coordinates[0], coordinates[1]] == 'X':
                return 99999

            return self.greedy_search(coordinates[0],coordinates[1],recursion)


