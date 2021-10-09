import math
import pygame

class PlayerShip:

    def __init__(self, screen):
        self.screen = screen
        self.x = 360
        self.y = 460
        self.image = pygame.image.load("./images/player.png")

    def PlayerMovementAndRotation(self):

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a] and self.x > 10:
            self.x -= 1              
        if keys[pygame.K_d] and self.x < 765:
            self.x += 1
        if keys[pygame.K_w] and self.y > 15:
            self.y -= 1
        if keys[pygame.K_s] and self.y < 570:
            self.y += 1

        self.RotateToMouse(window=self.screen)
               
    def RotateToMouse(self, window):
        player_rect = self.image.get_rect(center = (self.x, self.y))

        mx, my = pygame.mouse.get_pos()
        dx, dy = mx - player_rect.centerx, my - player_rect.centery
        angle = math.degrees(math.atan2(-dy, dx)) - 90

        rot_image = pygame.transform.rotate(self.image, angle)
        rot_image_rect = rot_image.get_rect(center = player_rect.center)
        window.blit(rot_image, rot_image_rect.topleft)
    
    def GetPosition(self):
        return (self.x, self.y)

    
