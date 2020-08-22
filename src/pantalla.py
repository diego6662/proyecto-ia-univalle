#imporsts
import numpy as np
import pygame
# load classs
from Player import Player
from mapa import mapa
from ghost import Ghost

# main
def main():
    # load, screeem
    successes, failures = pygame.init()
    screen = pygame.display.set_mode((720, 480))
    # temporizadores
    clock = pygame.time.Clock()
    FPS = 60 

    #colores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    #objetos de uso
    player = Player() #pacman
    ghost = Ghost() #fantasma
    mapa_game = mapa() # mapa
    mapa_game.construir_mapa(mapa.matrix,player,ghost) #cargar el mapa
    #letreros
    font = pygame.font.Font(None,30)
    miss_pacman_dialog = f"Pacman estoy en {player.goal},si me salvas puedes hacerme el ¡SIN RESPETO!"
    text = font.render(miss_pacman_dialog,0,WHITE)
    # STARTING
    running = True
    win,loose = False,False
    scream = False
    # INIT REFRESH RATE
    clock.tick(FPS)
   
    
    trya = 1 # EN QUE INTERACCION GRITA 
    # INTERACCIONES
    clock.tick(FPS)

    while running:
        # Secion de dibujo
        screen.fill(BLACK)        
        mapa_game.draw_wall(screen)
        player.update()
        ghost.update()
        player.draw_pacman(screen)
        ghost.draw_ghost(screen)
        pygame.display.update()

        if win:
            break
        if loose:
            print("Game over")
            break
        if not scream:
            #probabilidad 
            scream_number = np.random.randint(1, 1000)
            scream_probability =  100 <= 30 
            if scream_probability:
                player.A_start = True
                screen.blit(text,(0,0))
                print(miss_pacman_dialog,trya)
                scream = True
                pygame.display.update()
                pygame.time.delay(2500)
        
        trya += 1
        
       
        win = player.search()
        player.update()
        
        loose = ghost.uniform_move(screen)
        screen.fill(BLACK)
        
        ghost.update()
        mapa_game.draw_wall(screen)
        player.draw_pacman(screen)
        ghost.draw_ghost(screen)
        pygame.display.update()

        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #input()
    quit()     
    # MAIN
if __name__ == "__main__":
    main()
