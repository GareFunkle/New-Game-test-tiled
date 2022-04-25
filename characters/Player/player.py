from characters.Player.Animatesprite.animatesprite import Player_Sprite
from characters.Player.Action.canwalk import CanWalk
from lib.units.unit import Unit
from characters.Player.Action.canjump import CanJump
from characters.Player.Action.canattack import CanAttack


class Player(Unit, CanWalk, CanJump, CanAttack):
    def __init__(self):
        Unit.__init__(self, Player_Sprite(0, 0),
                      current_health=100, max_health=100)

        CanWalk.__init__(self, self.rect, speed_walk=3, speed_run=5)
        CanJump.__init__(
            self,
            self.rect,
            jump=0,
            jump_high=0,
            jump_down=5,
            number_jump=0,
            to_jump=False,
        )
        CanAttack.__init__(self, attack_damage=3)
