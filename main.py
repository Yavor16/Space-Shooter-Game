import pygame
from pygame.constants import USEREVENT
from Player import PlayerShip as PS
from Enemy import EnemyShip as ES
from Bullet import Bullet as Bullets
from EnemyBullet import EnemyBullet as ENBullet

def main():
    
    #Initialize game
    pygame.init()
    #Create window
    screen = pygame.display.set_mode((800, 600))

    #Set name
    pygame.display.set_caption("Space game")
    #Set icon
    pygame.display.set_icon(pygame.image.load("./images/ufo.png"))

    #Player
    player = PS(screen=screen)
    #Enemy
    enemy = ES(screen=screen)
    #On true a bullet is fired
    toFire = False

    #Clock
    start_ticks = pygame.time.get_ticks()
    running = True
    while running:
        #Set background color
        screen.fill((0, 0, 0))
        #Get all mouse buttons pressed       
        mousePresses = pygame.mouse.get_pressed()
        #Get second for timer
        seconds =(pygame.time.get_ticks()-start_ticks) / 1000

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.QUIT:
                    running = False
                
        player.PlayerMovementAndRotation()
        enemy.EnemyMovementAndRotation(player=player)

        if mousePresses[0] and toFire == False:
            bullet = Bullets(screen=screen, location=player.GetPosition(), damage=10)
            toFire = True    
        if toFire:
            try:     
                if bullet.y <= 0 or bullet.y >= 590 or bullet.x >= 790 or bullet.x <= 0:
                    del bullet
                    toFire= False
                else: 
                    bullet.MoveBullet()
            except:
                bullet = Bullets(screen=screen, location=player.GetPosition())
        
        if  enemy.toFire == False:
            enemyBullet = ENBullet(screen=screen, location=(enemy.x, enemy.y), player=player, damage=10)
            enemy.toFire = True
        if enemy.toFire:
            try:
                if enemyBullet.y <= 0 or enemyBullet.y >= 590 or enemyBullet.x >= 790 or enemyBullet.x <= 0:
                    del enemyBullet
                    enemy.toFire = False
                else:
                    enemyBullet.MoveBullet()
            except:
                enemyBullet = ENBullet(screen=screen, location=(enemy.x, enemy.y), player=player, damage=10)
      
        
        pygame.display.update()

    pygame.display.quit()
    pygame.quit()
    
if __name__ == "__main__":
    main()