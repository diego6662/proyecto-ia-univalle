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
        self.A_start = False 
        self.visited = []
        self.visited_a_start = []
    def update_space(self,i = 0,j = 0):
        mapa.matrix[self.i,self.j] = " "
        self.i = i
        self.j = j
        mapa.pacman = (self.i, self.j)
        mapa.matrix[self.i, self.j] = "P"

    def update(self):
        self.x = self.j * 30 + 15
        self.y = self.i * 30 + 15

    def draw_pacman(self,screen):
        pygame.draw.circle(screen,(255,255,0),(self.x,self.y),self.radius)
    
    def search(self):
        if self.A_start:
            return self.A_Start()
        else:
            return self.greedy_search()
    
    def A_Start(self,i = None,j = None,recursion = None):
        if i == None and j == None:
            i, j = self.i,self.j
            if i == self.goal[0] and j == self.goal[1]:
                print("you found a miss pacman")
                return True
            self.visited.append((i,j))
            possiblilyties = [(i,j - 1),(i,j + 1),(i - 1,j),(i + 1,j)]
            routes = [self.A_start_implementation(possiblilyties[0]),self.A_start_implementation(possiblilyties[1]),self.A_start_implementation(possiblilyties[2]),self.A_start_implementation(possiblilyties[3])]
            print(routes)
            minumun = None
            index = None
            for i in range(4):
                if minumun == None:
                    minumun = routes[i]
                    index = i
                elif routes[i] < minumun:
                    minumun = routes[i]
                    index = i
            self.update_space(possiblilyties[index][0],possiblilyties[index][1])
            self.visited_a_start = []
            return False
        else:
            self.visited_a_start.append((i,j))
            possiblilyties = [(i,j - 1),(i,j + 1),(i - 1,j),(i + 1,j)]
            routes = [self.A_start_implementation(possiblilyties[0],recursion - 1),self.A_start_implementation(possiblilyties[1], recursion - 1),self.A_start_implementation(possiblilyties[2], recursion - 1),self.A_start_implementation(possiblilyties[3],recursion - 1)]
            minumun = None
            for i in range(4):
                if routes[i] >= 9999999999:
                    minumun = routes[i]
                    break
                if minumun == None:
                    minumun = routes[i]
                elif routes[i] < minumun:
                    minumun = routes[i]
            return minumun

    def A_start_implementation(self,coordinates,recursion=5):
        if recursion == 0:
            if coordinates == self.goal:
                return -9999999  
            elif mapa.matrix[coordinates[0],coordinates[1]] == 'G':
                return 9999999999 
            
            elif mapa.matrix[coordinates[0],coordinates[1]] == "X":
                return 9999999 

            elif coordinates in self.visited:
                return 99 + self.heuristic(coordinates,0)
            else:
                return 1 + self.heuristic(coordinates,0)
        else:

            if coordinates == self.goal:
                return  -9999999 
            elif mapa.matrix[coordinates[0],coordinates[1]] == 'G':
                return  9999999999
            elif mapa.matrix[coordinates[0],coordinates[1]] == "X":
                return 9999999 

            elif coordinates in self.visited:
                return (99 + self.heuristic(coordinates,0) + self.A_Start(coordinates[0],coordinates[1],recursion))
            else:
                return (1 + self.heuristic(coordinates,0) + self.A_Start(coordinates[0],coordinates[1],recursion))

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
           #corregir busqueda avara esta explorando nodos innecesarios 
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

            

    def heuristic(self,coordinates,recursion = 4):
        if recursion == 0:
            if mapa.matrix[coordinates[0], coordinates[1]] == "X":
                return 999999

            x_1 = self.goal[1]
            y_1 = self.goal[0]
            x_2 = coordinates[1]
            y_2 = coordinates[0]
            distance = ((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2)
            distance = np.sqrt(distance)
            return distance
        else:
            
            if mapa.matrix[coordinates[0], coordinates[1]] == 'X':
                return 999999

            x_1 = self.goal[1]
            y_1 = self.goal[0]
            x_2 = coordinates[1]
            y_2 = coordinates[0]
            distance = ((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2)
            distance = np.sqrt(distance)
            return distance + self.greedy_search(coordinates[0],coordinates[1],recursion)


