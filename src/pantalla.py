import pygame
from Player import Player
from mapa import mapa
successes, failures = pygame.init()
print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))
screen = pygame.display.set_mode((720, 480))
wall = open("/home/diego/Desktop/universidad/7-semestre/IA/proyecto/resources/mapa1.txt").read()
walls = wall.split("\n")
clock = pygame.time.Clock()
mapa_game = mapa()
mapa_game.construir_mapa(walls)


FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
player = Player()

running = True
while running:
    clock.tick(FPS)# Returns milliseconds between each call to 'tick'. The convert time to seconds.
    screen.fill(BLACK) # Fill the screen with background color.
    
    
    
    for event in pygame.event.get():
        movement = None
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                movement = "up"
                player.velocity_y -= 6 
            elif event.key == pygame.K_s:
                movement = "down"
                player.velocity_y += 6
            elif event.key == pygame.K_a:
                movement = "left"
                player.velocity_x -= 6
            elif event.key == pygame.K_d:
                movement = "rigth"
                player.velocity_x += 6
        elif  event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
               
                player.velocity_y = 0 
            elif event.key == pygame.K_s:
                
                player.velocity_y = 0
            elif event.key == pygame.K_a:
                
                player.velocity_x = 0
            elif event.key == pygame.K_d:
                
                player.velocity_x = 0 
    player.update()
    for i in mapa_game.block:
        if player.image.colliderect(i):
            player.x -= player.velocity_x 
            player.y -= player.velocity_y
    
    screen.fill(BLACK)
    mapa_game.draw_wall(screen)
    
    
    player.draw_pacman(screen,movement)
   
    pygame.display.update() # Or pygame.display.flip()
    
print("Exited the game loop. Game will quit...")
quit() # Not actually necessary since the script will exit anywa