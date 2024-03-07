class World:
    
    def __init__(self,pygame, width:int, height:int):
        self.pygame = pygame
        self.width = width
        self.height = height
        self.screen_size = [width,height]

    def set_world(self):
       return self.pygame.display.set_mode(self.screen_size)
    
    def set_background(self, world):
        background = self.pygame.image.load("space.jpg")
        world.blit(background,(0,0))

    def get_dimension(self)->tuple:
        return self.width,self.height
    


