import pygame
from characters.Player.player import Player
from Data.Map.map import MapManager
import Data.data as data
import Data.settings as settings


class Game:

    def __init__(self):
        # creation de la fenetre du jeu
        self.screen = pygame.display.set_mode((settings.DISPLAY_X, settings.DISPLAY_Y))
        pygame.display.set_caption(data.GAME_NAME)

        # generer un joueur
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)

        self.pressed = {}

    # def init_screen(width, height, mode):
    #     screen = pygame.display.set_mode((int(width), int(height)), mode)
    #     return screen

    def move(self):
        if self.pressed.get(pygame.K_RIGHT):
            self.player.move_right()
        if self.pressed.get(pygame.K_LEFT):
            self.player.move_left()
        if self.pressed.get(pygame.K_UP):
            self.player.to_jump = True
            self.player.number_jump += 1

        if self.pressed.get(pygame.K_SPACE):
            self.player.sprite.status = "attack"

    def update(self):
        self.map_manager.update()

# boucle du jeu
    def run(self):
        clock = pygame.time.Clock()
        # self.map_manager.get_group().update()
        
        running = True

        while running:

            self.player.sprite.save_location()
            self.move()
            self.update()
            self.map_manager.draw()

            # print(self.map_manager.get_ground())
            
            self.player.sprite.animate()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    self.pressed[event.key] = True

                elif event.type == pygame.KEYUP:
                    self.player.sprite.status = 'idle'
                    self.pressed[event.key] = False

            clock.tick(settings.FPS)
