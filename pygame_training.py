import pygame
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
    
    def player_input_keyboard(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= movement_speed
            self.image = self.player_left
        elif keys[pygame.K_d]:
            self.rect.x += movement_speed
            self.image = self.player_right
        elif keys[pygame.K_w]:
            self.rect.y -= movement_speed
            self.image = self.player_up
        elif keys[pygame.K_s]:
            self.rect.y += movement_speed
            self.image = self.player_down

    def player_mouse_input(self):
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            mouse_pos = pygame.mouse.get_pos()

            rect_x = self.rect.center[0]
            rect_y = self.rect.center[1]
            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]

            dif_x = abs(mouse_x - rect_x)
            dif_y = abs(mouse_y - rect_y)

            # up left
            if rect_x > mouse_x and rect_y > mouse_y:
                self.rect.x -= movement_speed
                self.rect.y -= movement_speed
                if dif_x > dif_y:
                    self.image = self.player_left 
                elif dif_x < dif_y:
                    self.image = self.player_up

            # up right
            elif rect_x < mouse_x and rect_y > mouse_y:
                self.rect.x += movement_speed
                self.rect.y -= movement_speed
                if dif_x > dif_y:
                    self.image = self.player_right
                elif dif_x < dif_y:
                    self.image = self.player_up     

            # down left
            elif rect_x > mouse_x and rect_y < mouse_y:
                self.rect.x -= movement_speed
                self.rect.y += movement_speed
                if dif_x > dif_y:
                    self.image = self.player_left 
                elif dif_x < dif_y:
                    self.image = self.player_down

            # down right
            elif rect_x < mouse_x and rect_y < mouse_y:
                self.rect.x += movement_speed
                self.rect.y += movement_speed
                if dif_x > dif_y:
                    self.image = self.player_right 
                elif dif_x < dif_y:
                    self.image = self.player_down


    def update(self):
        self.player_input_keyboard()
        self.player_mouse_input()



pygame.init()
screen = pygame.display.set_mode((1200, 800))
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
