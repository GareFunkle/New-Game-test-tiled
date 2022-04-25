import pygame
from animatesprite.Support_Animation.support import import_folder


class Player_Sprite(pygame.sprite.Sprite):

    def __init__(self, x, y, speed_walk=3, speed_run=5,  jump=0, jump_high=0, jump_down=5, number_jump=0, to_jump=False):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.25
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect()

        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.sprite = pygame.image.load('assets/PLAYER/idle/idle.png')
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()

        # jump
        self.jump = jump
        self.jump_high = jump_high
        self.jump_down = jump_down
        self.number_jump = number_jump
        self.to_jump = to_jump

    def move_jump(self):
        if self.to_jump:
            if self.jump_high >= 50:
                self.jump_down -= 1.5
                self.jump = self.jump_down
                self.status = 'jump'
                self.animation_speed = 0.2

            else:
                self.jump_high += 1
                self.jump = self.jump_high
                self.status = 'jump'
                self.animation_speed = 0.3

            if self.jump_down < 0:
                self.jump_high = 0
                self.jump_down = 5
                self.to_jump = False
                self.status = 'idle'
        self.rect.y = self.rect.y - (10 * (self.jump / 2))

    def save_location(self):
        self.old_position = self.position.copy()

    def move_right(self):
        self.facing_right = True
        self.position[0] += self.speed_walk
        self.status = 'run'
        self.animation_speed = 0.35

    def move_left(self):
        self.facing_right = False
        self.position[0] -= self.speed_walk
        self.status = 'run'
        self.animation_speed = 0.35
    
    def run_right(self):
        self.position[0] += self.speed_run
        self.status = 'run'
        self.animation_speed = 0.55

    def run_left(self):
        self.position[0] -= self.speed_run
        self.status = 'run'
        self.animation_speed = 0.55


    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def get_image(self, x, y):
        image = pygame.Surface([138, 138])
        image.blit(self.sprite, (0, 0), (x, y, 138, 138))
        return image

    def import_character_assets(self):
        character_path = 'assets/PLAYER/'
        self.animations = {'idle': [], 'run': [],
                           'jump': [], 'attack': [], 'dead': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        # loop over frame index
        self.frame_index += self.animation_speed

        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]

        if self.facing_right:
            self.image = image
        else:
            self.facing_right = False
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image
        # set the rect
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(
                bottomright=self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def getstatus(self):
        self.status

    def get_rect(self):
        return self.rect
