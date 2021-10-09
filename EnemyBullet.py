from Bullet import Bullet
import pygame
class EnemyBullet(Bullet):

    def __init__(self, screen, player, location, damage):
        self.screen = screen
        self.x = location[0]
        self.y = location[1]
        self.targetx = player.x
        self.targety = player.y
        self.dir = (self.targetx - self.x, self.targety - self.y )
        self.image = pygame.image.load("./images/bullet.png")
        self.damage = damage
    def UpdatePlayerPosition(self, player):
        self.targetx, self.targety = player
        
    