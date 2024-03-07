class Robot:
    
    def __init__(self, pygame, width: int, height: int, velocity: int):
        self.robot = pygame.image.load("robot.png")
        self.pygame = pygame
        self.width = width
        self.height = height
        self.velocity = velocity

    def load_robot(self,world):
        # robot = pygame.image.load("robot.png")
        world.blit(self.robot,(self.width/2,500))

    def move_left(self):
        x = (self.width/2) - self.velocity
        self.width = x*2
        return x
        

    def move_right(self):
        x = (self.width/2) + self.velocity
        self.width = x*2
        return x


