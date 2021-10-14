import math
import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, location, damage):
        super().__init__()
        self.image = pygame.image.load("./images/bullet.png")
        self.targetx, self.targety  = pygame.mouse.get_pos()
        self.screen = screen
        self.x = location[0]
        self.y = location[1] 
        self.dir = (self.targetx - self.x, self.targety - self.y )
        self.damage = damage
        self.killed = False
        self.rect = self.image.get_rect()
    def __del__(self):
        self.image = None
        self.screen = None
    def Test(self):
        length = math.hypot(*self.dir) 

        if length == 0.0:
            self.dir = (0 , -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
    def UpdateStats(self, x, y):
        self.targetx, self.targety  = pygame.mouse.get_pos()
        self.x = x
        self.y = y
        self.dir = (self.targetx - self.x, self.targety - self.y )
        self.killed = False
        
    def update(self):
        if not self.killed:
            if self.y <= 0 or self.y >= 600 or self.x >= 800 or self.x <= 0:
                self.kill()
                self.killed = True
            else:
                self.x += self.dir[0] / 500
                self.y += self.dir[1] / 500

                image_rect = self.image.get_rect(center = (self.x, self.y))     

                self.screen.blit(self.image, image_rect)

