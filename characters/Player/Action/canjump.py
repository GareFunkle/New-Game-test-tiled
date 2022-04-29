

class CanJump:

    def __init__(self, rect, jump=0, jump_high=0, jump_down=5, number_jump=0, to_jump=False):
        self.rect = rect
        self.jump = jump
        self.jump_high = jump_high
        self.jump_down = jump_down
        self.number_jump = number_jump
        self.to_jump = to_jump

    def move_jump(self):
        if self.to_jump:
            if self.jump_high >= 10:
                self.jump_down -= 1
                self.jump = self.jump_down
                self.sprite.status = 'jump'
                self.sprite.animation_speed = 0.3

            else:
                self.jump_high += 1
                self.jump = self.jump_high
                self.sprite.status = 'jump'
                self.sprite.animation_speed = 0.3

            if self.jump_down < 0:
                self.jump_high = 0
                self.jump_down = 5
                self.to_jump = False
                self.sprite.status = 'idle'
        self.rect.y = self.rect.y - (10 * (self.jump / 2))
