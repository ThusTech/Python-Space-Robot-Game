import random

class Enemy:
    def __init__(self,height: int, width: int):
        self.height = height
        self.width = width
        self.velocity = 1
        self.x = self.random_vertical_position()
        self.y = 50


    def reset_postion(self):
        self.y = 50
        self.x = self.random_vertical_position()

    def random_vertical_position(self):
        return random.randint(0,self.width-50)
    
    def increase_velocity(self):
        self.velocity += 0.5

    def get_verical_postion(self) -> int:
        return self.x
    
    def get_horizontal_position(self) -> int:
        return self.y
    
    def get_velocity(self) -> int:
        return self.velocity
    
    def set_horizontal_position(self, y: int):
        self.y = y

