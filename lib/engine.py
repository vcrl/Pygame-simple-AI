import os
import sys
import pygame
from .settings import WIDTH, HEIGHT, FPS
from .player import Player
from .sprites import Wall
from .sprites import all_sprites

class Engine():
    def __init__(self):
        self.state = {
            'running' : True,
            'playing' : False,
        }

        self.display = {
            'screen' : pygame.display.set_mode((WIDTH, HEIGHT)),
            'caption' : pygame.display.set_caption('Caption test'),
        }

        self.utils = {
            'clock' : pygame.time.Clock(),
        }

    def load_data(self):
        self.player = Player(self, 100, 100)
        self.walls = [
            Wall(self, 0, 500, WIDTH, HEIGHT),
            Wall(self, 0, 200, 300, HEIGHT),
            Wall(self, 500, 250, 300, HEIGHT)
        ]

    def update(self):
        all_sprites.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    pass

    def draw(self):
        self.display['screen'].fill((0, 0, 0))
        all_sprites.draw(self.display['screen'])
        pygame.display.flip()

    def run(self):
        self.load_data()
        while self.state['running']:
            self.dt = self.utils['clock'].tick(60) / 1000
            self.events()
            self.update()
            self.draw()

