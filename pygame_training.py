import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((400, 800))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    pygame.display.update()
    clock.tick(60)
