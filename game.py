import pygame
import pytmx
import pyscroll
from animatesprite.animatesprite import Player_Sprite
from map import MapManager


class Game:

    def __init__(self):
        # creation de la fenetre du jeu
        self.screen = pygame.display.set_mode((1260, 700))
        pygame.display.set_caption("Pygame test")


        # generer un joueur
        self.player = Player_Sprite(0, 0)
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

        # if self.pressed.get(pygame.K_LSHIFT):
        #     self.player.run()
        if self.pressed.get(pygame.K_SPACE):
            self.player.status = "attack"

    def update(self):
        self.map_manager.update()

# boucle du jeu
    def run(self):
        clock = pygame.time.Clock()

        running = True

        while running:

            self.player.save_location()
            self.move()
            self.update()
            self.map_manager.draw()
            self.player.animate()
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
