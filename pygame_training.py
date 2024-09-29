import pygame
import random
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

        self.movement_speed = 5

    def get_pos(self):
        return self.rect.centerx, self.rect.centery
    
    def player_input_keyboard(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.movement_speed
            self.image = self.player_left
        elif keys[pygame.K_d]:
            self.rect.x += self.movement_speed
            self.image = self.player_right
        elif keys[pygame.K_w]:
            self.rect.y -= self.movement_speed
            self.image = self.player_up
        elif keys[pygame.K_s]:
            self.rect.y += self.movement_speed
            self.image = self.player_down


    # Chat-Bro version with vector math
    # def player_mouse_input(self): 
    #         mouse = pygame.mouse.get_pressed()
    #         if mouse[0]:
    #             mouse_pos = pygame.mouse.get_pos()

    #             # Calculate the angle and move the player toward the mouse smoothly
    #             player_pos = pygame.Vector2(self.rect.center)
    #             direction = pygame.Vector2(mouse_pos) - player_pos

    #             if direction.length() != 0:  # Avoid division by zero
    #                 direction.normalize_ip()

    #                 # Apply movement based on the direction
    #                 self.rect.x += direction.x * self.movement_speed
    #                 self.rect.y += direction.y * self.movement_speed

    #                 # Update player sprite image based on movement direction
    #                 if abs(direction.x) > abs(direction.y):
    #                     self.image = self.player_right if direction.x > 0 else self.player_left
    #                 else:
    #                     self.image = self.player_down if direction.y > 0 else self.player_up

    # def player_mouse_input(self):
    #     mouse = pygame.mouse.get_pressed()
    #     if mouse[0]:
    #         mouse_pos = pygame.mouse.get_pos()

    #         rect_x = self.rect.center[0]
    #         rect_y = self.rect.center[1]
    #         mouse_x = mouse_pos[0]
    #         mouse_y = mouse_pos[1]

    #         dif_x = abs(mouse_x - rect_x)
    #         dif_y = abs(mouse_y - rect_y)

    #         # up left
    #         if rect_x > mouse_x and rect_y > mouse_y:
    #             self.rect.x -= self.movement_speed
    #             self.rect.y -= self.movement_speed
    #             if dif_x > dif_y:
    #                 self.image = self.player_left 
    #             elif dif_x < dif_y:
    #                 self.image = self.player_up
    #         # up right
    #         elif rect_x < mouse_x and rect_y > mouse_y:
    #             self.rect.x += self.movement_speed
    #             self.rect.y -= self.movement_speed
    #             if dif_x > dif_y:
    #                 self.image = self.player_right
    #             elif dif_x < dif_y:
    #                 self.image = self.player_up     
    #         # down left
    #         elif rect_x > mouse_x and rect_y < mouse_y:
    #             self.rect.x -= self.movement_speed
    #             self.rect.y += self.movement_speed
    #             if dif_x > dif_y:
    #                 self.image = self.player_left 
    #             elif dif_x < dif_y:
    #                 self.image = self.player_down
    #         # down right
    #         elif rect_x < mouse_x and rect_y < mouse_y:
    #             self.rect.x += self.movement_speed
    #             self.rect.y += self.movement_speed
    #             if dif_x > dif_y:
    #                 self.image = self.player_right 
    #             elif dif_x < dif_y:
    #                 self.image = self.player_down

    def update(self):
        self.player_input_keyboard()
        # self.player_mouse_input()
        self.get_pos()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/enemy/enemy.png").convert_alpha()
        self.rect = self.image.get_rect(center = (200,200))

    def destroy(self, projectile_group):
        if pygame.sprite.spritecollide(self, projectile_group, True):
            self.kill()

    def update(self, projectile_group):
        self.destroy(projectile_group)


class Projectile(pygame.sprite.Sprite):
    def __init__(self, player_pos, target_pos):
        super().__init__()
        self.fireball_up = pygame.image.load("graphics/projectile/fireball_up.png").convert_alpha()
        self.fireball_down = pygame.image.load("graphics/projectile/fireball_down.png").convert_alpha()
        self.fireball_left = pygame.image.load("graphics/projectile/fireball_left.png").convert_alpha()
        self.fireball_right = pygame.image.load("graphics/projectile/fireball_right.png").convert_alpha()
        
        self.image = pygame.image.load("graphics/projectile/fireball_up.png").convert_alpha()
        self.rect = self.image.get_rect(center = player_pos)

        self.direction = target_pos
        self.speed = 10

    def fly(self, target_pos):
        rect_x = self.rect.center[0]
        rect_y = self.rect.center[1]
        target_x = target_pos[0]
        target_y = target_pos[1]

        dif_x = abs(target_x - rect_x)
        dif_y = abs(target_y - rect_y)

        # up left
        if rect_x > target_x and rect_y > target_y:
            self.rect.x -= self.speed
            self.rect.y -= self.speed
            if dif_x > dif_y:
                self.image = self.fireball_left 
            elif dif_x < dif_y:
                self.image = self.fireball_up
        # up right
        elif rect_x < target_x and rect_y > target_y:
            self.rect.x += self.speed
            self.rect.y -= self.speed
            if dif_x > dif_y:
                self.image = self.fireball_right
            elif dif_x < dif_y:
                self.image = self.fireball_up     
        # down left
        elif rect_x > target_x and rect_y < target_y:
            self.rect.x -= self.speed
            self.rect.y += self.speed
            if dif_x > dif_y:
                self.image = self.fireball_left 
            elif dif_x < dif_y:
                self.image = self.fireball_down
        # down right
        elif rect_x < target_x and rect_y < target_y:
            self.rect.x += self.speed
            self.rect.y += self.speed
            if dif_x > dif_y:
                self.image = self.fireball_right 
            elif dif_x < dif_y:
                self.image = self.fireball_down


    def destroy(self, enemy_group):
        if pygame.sprite.spritecollide(self, enemy_group, True):
            self.kill()

    def update(self, enemy_group):
        self.destroy(enemy_group)
        self.fly(self.direction)



pygame.init()
screen = pygame.display.set_mode((1200, 800))
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

    mouse = pygame.mouse.get_pressed()
    if mouse[0]:
        mouse_pos = pygame.mouse.get_pos()
        projectile = Projectile(player.sprite.get_pos(), mouse_pos)
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
