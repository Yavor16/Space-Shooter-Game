import math
import pygame
class Bullet:
    def __init__(self, screen, location, damage):
        self.image = pygame.image.load("./images/bullet.png")
        self.targetx, self.targety  = pygame.mouse.get_pos()
        self.screen = screen
        self.x = location[0]
        self.y = location[1] 
        self.dir = (self.targetx - self.x, self.targety - self.y )
        self.damage = damage
    def __del__(self):
        self.image = None
        self.screen = None
        self.x = None
        self.y = None
        self.dir = None
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

    def isColliding(self, enemy):
        distance = math.sqrt((math.pow(self.x - enemy[0], 2)) + (math.pow(self.y - enemy[1], 2)))
        if distance < 27:
            return True
        else:
            return False 

    def DestroyEnemy(self, enemy, enemyLocation):
        if self.isColliding(enemyLocation):
            del enemy



        