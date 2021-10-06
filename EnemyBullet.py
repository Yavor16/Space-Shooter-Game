import pygame
from Bullet import Bullet

class EnemyBullet(Bullet):

    def __init__(self, screen, location, player):
        super().__init__(screen, location)
        self.image = pygame.image.load("./images/bullet.png")
        self.x = location[0]
        self.y = location[1]
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.targetx = player.x
        self.targety = player.y
        self.dir = (self.targetx - self.x, self.targety - self.y )
        
    

    