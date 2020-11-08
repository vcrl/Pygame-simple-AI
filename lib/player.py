import pygame
from .settings import PLAYER_FRICTION, PLAYER_ACC, GRAV, PLAYER_JUMP
from .sprites import all_sprites, player, walls
from .settings import WIDTH, HEIGHT
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = all_sprites, player
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((32, 64))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.acc = vec(0, 0)
        self.vel = vec(0, 0)
        self.pos = vec(self.x, self.y)

        self.state = {
            'on_ground': False,
            'on_wall': False,
        }
 
    def collision_y(self):
        collision = pygame.sprite.spritecollide(self, walls, False)
        if collision:
            if self.vel.y > 0: #Si le joueur tombe, sa vélocité = positive
                self.pos.y = collision[0].rect.top - self.rect.height * 0.5
                self.vel.y = 0
                self.state['on_ground'] = True
            else:
                self.state['on_ground'] = False
            self.rect.centery = self.pos.y

    def collision_x(self):
        collision = pygame.sprite.spritecollide(self, walls, False)
        if collision:
            if self.vel.x < 0:
                self.pos.x = collision[0].rect.right + self.rect.width * 0.5
                self.state['on_wall'] = True
            if self.vel.x > 0:
                self.pos.x = collision[0].rect.left - self.rect.width * 0.5
                self.state['on_wall'] = True
            self.rect.centerx = self.pos.x
        else:
            self.state['on_wall'] = False

    def jump(self):
        key = pygame.key.get_pressed()
        collision = pygame.sprite.spritecollide(self, walls, False)

        if self.state['on_ground'] or self.state['on_wall']:
            if key[pygame.K_SPACE]:
                self.vel.y = -PLAYER_JUMP * self.game.dt
        self.state['on_ground'] = False
        

    def movements(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.acc.x = -PLAYER_ACC * self.game.dt
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.acc.x = PLAYER_ACC * self.game.dt

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

    def update(self):
        if not self.state['on_ground']:
            self.acc = vec(0, GRAV *  self.game.dt)
        else:
            self.acc = vec(0, 0)
        #///////////////#
        self.movements()
        self.jump()
        self.rect.centerx = self.pos.x
        self.collision_x()
        self.rect.centery = self.pos.y
        self.collision_y()
        self.debug(self.state['on_wall'])

    def debug(self, elmt):
        print(elmt)