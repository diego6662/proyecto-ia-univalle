import numpy as np
import pygame
from Player import Player
from mapa import mapa
from ghost import Ghost
def main():
    successes, failures = pygame.init()
    print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))
    screen = pygame.display.set_mode((720, 480))
    wall = open("/home/diego/Desktop/universidad/7-semestre/IA/proyecto/resources/mapa1.txt").read()
    walls = wall.split("\n")
    clock = pygame.time.Clock()
    row,column = len(walls) - 1,len(walls[0])
    matrix = np.zeros((row,column),dtype = str)
    for i in range(row):
        for j in range(column):
            matrix[i,j] = walls[i][j]
    FPS = 60
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    player = Player(matrix)
    ghost = Ghost(matrix) 
    mapa_game = mapa()
    mapa_game.construir_mapa(walls,player,ghost)

    running = True
    while running:
        clock.tick(FPS)
        screen.fill(BLACK)        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update()
       
        pygame.time.delay(30)
        mapa_game.draw_wall(screen)
        pygame.time.delay(30)
        player.draw_pacman(screen)
        #ghost.draw_ghost(screen)
        pygame.time.delay(30)
        pygame.display.update()
        pygame.time.delay(30)
        player.greedy_search()
    quit() 
if __name__ == "__main__":
    main()
