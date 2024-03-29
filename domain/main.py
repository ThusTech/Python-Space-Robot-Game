from world.world import World
from robot.robot import Robot
from emeny.enemy import Enemy
from pygame import mixer
import pygame
import math




pygame.init()

clock = pygame.time.Clock()

running = True
width = 600
height = 600
x = (width/2) - 25
y = height - 50
velocity = 25
score = 0
player_lives = 5
font = pygame.font.Font('freesansbold.ttf',32)

world = World(width,height)
robot = Robot(x,y,velocity,width)
planet = Enemy(height,width)

# create the display window
window = world.get_world()
window.fill((200,200,200))
# world.set_background(window)
game_over_window = pygame.display.set_mode((width,height))

# Loading images
player = pygame.image.load("robot.png")
emeny = pygame.image.load("planet.png")
bullet = pygame.image.load("bullet.png")

# Background Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

bullet_x = robot.get_x_position()
bullet_y = robot.get_y_postion()

# frames per second
FPS = 27

def isCollision(bullet_x: int,butllet_y: int,enemy_x: int,enemy_y):
    distance = math.sqrt((math.pow(bullet_x-enemy_x,2))+(math.pow(butllet_y-enemy_y,2)))
    return distance < 30 and enemy_y < (height - 50) 

def display_info():
    score_board = font.render("Score  : "+ str(score),True,(0,0,0))
    velocity_board = font.render("Speed : "+ str(planet.get_velocity()),True,(0,0,0))
    lives_board = font.render("Lives  : "+ str(player_lives),True,(0,0,0))

    window.blit(velocity_board,(20,0))
    window.blit(score_board,(225,0))
    window.blit(lives_board,(425, 0))

def gameover_loop():
    game_over_window = pygame.display.set_mode((width,height))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

def main_loop():
    global running
    global x, y
    global bullet_y, bullet_x,bullet
    global player_lives
    global score

    while running:
        keys = pygame.key.get_pressed()
        clock.tick(FPS)
        window.blit(player,(x,y))

        # Enemy movement
        enemy_x_position = planet.get_verical_postion()
        enemy_y_postion = planet.get_horizontal_position()

        if enemy_y_postion > height:
            player_lives-=1
            planet.reset_postion()
        else:
            window.blit(emeny,(planet.get_verical_postion(),planet.get_horizontal_position()))
            enemy_y_postion += planet.get_velocity()
            planet.set_horizontal_position(enemy_y_postion)
        
        # Bullet movement
        if bullet_y <= 50:
            robot.reset_bullet_state()
            bullet_y = robot.get_y_postion()

        if robot.get_bullet_state() == "fire":
            bullet_y -= velocity
            window.blit(bullet, (bullet_x+18,bullet_y)) 
            
            

        # Show score
        display_info()
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
            if robot.get_bullet_state() == "ready":
                print("Bullet fired")
                mixer.Sound("laser.wav").play()        
                bullet_x = robot.get_x_position()
                robot.fire()

        if player_lives == 0:
            running = False

        # Collision
        if isCollision(bullet_x,bullet_y,enemy_x_position,enemy_y_postion):
            mixer.Sound("explosion.wav").play()
            robot.reset_bullet_state()
            bullet_y = robot.get_y_postion()

            planet.reset_postion()
            score+=1

            # if score is a multiple of 5 increment the speed
            if score % 5 == 0:
                planet.increase_velocity()
                print("Velocity increased")

        # Clear the screen
        window.fill((200,200,200))



def menu_loop():
    menu_window = pygame.display.set_mode((width,height))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


# gameover_loop()
# pygame.quit()
                
if __name__ == '__main__':            
    main_loop()



