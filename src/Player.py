import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = -999
        self.y = -999
        self.radius = 10
        
        self.velocity_x = 0
        self.velocity_y = 0
        self.image = pygame.Rect(self.x - 10,self.y - 10,20,20) 
       
    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.image = pygame.Rect(self.x - 10,self.y - 10,20,20)
        
    def draw_pacman(self,screen,direction = None):
        
        
        if direction == None:
            pygame.draw.circle(screen,(255,255,0),(self.x,self.y),self.radius)
        elif direction == "up":
            pygame.draw.circle(screen,(255,255,0),(self.x,self.y),self.radius)
            pygame.draw.polygon(screen,(0,0,0),[[self.x,self.y],[self.x - 5,self.y - 10],[self.x + 5,self.y - 10]])
        elif direction == "down":
            pygame.draw.circle(screen,(255,255,0),(self.x,self.y),self.radius)
            pygame.draw.polygon(screen,(0,0,0),[[self.x,self.y],[self.x - 5,self.y + 10],[self.x + 5,self.y + 10]])

        elif direction == "left":
            pygame.draw.circle(screen,(255,255,0),(self.x,self.y),self.radius)
            pygame.draw.polygon(screen,(0,0,0),[[self.x,self.y],[self.x - 10,self.y + 5],[self.x - 10,self.y - 5]])
        elif direction == "rigth":
            pygame.draw.circle(screen,(255,255,0),(self.x,self.y),self.radius)
            pygame.draw.polygon(screen,(0,0,0),[[self.x,self.y],[self.x + 10,self.y + 5],[self.x + 10,self.y - 5]])
        pygame.display.update()
        pygame.time.delay(8)
        pygame.draw.circle(screen,(255,255,0),(self.x,self.y),self.radius)

        