import math
import pygame
from Bullet import Bullet as Bullets
from Enemy import EnemyShip
from Explosion import Exposion as Explosion

class PlayerShip:

    def __init__(self, screen):
        self.screen = screen
        self.x = 360
        self.y = 460
        self.toFire = True
        self.image = pygame.image.load("./images/player.png")
        self.bullet = Bullets(screen=screen, location=(self.x, self.y), damage = 10)
        self.lastDeathEnemy : EnemyShip = None

        self.explosionGroup = pygame.sprite.Group()

    def PlayerMovementAndRotation(self):

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a] and self.x > 10:
            self.x -= 0.5              
        if keys[pygame.K_d] and self.x < 765:
            self.x += 0.5
        if keys[pygame.K_w] and self.y > 15:
            self.y -= 0.5
        if keys[pygame.K_s] and self.y < 570:
            self.y += 0.5

        self.RotateToMouse(window=self.screen)
               
    def RotateToMouse(self, window):
        player_rect = self.image.get_rect(center = (self.x, self.y))

        mx, my = pygame.mouse.get_pos()
        dx, dy = mx - player_rect.centerx, my - player_rect.centery
        angle = math.degrees(math.atan2(-dy, dx)) - 90

        rot_image = pygame.transform.rotate(self.image, angle)
        rot_image_rect = rot_image.get_rect(center = player_rect.center)
        window.blit(rot_image, rot_image_rect.topleft)
    
    def GetPosition(self):
        return (self.x, self.y)
    
    def PlayerShoot(self, enemies):
        self.explosionGroup.draw(self.screen)
        self.explosionGroup.update()
        if self.toFire:
            try:     
                if self.bullet.y <= 0 or self.bullet.y >= 600 or self.bullet.x >= 800 or self.bullet.x <= 0:
                    del self.bullet
                    self.toFire= False
                else:       
                    self.bullet.MoveBullet()                    
                    for a in range(len(enemies)):
                        distance = math.sqrt((math.pow(self.bullet.x - enemies[a].x, 2)) + (math.pow(self.bullet.y - enemies[a].y, 2)))
                        if distance < 27:
                            self.lastDeathEnemy = enemies[a]
                            self.DeathExplosion((enemies[a].x , enemies[a].y))
                            del enemies[a]
                            del self.bullet
                            self.toFire = False                 
                            enemies.remove(a)
                            enemies.sort()
            except:
                self.bullet = Bullets(screen=self.screen, location=(self.x, self.y), damage = 10)
  
    def PlayerActions(self, enemies):
        mousePresses = pygame.mouse.get_pressed()

        self.PlayerMovementAndRotation()
        if mousePresses[0] and self.toFire==False:
            self.toFire = True  
        self.PlayerShoot(enemies=enemies)
    
    def DeathExplosion(self, pos):
        explosion = Explosion(pos[0], pos[1])
        self.explosionGroup.add(explosion)