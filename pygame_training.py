import pygame
from random import randint
from sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_up = pygame.image.load("graphics/wizard/wizard_up.png").convert_alpha()
        self.player_down = pygame.image.load("graphics/wizard/wizard_down.png").convert_alpha()
        self.player_left = pygame.image.load("graphics/wizard/wizard_left.png").convert_alpha()
        self.player_right = pygame.image.load("graphics/wizard/wizard_right.png").convert_alpha()
    
        self.image = pygame.image.load("graphics/wizard/wizard_down.png").convert_alpha()
        self.rect = self.image.get_rect(center = (400, 600))

        self.direction = pygame.math.Vector2()
        self.speed = 5

    def get_pos(self):
        return self.rect.centerx, self.rect.centery
    
    def get_orientation(self):
        if self.image == self.player_left:
            return "left"
        elif self.image == self.player_right:
            return "right"
        elif self.image == self.player_up:
            return "up"
        elif self.image == self.player_down:
            return "down"
    
    def player_input_keyboard(self):
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.image = self.player_left
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.image = self.player_right
        else:
            self.direction.x = 0
        
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.image = self.player_up
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.image = self.player_down
        else:
            self.direction.y = 0
                
        if self.direction.x != 0 and self.direction.y != 0:
            self.direction = self.direction.normalize()

        self.rect.move_ip(self.direction.x, self.direction.y)

    def move(self, speed):
        self.rect.center += self.direction * speed
    

    def update(self):
        self.player_input_keyboard()
        self.move(self.speed)
        self.get_pos()
        self.get_orientation()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/enemy/enemy.png").convert_alpha()
        self.rect = self.image.get_rect(center = (randint(0, screen_width),randint(0, screen_height)))

    def destroy(self, projectile_group):
        if pygame.sprite.spritecollide(self, projectile_group, True):
            self.kill()

    def update(self, projectile_group):
        self.destroy(projectile_group)


class Projectile(pygame.sprite.Sprite):
    def __init__(self, player_pos, player_orientation):
        super().__init__()
        self.fireball_up = pygame.image.load("graphics/projectile/fireball_up.png").convert_alpha()
        self.fireball_down = pygame.image.load("graphics/projectile/fireball_down.png").convert_alpha()
        self.fireball_left = pygame.image.load("graphics/projectile/fireball_left.png").convert_alpha()
        self.fireball_right = pygame.image.load("graphics/projectile/fireball_right.png").convert_alpha()
        
        self.image = pygame.image.load("graphics/projectile/fireball_default.png").convert_alpha()
        self.rect = self.image.get_rect(center = player_pos)
        self.orientation = player_orientation

        self.direction = pygame.math.Vector2()
        self.spawn_time = pygame.time.get_ticks()
        self.life_time = 2000
        self.speed = 10

    def destroy(self, enemy_group):
        if pygame.sprite.spritecollide(self, enemy_group, True):
            self.kill()

    def set_orientation(self):
        if self.orientation == "left":
            self.image = self.fireball_left
            self.direction.x = -1
        elif self.orientation == "right":
            self.image = self.fireball_right
            self.direction.x = 1
        else:
            self.direction.x = 0
        
        if self.orientation == "up":
            self.image = self.fireball_up
            self.direction.y = -1
        elif self.orientation == "down":
            self.image = self.fireball_down
            self.direction.y = 1
        else:
            self.direction.y = 0

        if self.direction.x != 0 and self.direction.y != 0:
            self.direction = self.direction.normalize()

        self.rect.move_ip(self.direction.x, self.direction.y)

    def move(self, speed):
        self.rect.center += self.direction * speed

    def update(self, enemy_group):
        self.destroy(enemy_group)
        self.set_orientation()
        self.move(self.speed)
        # self.fly(self.direction)
        if pygame.time.get_ticks() - self.spawn_time > self.life_time:
            self.kill()


screen_width = 1200
screen_height = 800
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

# Player
player = pygame.sprite.GroupSingle()
player.add(Player())

# Enemy
enemy_group = pygame.sprite.Group()
enemy_group.add(Enemy())

projectile_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                projectile = Projectile(player.sprite.get_pos(), player.sprite.get_orientation())
                projectile_group.add(projectile)

    screen.fill("black")        
    
    player.draw(screen)
    player.update()

    enemy_group.draw(screen)
    enemy_group.update(projectile_group)

    projectile_group.draw(screen)
    projectile_group.update(enemy_group)

    pygame.display.update()
    clock.tick(60)
