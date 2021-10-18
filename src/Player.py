import math
import pygame
from Bullet import Bullet as Bullets
from Explosion import Exposion as Explosion

class PlayerShip:

    def __init__(self, screen, saveAndLoad):
        self.screen = screen
        self.x = 360
        self.y = 460
        self.toFire = True
        self.image = pygame.image.load("./images/player.png")
        self.bullet = Bullets(screen=screen, location=(self.x, self.y), damage = 10)
        self.explosionGroup = pygame.sprite.Group()
        self.score = 0
        self.deaths = 0
        self.enemiesKilled = 0
        self.timePlayed = 0
        self.health = 100
        self.saveAndLoad = saveAndLoad

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

        self.RotateToMouse()
               
    def RotateToMouse(self):
        player_rect = self.image.get_rect(center = (self.x, self.y))

        mx, my = pygame.mouse.get_pos()
        dx, dy = mx - player_rect.centerx, my - player_rect.centery
        angle = math.degrees(math.atan2(-dy, dx)) - 90

        rot_image = pygame.transform.rotate(self.image, angle)
        rot_image_rect = rot_image.get_rect(center = player_rect.center)
        self.screen.blit(rot_image, rot_image_rect.topleft)
    
    def GetPosition(self):
        return (self.x, self.y)
    
    def PlayerActions(self, enemies):
        
        if self.health > 0:
            mousePresses = pygame.mouse.get_pressed()
            
            self.PlayerMovementAndRotation()
            
            if mousePresses[0] and self.toFire==False:
                self.toFire = True  
            self.Shoot(enemies)
        else:
            self.deaths+=1
            self.saveAndLoad.SaveGame(deaths = self.deaths, score=self.score, enemiesKilled = self.enemiesKilled, timePlayed = self.timePlayed)
            

    def DeathExplosion(self, pos):
        explosion = Explosion(pos[0], pos[1])
        self.explosionGroup.add(explosion)
        
    def Shoot(self, enemies):
        self.explosionGroup.draw(self.screen)
        self.explosionGroup.update()
        
        if self.toFire:
            try:
                if not self.bullet.killed: 
                    self.bullet.update()
                    for a in range(len(enemies)):
                        a-=1
                        distance = math.sqrt((math.pow(self.bullet.x - enemies[a].x, 2)) + (math.pow(self.bullet.y - enemies[a].y, 2)))
                        if distance < 35:
                            enemies[a].health-=self.bullet.damage
                            self.toFire = False 
                            self.bullet.killed = True
                            if enemies[a].health <=0:
                                self.score += enemies[a].score           
                                self.enemiesKilled += 1             
                                self.DeathExplosion((enemies[a].x , enemies[a].y))                             
                                enemies.remove(enemies[a])     
                else:
                    self.toFire = False
                    self.UpdateBulletSettings()
                    self.bullet.killed = False
            except Exception as e:
                print(e)
        else:
           self.UpdateBulletSettings()

    def UpdateBulletSettings(self):
        self.bullet.x = self.x
        self.bullet.y = self.y
        self.bullet.targetx, self.bullet.targety  = pygame.mouse.get_pos()
        self.bullet.dir = (self.bullet.targetx - self.bullet.x, self.bullet.targety - self.bullet.y )
