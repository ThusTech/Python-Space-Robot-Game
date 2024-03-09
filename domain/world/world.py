import pygame
class World:
    
    def __init__(self,width:int, height:int):
        self.width = width
        self.height = height
        self.screen_size = [width,height]

    def get_world(self):
       return pygame.display.set_mode(self.screen_size)
    
    def set_background(self, window):
        background = pygame.image.load("space.jpg")
        window.blit(background,(0,0))
    


