import pygame

class Robot:
    
    def __init__(self, x: int, y: int, velocity: int, width: int):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.width = width
        self.bullet_state = "ready"

    def move_left(self):
        if self._left_boundry():
            self.x -= self.velocity
        return self.x
        

    def move_right(self):
        if self._right_boundry():
            self.x += self.velocity
        return self.x
    
    def _left_boundry(self) -> bool:
        return self.x > 0 
    
    def _right_boundry(self) -> bool:
        return self.x < self.width - 50
    
    def fire(self):
        self.bullet_state = "fire"

    def get_bullet_state(self)-> str:
        return self.bullet_state
    
    def reset_bullet_state(self):
        self.bullet_state = "ready"
    
    def get_x_position(self):
        return self.x
    
    def get_y_postion(self):
        return self.y




