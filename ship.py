import pygame
import os

WIDTH = 500
HEIGHT = 600

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.frame_names = [f"ship_frame{i}.png" for i in range(1, 3)]
        self.frames = [pygame.image.load(os.path.join("assets/ship_frames", frame_name)) for frame_name in self.frame_names]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]

        self.rect = self.image.get_rect()
        self.rect.center = (240, 550)
        self.frame_time = 120
        self.last_frame_time = pygame.time.get_ticks()
        self.direction = "stop"
        self.speed = 5

    def left(self):
        self.direction = "left"

    def right(self):
        self.direction = "right"
     
    def move(self):
        if(self.direction == "left"):
            self.rect.x -= self.speed 
            if(self.rect.x <= 0):
                self.rect.x = 0
        if(self.direction == "right"):
            self.rect.x += self.speed 
            if(self.rect.x >= 455):
                self.rect.x = 455

    def animate(self):
        self.move()
        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_time > self.frame_time:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.last_frame_time = current_time
