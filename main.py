import pygame
import sys
from random import randint

from ship import Ship
from laser import Laser
from enemy import Enemy

pygame.init()
pygame.mixer.init()

WIDTH = 500
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

background_image = pygame.image.load("assets/space.jpg")
bg_y1 = 0
bg_y2 = -HEIGHT
background_speed = 1 

if(randint(1,2) == 1):
    pygame.mixer.music.load('assets/sounds/Corneria.ogg')
    pygame.mixer.music.set_volume(0.5)
    
else:
    pygame.mixer.music.load('assets/sounds/Wolf.ogg')
    pygame.mixer.music.set_volume(0.5)

pygame.mixer.music.play(-1)

laser_sound = pygame.mixer.Sound('assets/sounds/Laser.wav')
laser_sound.set_volume(0.8)

point_sound = pygame.mixer.Sound('assets/sounds/Point.wav')
point_sound.set_volume(0.4)


ship = Ship()
laser = Laser()

enemies = []

score_font = pygame.font.SysFont(None, 36)
score = 0

enemy_count = 5
static_enemy_count = enemy_count
def create_enemies(enemy_count):
    for i in range(enemy_count):
        new_enemy = Enemy()
        enemies.append(new_enemy)

create_enemies(enemy_count)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship.left()
            if event.key == pygame.K_RIGHT:
                ship.right()
            if event.key == pygame.K_SPACE:
                if(laser.laser_state == "ready"):
                    laser.rect.center = ship.rect.center
                    laser.fire()
                    laser_sound.play()

    bg_y1 += background_speed
    bg_y2 += background_speed

    if bg_y1 >= HEIGHT:
        bg_y1 = -HEIGHT

    if bg_y2 >= HEIGHT:
        bg_y2 = -HEIGHT

    screen.blit(background_image, (0, bg_y1))
    screen.blit(background_image, (0, bg_y2))

    screen.blit(ship.image, ship.rect)
    ship.animate()

    score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))  
    screen.blit(score_text, (10, 10))  

    if(laser.laser_state == "fire"):
        laser.animate()
        screen.blit(laser.image, laser.rect)

    for enemy in enemies:
        enemy.animate()
        enemy.laser.animate()
        if(enemy.rect.y < 450 and enemy.hit == False):
            enemy.fire()
        if(enemy.hit == False):
            screen.blit(enemy.image, enemy.rect)
        if(enemy.laser.laser_state == "fire"):
            screen.blit(enemy.laser.image, enemy.laser.rect)
        if(pygame.rect.Rect.colliderect(laser.rect, enemy.rect) and enemy.hit == False) and laser.laser_state == "fire":
            laser.laser_state = "ready"
            enemy.hit = True
            enemy_count -= 1
            score += 1
            laser.speed += .25
            ship.speed += .25
            point_sound.play()
        if(enemy.rect.y >= HEIGHT and enemy.hit == False or (pygame.rect.Rect.colliderect(ship.rect, enemy.laser.rect) and enemy.hit == False)):
            for enemy in enemies:
                enemy.hit = False
                enemy.rect.center = (randint(30, WIDTH - 50), randint(-150, -20))
                enemy.laser.rect.center = enemy.rect.center
                enemy.laser.laser_state = "ready"
            enemy_count = 5
            static_enemy_count = enemy_count
            enemies = []
            create_enemies(5)
            score = 0
            laser.speed = 15
            ship.speed = 5
            if(randint(1,2) == 1):
                pygame.mixer.music.load('assets/sounds/Corneria.ogg')
                pygame.mixer.music.set_volume(0.5)
                
            else:
                pygame.mixer.music.load('assets/sounds/Wolf.ogg')
                pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
        
        
    
    if(enemy_count == 0):
        for enemy in enemies:
            enemy.hit = False
            enemy.rect.center = (randint(30, WIDTH - 50), randint(-200, -20))
            enemy.laser.rect.center = enemy.rect.center
        enemy_count = static_enemy_count + 1
        static_enemy_count = enemy_count
        create_enemies(1)
        
        
    clock.tick(60)
    pygame.display.flip()
