import pygame
from Bullet import Bullet

class EnemyBullet(Bullet):

    def __init__(self, screen, location,player, damage):
        super().__init__(screen, location, damage)
        self.x = location[0]
        self.y = location[1]
        self.targetx = player.x
        self.targety = player.y
        self.dir = (self.targetx - self.x, self.targety - self.y )

    