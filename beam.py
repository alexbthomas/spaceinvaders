import pygame
import os

WIDTH = 500
HEIGHT = 600

class Beam(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.frame_names = [f"beam_frame{i}.gif" for i in range(1, 12)]
        self.frames = [pygame.image.load(os.path.join("assets/beam_frames", frame_name)) for frame_name in self.frame_names]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]

        self.rect = self.image.get_rect()
        self.rect.center = (240, 270)
        self.frame_time = 40
        self.last_frame_time = pygame.time.get_ticks()
        
        self.active = True

    def animate(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_time > self.frame_time:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.image = pygame.transform.rotate(self.image, 90)
        
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center

            self.last_frame_time = current_time
    
