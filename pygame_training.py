import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

# Player
player_surf = pygame.image.load("graphics/player.png").convert_alpha()
player_surf_up = pygame.image.load("graphics/player_up.png").convert_alpha()
player_surf_down = pygame.image.load("graphics/player_down.png").convert_alpha()
player_surf_left = pygame.image.load("graphics/player_left.png").convert_alpha()
player_surf_right = pygame.image.load("graphics/player_right.png").convert_alpha()
player_rect = player_surf_up.get_rect(midbottom = (400, 600))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_rect.x -= 10
            player_surf = player_surf_left
        if keys[pygame.K_d]:
            player_rect.x += 10
            player_surf = player_surf_right
        if keys[pygame.K_w]:
            player_rect.y -= 10
            player_surf = player_surf_up
        if keys[pygame.K_s]:
            player_rect.y += 10
            player_surf = player_surf_down
    

    screen.fill("black")        
    screen.blit(player_surf, player_rect)


    pygame.display.update()
    clock.tick(60)
