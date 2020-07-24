import pygame

class mapa():
    """
    Podria tener 16 bloques de ancho y 24 a lo largo en bloques de 30x30
    """
    def __init__(self):
        
        self.block = None
    def construir_mapa(self,walls,player):
        muros = []
        x = 0
        y = 0
        iter_row = 0
        iter_col = 0
        for row in walls:
            for wall in row:
                if wall == "X":
                    muros.append(pygame.Rect(x,y,30,30))
                elif wall == "P":
                    player.x = x + 15
                    player.y = y + 15
                    player.i = iter_row
                    player.j = iter_col
                x += 30
                iter_col += 1
            x = 0
            iter_col = 0
            y += 30
            iter_row += 1
        self.block = muros
    def draw_wall(self,screen):
        for i in self.block:
            pygame.draw.rect(screen,(0,0,255),i)

        
