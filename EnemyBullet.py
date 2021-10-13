from Bullet import Bullet
import pygame
import random

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
        self.bulletSpeed = random.randint(300, 700)
    def UpdatePlayerPosition(self, player):
        self.targetx, self.targety = player
    
    
    def MoveBullet(self):

        self.x += self.dir[0] / self.bulletSpeed
        self.y += self.dir[1] / self.bulletSpeed

        image_rect = self.image.get_rect(center = (self.x, self.y))     

        self.screen.blit(self.image, image_rect)
