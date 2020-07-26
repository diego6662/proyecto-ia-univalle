import pygame
import numpy as np
class Player(pygame.sprite.Sprite):
    def __init__(self,space):
        super().__init__()
        self.x = None
        self.y = None
        self.i = None
        self.j = None
        self.goal = None
        self.radius = 10
        self.velocity_x = 0
        self.velocity_y = 0
        self.space = space
    def update_space(self,i = 0,j = 0):
        self.space[self.i,self.j] = " "
        self.i += i
        self.j += j
        self.space[self.i, self.j] = "P"
    def update(self):
        self.x = self.j * 30 + 15
        self.y = self.i * 30 + 15
    def draw_pacman(self,screen,direction = None,i_move = 1, j_move = 1):
        pygame.draw.circle(screen,(255,255,0),(self.x,self.y),self.radius)
     
    def greedy_search(self):
        i,j = self.i, self.j
        if i == self.goal[0] and j == self.goal[1] :
            print("you found a miss pacman")
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
        self.i = possiblilyties[index][0]
        self.j = possiblilyties[index][1]
                


    def heuristic(self,coordinates):
        if self.space[coordinates[0],coordinates[1]] == "X":
            return 99999

        x_1 = self.goal[1]
        y_1 = self.goal[0]
        x_2 = coordinates[1]
        y_2 = coordinates[0]
        distance = ((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2)
        distance = np.sqrt(distance)
        return distance
