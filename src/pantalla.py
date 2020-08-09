import numpy as np
import pygame
from Player import Player
from mapa import mapa
from ghost import Ghost
def main():
    successes, failures = pygame.init()
    screen = pygame.display.set_mode((720, 480))
    clock = pygame.time.Clock()
    FPS = 60 
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
        
        player.update()
        ghost.update()
        pygame.time.delay(30)
        mapa_game.draw_wall(screen)
        #pygame.time.delay(30)
        player.draw_pacman(screen)
        ghost.draw_ghost(screen)
        #pygame.time.delay(30)
        pygame.display.update()
        pygame.time.delay(30)
        if player.x == ghost.x and player.y == ghost.y:
            
            loose = True
        
        win = player.greedy_search()
        player.update()
        loose = ghost.deep_search()
        screen.fill(BLACK)
        if player.x == ghost.x and player.y == ghost.y:
            
            loose = True
        
        ghost.update()
        if player.x == ghost.x and player.y == ghost.y:
            
            loose = True
        
        pygame.time.delay(30)
        mapa_game.draw_wall(screen)
        player.draw_pacman(screen)
        ghost.draw_ghost(screen)
        pygame.display.update()
        if win:
            break
        if loose:
            print("Game over")
            break
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    quit() 
if __name__ == "__main__":
    main()
