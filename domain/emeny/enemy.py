import random

class Enemy:
    def __init__(self,height: int, width: int):
        self.height = height
        self.width = width
        self.velocity = 5
        self.x = random.randint(0,self.width-50)
        self.y = 0


    def move_down(self):
        pass

    def random_vertical_position(self):
        pass

    def get_verical_postion(self):
        return self.x
    
    def get_horizontal_position(self):
        return self.y
    
    def set_horizontal_position(self, y: int):
        self.y = y

