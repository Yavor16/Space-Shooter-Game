import math
import pygame
import random
from EnemyBullet import EnemyBullet as EnemyBull

class EnemyShip(pygame.sprite.Sprite):
    def __init__(self, screen, player, damage):
        super().__init__()
        self.screen = screen
        self.x = random.randint(1, 765)
        self.y = -30
        self.player = player
        self.direction = random.randint(0, 1)
        self.updirection = random.randint(0,1)
        self.image = pygame.image.load("./images/enemy.png")
        self.image = pygame.transform.scale(self.image, ((32, 32)))
        self.startLocation = (self.x, self.y)
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.enemyBullet = EnemyBull(screen=self.screen, player=player, location=(self.rect.x, self.rect.y), damage=10)
        self.damage = damage
        self.maxHealth = 30
        self.health = 30
        self.score = 1

    def __del__(self):
        self.screen = None
        self.image = None

    def LeftandRightEnemyMovement(self):
        if self.x > 30 and self.x < 765:    
            self.x = (self.x + 0.1, self.x - 0.1)[self.direction == 1]
        else:
            if self.x <= 30:
                self.x += 0.1
            elif self.x >= 765:
                self.x -= 0.1
            self.direction = (0, 1)[self.direction == 0]
            
    def UpandDownEnemyMovement(self):
        if self.y > 30 and self.y < 400:
            self.y = (self.y + 0.1, self.y - 0.1)[self.updirection == 0]
        else:
            if self.y <= 30:
                self.y += 0.1
            elif self.y >= 400:
                self.y -= 0.1
            self.updirection = (0, 1)[self.updirection == 0]

    def EnemyMovementAndRotation(self):

        randomDistanceForX = random.randint(300, 500)
        randomDistanceForY = random.randint(300, 700)

        if abs(self.startLocation[0] - self.x) >= randomDistanceForX:
            self.direction = (0, 1)[self.direction == 0]
        if abs(self.startLocation[1] - self.y) >= randomDistanceForY:
            self.updirection = (0, 1)[self.updirection == 0]

        self.UpandDownEnemyMovement()
        self.LeftandRightEnemyMovement()
        self.RotateEnemy()

    def RotateEnemy(self):
        enemy_rect = self.image.get_rect(center = (self.x, self.y))
        
        mx, my = self.player.GetPosition()
        dx, dy = mx - enemy_rect.centerx, my - enemy_rect.centery
        angle = math.degrees(math.atan2(-dy, dx)) - 90

        rot_image = pygame.transform.rotate(self.image, angle)
        rot_image_rect = rot_image.get_rect(center = enemy_rect.center)
        self.screen.blit(rot_image, rot_image_rect.center)
    
    def EnemyShoot(self):
        try:
            if self.enemyBullet.y <= 0 or self.enemyBullet.y >= 600 or self.enemyBullet.x >= 800 or self.enemyBullet.x <= 0:        
                del self.enemyBullet
            else:
                self.enemyBullet.MoveBullet()
                distance = math.sqrt((math.pow(self.enemyBullet.x - self.player.x, 2)) + (math.pow(self.enemyBullet.y - self.player.y, 2)))
                if distance < 27:
                    self.player.health-=self.damage
                    del self.enemyBullet
        except:
            self.enemyBullet = EnemyBull(screen=self.screen, player=self.player, location=(self.x, self.y), damage=10)
   
    def HealthBar(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (self.x , self.y - 15, self.maxHealth, 10))
        pygame.draw.rect(self.screen, (0, 255, 0), (self.x , self.y - 15, self.health, 10))

    def AllEnemyEvents(self):
        self.HealthBar()
        self.EnemyMovementAndRotation()
        self.EnemyShoot()
