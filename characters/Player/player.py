import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load("assets/PLAYER/idle/idle.png")
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        # self.images = {
        #     "up": self.get_image(0, 96),
        #     "down": self.get_image(0, 0),
        #     "right": self.get_image(0, 64),
        #     "left": self.get_image(0, 32)
        # }
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.speed_walk = 3
        self.jump = 0
        self.jump_high = 0
        self.jump_down = 5
        self.number_jump = 0
        self.to_jump = False

    # def get(self):
    #     self.image = self.images["down"]
    #     self.image.set_colorkey([0, 0, 0])
    #     return self.image

    def save_location(self):
        self.old_position = self.position.copy()

    def move_right(self):
        self.position[0] += self.speed_walk

    def move_left(self):
        self.position[0] -= self.speed_walk

    def move_jump(self):
        if self.to_jump:
            if self.jump_high >= 7:
                self.jump_down -= 1
                self.jump = self.jump_down

            else:
                self.jump_high += 1
                self.jump = self.jump_high

            if self.jump_down < 0:
                self.jump_high = 0
                self.jump_down = 5
                self.to_jump = False
        self.position[1] = self.position[1] - (10 * (self.jump / 2))

    # def move_player(self, type):
    #     self.image = self.images[type]
    #     self.image.set_colorkey([0, 0, 0])
    #     if type == "up":
    #         self.position[1] -= self.speed
    #     elif type == "down":
    #         self.position[1] += self.speed
    #     elif type == "right":
    #         self.position[0] += self.speed
    #     elif type == "left":
    #         self.position[0] -= self.speed

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position.copy()
        self.feet.midbottom = self.rect.midbottom
        self.update()

    def get_image(self, x, y):
        image = pygame.Surface([118, 138])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 128, 138))
        return image
