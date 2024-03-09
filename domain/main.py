from world.world import World
from robot.robot import Robot
from emeny.enemy import Enemy
import pygame
import math

pygame.init()

clock = pygame.time.Clock()

width = 600
height = 600
x = (width/2) - 25
y = height - 50
velocity = 25
score = 0

world = World(width,height)
robot = Robot(x,y,velocity,width)
planet = Enemy(height,width)

# create the display window
window = world.set_world()
window.fill((200,200,200))


# world.set_background(window)

player = pygame.image.load("robot.png")
emeny = pygame.image.load("planet.png")
bullet = pygame.image.load("bullet.png")

bullet_x = robot.get_x_position()
bullet_y = robot.get_y_postion()


# frames per second
FPS = 27

def isCollision(bullet_x: int,butllet_y: int,enemy_x: int,enemy_y):
    distance = math.sqrt((math.pow(bullet_x-enemy_x,2))+(math.pow(butllet_y-enemy_y,2)))
    return distance < 30

running = True
while running:
    keys = pygame.key.get_pressed()
    clock.tick(FPS)
    window.blit(player,(x,y))
    

    # Enemy movement
    enemy_x_position = planet.get_verical_postion()
    enemy_y_postion = planet.get_horizontal_position()

    if enemy_y_postion == height:
        print("Player killed")
    else:
        window.blit(emeny,(planet.get_verical_postion(),planet.get_horizontal_position()))
        enemy_y_postion += 1
        planet.set_horizontal_position(enemy_y_postion)

    
    # Bullet movement
    if bullet_y <= 0:
        robot.reset_bullet_state()
        bullet_y = robot.get_y_postion()

    if robot.get_bullet_state() is "fire":
        bullet_y -= velocity
        window.blit(bullet, (bullet_x+18,bullet_y)) 
    else:
        bullet_x = robot.get_x_position()
        

    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    if keys[pygame.K_LEFT]:
        x = robot.move_left()
        print("Moving left: "+str(x))
    if keys[pygame.K_RIGHT]:
        x = robot.move_right()
        print("Moving right: "+str(x))
    
    if keys[pygame.K_SPACE]:
        print("Bullet fired")
        robot.fire()

    # Collision
    if isCollision(bullet_x,bullet_y,enemy_x_position,enemy_y_postion):
        robot.reset_bullet_state()
        bullet_y = robot.get_y_postion()
        score+=1
        print(str(score))

    # Clear the screen
    window.fill((200,200,200))

pygame.quit() 




