import math
import pygame
from pygame.constants import USEREVENT
from Player import PlayerShip as PS
from Enemy import EnemyShip as ES
from Bullet import Bullet as Bullets
from EnemyBullet import EnemyBullet as ENBullet


screen = pygame.display.set_mode((800, 600))
player = PS(screen=screen)
toFire = False
bullet = Bullets(screen=screen, location=player.GetPosition(), damage=10)
running = True
enemies = []
enemyBullets = []

def main():
    
    #Initialize game
    pygame.init()
    #Create window

    #Set name
    pygame.display.set_caption("Space game")
    #Set icon
    pygame.display.set_icon(pygame.image.load("./images/ufo.png"))

    #Create enemies
    
    for k in range(5):
        enemy = ES(screen=screen, player=player)
        enemies.append(enemy)

    for p in range(5):
        enemyBullet = ENBullet(screen=screen, player=player, location=(enemies[p].x, enemies[p].y), damage=10)
        enemyBullets.append(enemyBullet)
    def PlayerShoot():

        global toFire      
        global bullet

        if mousePresses[0] and toFire==False:
            toFire = True    
        if toFire:
            try:     
                if bullet.y <= 0 or bullet.y >= 600 or bullet.x >= 800 or bullet.x <= 0:
                    del bullet
                    toFire= False
                else:     
                    bullet.MoveBullet()                    
                    for a in range(len(enemies)):
                        distance = math.sqrt((math.pow(bullet.x - enemies[a].x, 2)) + (math.pow(bullet.y - enemies[a].y, 2)))
                        if distance < 27:
                            del enemies[a]
                            toFire = False                 
                            del bullet
                            enemies.remove(a)
                            enemies.sort()
                            enemyBullets.remove(a)
                            enemyBullets.sort()
            except:
                bullet = Bullets(screen=screen, location=player.GetPosition(), damage = 10)

    def CheckToCloseGame():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.QUIT:
                    global running
                    running = False
  
    def EnemyShoot(enemy, bullet, index) :    
        try:
            if bullet.y <= 0 or bullet.y >= 600 or bullet.x >= 800 or bullet.x <= 0:        
                del bullet
                    
            else:
                bullet.MoveBullet()
        except:
            enemyBullet = ENBullet(screen=screen, player=player, location=(enemies[p].x, enemies[p].y), damage=10)
            enemyBullets[index] = enemyBullet
 
    
    #Clock
    start_ticks = pygame.time.get_ticks()

    while running:
        #Set background color
        screen.fill((0, 0, 0))
        #Get all mouse buttons pressed       
        mousePresses = pygame.mouse.get_pressed()
        #Checks if escape button is pressed, if it is, it closes the game
        CheckToCloseGame()

        #Get second for timer
        seconds =(pygame.time.get_ticks()-start_ticks) / 1000

        player.PlayerMovementAndRotation()
        PlayerShoot()
        #Make each enemy move 
        for a in range(len(enemies)):
            enemies[a].EnemyMovementAndRotation(player=player)
            enemies[a].EnemyShoot(player)
           
        
        pygame.display.update()

    pygame.display.quit()
    pygame.quit()
    
if __name__ == "__main__":
    main()