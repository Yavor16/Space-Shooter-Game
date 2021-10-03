import math
import pygame
import random

class EnemyShip:

    def __init__(self, screen):
        self.screen = screen
        self.x = random.randint(1, 765)
        self.y = 100
        self.direction = random.randint(0, 1)
        self.image = pygame.image.load("./images/enemy.png")
        self.image = pygame.transform.scale(self.image, ((32, 32)))
 
    def EnemyMovement(self):
        #right = 0
        #left = 1
        if self.x > 2 and self.x < 765:    
            self.x = (self.x + 0.1, self.x - 0.1)[self.direction == 1]
        else:
            if self.x <= 2:
                self.x += .1
            elif self.x >= 765:
                self.x -= .1

            self.direction = (0, 1)[self.direction == 0]

    def RotateEnemy(self, player):
        enemy_rect = self.image.get_rect(center = (self.x, self.y))
        a = 5
        mx, my = player.GetPosition()
        dx, dy = mx - enemy_rect.centerx, my - enemy_rect.centery
        angle = math.degrees(math.atan2(-dy, dx)) - 90

        rot_image = pygame.transform.rotate(self.image, angle)
        rot_image_rect = rot_image.get_rect(center = enemy_rect.center)
        self.screen.blit(rot_image, rot_image_rect.bottomleft)
        

        