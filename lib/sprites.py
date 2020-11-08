import pygame

all_sprites = pygame.sprite.Group()
player = pygame.sprite.Group()
walls = pygame.sprite.Group()

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.game = game
        self.groups = all_sprites, walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((w, h))
        self.image.fill((150, 200, 95))
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.rect.x, self.rect.y = self.x, self.y