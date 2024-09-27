import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

# Player
player_surf = pygame.image.load("graphics/player.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (400, 600))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rect.x -= 10
        if keys[pygame.K_RIGHT]:
            player_rect.x += 10
        if keys[pygame.K_UP]:
            player_rect.y -= 10
        if keys[pygame.K_DOWN]:
            player_rect.y += 10
    

    screen.fill("black")        
    screen.blit(player_surf, player_rect)


    pygame.display.update()
    clock.tick(60)
