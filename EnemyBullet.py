import pygame
from Bullet import Bullet
import math
class EnemyBullet(Bullet):

    def __init__(self, screen, location, player):
        super().__init__(screen, location)
        self.image = pygame.image.load("./images/bullet.png")
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.x = location[0]
        self.y = location[1]
        self.targetx, self.targety  = player
        self.dir = (self.targetx - self.x, self.targety - self.y )

    
    def __del__(self):
        super().__del__()

    def Test(self):
        length = math.hypot(*self.dir) 

        if length == 0.0:
            self.dir = (0 , -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
    def MoveBullet(self):
        self.x += self.dir[0] / 500
        self.y += self.dir[1] / 500

        image_rect = self.image.get_rect(center = (self.x, self.y))     

        self.screen.blit(self.image, image_rect)
    


    