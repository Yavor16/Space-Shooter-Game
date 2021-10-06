import pygame
from Player import PlayerShip as PS
from Enemy import EnemyShip as ES
from Bullet import Bullet as Bullets
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

    #Bullet
    toFire = False

    running = True
    while running:
        #Set background color
        screen.fill((0, 0, 0))
        keys = pygame.key.get_pressed()        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.QUIT:
                    running = False
                
        player.PlayerMove()
        player.RotateToMouse(window=screen)

        #enemy.LeftandRightEnemyMovement()   
        #enemy.UpandDownEnemyMovement()     
        enemy.RotateEnemy(player)
        enemy.Shoot(player=player)

        if keys[pygame.K_SPACE] and toFire == False:
            bullet = Bullets(screen=screen, location=player.GetPosition())
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
            
        pygame.display.update()

    pygame.display.quit()
    pygame.quit()
    

if __name__ == "__main__":
    main()