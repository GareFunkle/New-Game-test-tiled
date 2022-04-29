import pygame
import pytmx

class Sol(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ground = list([pygame.Rect])
        self.rect = pygame.Rect(list.x, list.y, list.width, list.height)
