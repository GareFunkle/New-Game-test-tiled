import pygame
import pytmx
import pyscroll
from animatesprite.animatesprite import Player_Sprite


class Game:

    def __init__(self):
        # creation de la fenetre du jeu
        self.screen = pygame.display.set_mode((1260, 700))
        pygame.display.set_caption("Pygame test")

        # charger la carte
        tmx_data = pytmx.util_pygame.load_pygame('tile/carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(
            map_data, self.screen.get_size())

        # generer un joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player_Sprite(player_position.x, player_position.y)
        self.sol = tmx_data.get_object_by_name("sol")
        # definir une liste qui va stocker mec collision
        # mapPlay = load_pygame(get_map(stats['map']))
        # self.ground = []
        
        # for obj in tmx_data.objects:
        #     if obj.type == "collision":
        #         self.ground.append(pygame.Rect(
        #             obj.x, obj.y, obj.width, obj.height))
        # self.walls = list()
        # for object in mapPlay.objects:
        #     self.walls.append(pygame.Rect(
        #     object.x, object.y,
        #     object.width, object.height))

        self.gravity = (0, 10)
        self.resistance = (0, 0)
        self.collision_sol = False

        # dessiner ke groupe de calques
        self.group = pyscroll.PyscrollGroup(
            map_layer=map_layer, default_layer=3)
        self.group.add(self.player)

        self.pressed = {}
        
    # def init_screen(width, height, mode):
    #     screen = pygame.display.set_mode((int(width), int(height)), mode)
    #     return screen

    def move(self):
        if self.pressed.get(pygame.K_RIGHT):
            self.player.move_right()
        if self.pressed.get(pygame.K_LEFT):
            self.player.move_left()

    def gravity_game(self):
        self.player.rect.y += self.gravity[1] + self.resistance[1]
        

    def update(self):
        self.group.update()

        # for sprite in self.group.sprites():
        #     if sprite.feet.collidelist(self.ground) > -1:
        #         sprite.move_back()
# boucle du jeu
    def run(self):
        clock = pygame.time.Clock()

        running = True

        while running:

            self.player.save_location()
            self.move()
            self.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            self.player.animate()

            self.gravity_game()

            if self.sol:
                self.resistance = (0, -10)
                self.collision_sol = True

            else:
                self.resistance = (0, 0)

            # if self.player.to_jump and self.collision_sol:
            #     self.player.move_jump()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    self.pressed[event.key] = True

                elif event.type == pygame.KEYUP:
                    self.player.status = 'idle'
                    self.pressed[event.key] = False

            clock.tick(60)
