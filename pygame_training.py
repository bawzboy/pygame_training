import pygame
from sys import exit


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_up = pygame.image.load("graphics/player_up.png").convert_alpha()
        self.player_down = pygame.image.load("graphics/player_down.png").convert_alpha()
        self.player_left = pygame.image.load("graphics/player_left.png").convert_alpha()
        self.player_right = pygame.image.load("graphics/player_right.png").convert_alpha()
    
        self.image = pygame.image.load("graphics/player.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (400, 600))
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= movement_speed
            self.image = self.player_left
        if keys[pygame.K_d]:
            self.rect.x += movement_speed
            self.image = self.player_right
        if keys[pygame.K_w]:
            self.rect.y -= movement_speed
            self.image = self.player_up
        if keys[pygame.K_s]:
            self.rect.y += movement_speed
            self.image = self.player_down
        
    def update(self):
        self.player_input()


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

# Player
player = pygame.sprite.GroupSingle()
player.add(Player())
movement_speed = 5


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("black")        
    
    player.draw(screen)
    player.update()

    pygame.display.update()
    clock.tick(60)
