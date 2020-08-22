#imporsts
import numpy as np
import pygame
# load classs
from Player import Player
from mapa import mapa
from ghost import Ghost
from tree import Tree
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
            print("Pacman: Huuu!! I found you ...im making you el chicloso( ͡° ͜ʖ ͡°) \n Miss Pacman: ヽ(＾Д＾)ﾉ")
            break
        if loose:
            print("Game over")
            break
        if not scream:
            #probabilidad 
            scream_number = np.random.randint(1, 11)
            scream_probability =  scream_number <= 3 
            if scream_probability:
                player.A_start = True
                screen.blit(text,(0,0))
                print(miss_pacman_dialog,trya)
                scream = True
                pygame.display.update()
                pygame.time.delay(2500)
        
        trya += 1
        
        # move pacman
        
        win = player.search(screen)
        # move gosth
        loose = ghost.uniform_move(screen)
        
        
        # seccion de dibujo
        screen.fill(BLACK)
        player.update()
        ghost.update()
        mapa_game.draw_wall(screen)
        player.draw_pacman(screen)
        ghost.draw_ghost(screen)
        pygame.display.update()

        pygame.time.delay(300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #input()
    arbol_pacman = Tree(player.visited)
    arbol_pacman.printer("Pacman")
    arbol_ghost = Tree(ghost.visited)
    arbol_ghost.printer("Fantasma")
    quit()     
    # MAIN
if __name__ == "__main__":
    main()
