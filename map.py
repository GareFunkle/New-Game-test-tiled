from dataclasses import dataclass
import pygame
import pytmx
import pyscroll


@dataclass
class Map:
    name: str
    ground:list([pygame.Rect])
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap


class MapManager:

    def __init__(self, screen, player):
        self.maps = dict()
        self.screen = screen
        self.current_map = "carte"
        self.player = player
        self.gravity = (0, 10)
        self.resistance = (0, 0)
        self.collision_sol = False

        self.register_map("carte")

        self.teleport_player("player")

    def check_collision(self):
        for sprite in self.get_group().sprites():
            if sprite.feet.collidelist(self.get_ground()) > +0.1:
                sprite.move_back()
                self.player.rect
                self.resistance = (0, -10)
                self.collision_sol = True

        if self.player.to_jump and self.collision_sol:
            self.player.move_jump()

    def gravity_game(self):
        self.player.rect.y += self.gravity[1] + self.resistance[1]

    def teleport_player(self, name):
        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()

    def register_map(self, name):
        # charger la carte
        tmx_data = pytmx.util_pygame.load_pygame(f"tile/{name}.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(
            map_data, self.screen.get_size())

        # definir une liste qui va stocker mec collision
        ground = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                ground.append(pygame.Rect(
                    obj.x, obj.y, obj.width, obj.height))

                # dessiner ke groupe de calques
        group = pyscroll.PyscrollGroup(
            map_layer=map_layer, default_layer=3)
        group.add(self.player)

        # creer un objet map
        self.maps[name] = Map(name, ground, group, tmx_data)

    def get_map(self):
        return self.maps[self.current_map]

    def get_group(self):
        return self.get_map().group

    def get_ground(self):
        return self.get_map().ground



    def get_object(self, name):
        return self.get_map().tmx_data.get_object_by_name(name)

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def update(self):
        self.get_group().update()
        self.check_collision()
        self.gravity_game()
