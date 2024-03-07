from world.world import World
from robot.robot import Robot
import pygame

pygame.init()

clock = pygame.time.Clock()

# mainLoop
def main_loop():
    width = 800
    height = 600
    velocity = 5

    world = World(pygame,width,height)
    robot = Robot(pygame,width, height, velocity)

    window = world.set_world()
    world.set_background(window)
    robot.load_robot(window)

    running = True

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x = robot.move_left()
            print("Moving left: "+str(x))
        if keys[pygame.K_RIGHT]:
            x = robot.move_right()
            print("Moving right: "+str(x))
        
        
        

        clock.tick(27)

    pygame.quit()

def update_screen(x:int):

    pygame.display.update()

main_loop()



