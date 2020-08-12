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
    font = pygame.font.Font(None,30)
    miss_pacman_dialog = f"Pacman estoy en {player.goal},si me salvas puedes hacerme el ¡DELICIOSO!"
    text = font.render(miss_pacman_dialog,0,WHITE)
    running = True
    win,loose = False,False
    scream = False
    trya = 1 
    while running:
        clock.tick(FPS)
        screen.fill(BLACK)        
        mapa_game.draw_wall(screen)
        if win:
            break
        if loose:
            print("Game over")
            break
        if not scream:
            scream_number = np.random.randint(1, 10)
            scream_probability = True if scream_number <= 3 else False
            if scream_probability:
                player.A_start = True
                screen.blit(text,(0,0))
                print(miss_pacman_dialog,trya)
                scream = True
                pygame.display.update()
                pygame.time.delay(2500)
        trya += 1
        player.update()
        ghost.update()
        #pygame.time.delay(30)
        #pygame.time.delay(30)
        player.draw_pacman(screen)
        ghost.draw_ghost(screen)
        #pygame.time.delay(30)
        pygame.display.update()
        pygame.time.delay(30)
        win = player.search()
        player.update()
        loose = ghost.deep_search()
        screen.fill(BLACK)
        
        ghost.update()
        
        pygame.time.delay(30)
        mapa_game.draw_wall(screen)
        player.draw_pacman(screen)
        ghost.draw_ghost(screen)
        pygame.display.update()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    quit() 
if __name__ == "__main__":
    main()
