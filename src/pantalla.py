import numpy as np
import pygame
from Player import Player
from mapa import mapa
from ghost import Ghost
def main():
    successes, failures = pygame.init()
    screen = pygame.display.set_mode((720, 480))
<<<<<<< HEAD
=======
    #wall = open ("/home/daniel/Escritorio/IA/resources/mapa1.txt")
    wall = open("/home/diego/Desktop/universidad/7-semestre/IA/proyecto/resources/mapa1.txt").read()
    walls = wall.split("\n")
>>>>>>> 14316bc3fd7114f423d90cb2b6008f8959d70b5e
    clock = pygame.time.Clock()
<<<<<<< HEAD
    FPS = 60
=======
    FPS = 60 
>>>>>>> 32c821da84051cf26311b892e0064b346441fc22
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    player = Player()
    ghost = Ghost() 
    mapa_game = mapa()
    mapa_game.construir_mapa(mapa.matrix,player,ghost)
    
    running = True
    win,loose = False,False
    while running:
        clock.tick(FPS)
        screen.fill(BLACK)        
        if win:
            break
        if loose:
            break
        
        player.update()
        ghost.update()
        pygame.time.delay(30)
        mapa_game.draw_wall(screen)
        #pygame.time.delay(30)
<<<<<<< HEAD
        player.draw_pacman(screen)
        ghost.draw_ghost(screen)
        #pygame.time.delay(30)
        pygame.display.update()
        #pygame.time.delay(30)
        win = player.greedy_search()
        loose = ghost.deep_search()
        screen.fill(BLACK)
        player.update()
        ghost.update()
        #pygame.time.delay(30)
        mapa_game.draw_wall(screen)
        player.draw_pacman(screen)
        ghost.draw_ghost(screen)
        pygame.display.update()
=======
        player.draw_pacman(screen)
        ghost.draw_ghost(screen)
        #pygame.time.delay(30)
        pygame.display.update()
        pygame.time.delay(30)
        win = player.greedy_search()
        loose = ghost.deep_search()
        screen.fill(BLACK)
        player.update()
        ghost.update()
        pygame.time.delay(30)
        mapa_game.draw_wall(screen)
        player.draw_pacman(screen)
        ghost.draw_ghost(screen)
        pygame.display.update()
>>>>>>> 32c821da84051cf26311b892e0064b346441fc22
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    quit() 
if __name__ == "__main__":
    main()
