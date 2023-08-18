import pygame
import os
from random import randint
from enemy_laser import Enemy_Laser

WIDTH = 500
HEIGHT = 600

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.frame_names = [f"enemy_frame{i}.gif" for i in range(1, 3)]
        self.frames = [pygame.image.load(os.path.join("assets/enemy_frames", frame_name)) for frame_name in self.frame_names]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]

        self.rect = self.image.get_rect()
        self.rect.center = (randint(30, WIDTH - 50), randint(-200, -20))
        self.frame_time = 120
        self.last_frame_time = pygame.time.get_ticks()
        self.direction = "stop"
        self.speed = 2

        self.hit = False

        self.mover = randint(1, 2)

        self.laser = Enemy_Laser()
        self.laser.rect.center = self.rect.center

    def move(self):
        if(self.mover == 1):
            self.rect.x += self.speed
            if(self.rect.x <= 0 or self.rect.x >= WIDTH - 50):
                self.speed *= -1
            self.rect.y += 1
        else:
            self.rect.y += 2
        

    def animate(self):
        self.move()
        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_time > self.frame_time:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.image = pygame.transform.rotate(self.image, -180)

            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center

            self.last_frame_time = current_time

    def fire(self):
        if(self.laser.laser_state == "ready"):
            if(randint(1,150) == 1):
                self.laser.laser_state = "fire"
                self.laser.rect.center = self.rect.center

        

    
