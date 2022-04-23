import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, speed_walk=3 , speed_run=5):
        super().__init__()
        self.sprite = pygame.image.load('assets/PLAYER/idle/idle.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.facing_right = True



    def move_right(self):
        self.position[0] += self.speed_walk
        self.facing_right()

    def move_left(self):

        self.position[0] -= self.speed_walk

    

    def update(self):
        self.rect.topleft = self.position

    def get_image(self, x, y):
        image = pygame.Surface([138, 138])
        image.blit(self.sprite, (0, 0), (x, y, 138, 138))
        return image
