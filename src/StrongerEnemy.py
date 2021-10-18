from Enemy import EnemyShip
from EnemyBullet import EnemyBullet as EnemyBull
import pygame

class BossEnemy(EnemyShip):
    def __init__(self, screen, player):
        super().__init__(screen, player)
        self.image = pygame.image.load("./images/secondenemy.png")
        self.image = pygame.transform.scale(self.image, ((48, 48)))
        self.health = 40
        self.enemyBullet = EnemyBull(screen=self.screen, player=player, location=(self.x, self.y), damage=20)
        self.score = 2 
        self.maxHealth = 40
        self.damage = 20