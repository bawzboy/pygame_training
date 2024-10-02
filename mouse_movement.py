# Chat-Bro version with vector
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

    # def fly(self, target_pos):
        # rect_x = self.rect.center[0]
        # rect_y = self.rect.center[1]
        # target_x = target_pos[0]
        # target_y = target_pos[1]

        # dif_x = abs(target_x - rect_x)
        # dif_y = abs(target_y - rect_y)

        # # up left
        # if rect_x > target_x and rect_y > target_y:
        #     self.rect.x -= self.speed
        #     self.rect.y -= self.speed
        #     if dif_x > dif_y:
        #         self.image = self.fireball_left 
        #     elif dif_x < dif_y:
        #         self.image = self.fireball_up
        # # up right
        # elif rect_x < target_x and rect_y > target_y:
        #     self.rect.x += self.speed
        #     self.rect.y -= self.speed
        #     if dif_x > dif_y:
        #         self.image = self.fireball_right
        #     elif dif_x < dif_y:
        #         self.image = self.fireball_up     
        # # down left
        # elif rect_x > target_x and rect_y < target_y:
        #     self.rect.x -= self.speed
        #     self.rect.y += self.speed
        #     if dif_x > dif_y:
        #         self.image = self.fireball_left 
        #     elif dif_x < dif_y:
        #         self.image = self.fireball_down
        # # down right
        # elif rect_x < target_x and rect_y < target_y:
        #     self.rect.x += self.speed
        #     self.rect.y += self.speed
        #     if dif_x > dif_y:
        #         self.image = self.fireball_right 
        #     elif dif_x < dif_y:
        #         self.image = self.fireball_down

        # self.rect.x += self.direction.x * self.speed
        # self.rect.y += self.direction.y * self.speed

        # self.direction = pygame.Vector2(target_pos) - pygame.Vector2(player_pos)
        # if self.direction.length() != 0:
        #     self.direction.normalize_ip()

        # if abs(self.direction.x) > abs(self.direction.y):
        #     self.image = self.fireball_right if self.direction.x > 0 else self.fireball_left
        # else:
        #     self.image = self.fireball_down if self.direction.y > 0 else self.fireball_up

