import pygame
class mapa():
    """
    Podria tener 16 bloques de ancho y 24 a lo largo en bloques de 30x30
    """
    def __init__(self):
        
        self.block = None
    def construir_mapa(self,walls):
        muros = []
        
        x = 0
        y = 0
        for row in walls:
            for wall in row:
                if wall == "X":
                    muros.append(pygame.Rect(x,y,30,30))
                x += 30
            x = 0
            y += 30
        self.block = muros
    def draw_wall(self,screen):
        for i in self.block:
            pygame.draw.rect(screen,(0,0,255),i)

        