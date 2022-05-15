import pygame
import pytmx


class Sol(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(2160, 359, 2384, 14)
        self.rect2 = pygame.Rect(5, 359, 655, 17)
        self.rect3 = pygame.Rect(783, 362, 739, 9)

    # <rect(2160, 359, 2384, 14)>, <rect(5, 359, 655, 17)>, <rect(783, 362, 739, 9)>
