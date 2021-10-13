import math
import pygame
from pygame.constants import USEREVENT
from Player import PlayerShip as PS
from Enemy import EnemyShip as ES
from Bullet import Bullet as Bullets

screen = pygame.display.set_mode((800, 600))
player = PS(screen=screen)
toFire = False
bullet = Bullets(screen=screen, location=player.GetPosition(), damage=10)
running = True
enemies = []


explosionGroup = pygame.sprite.Group()

def main():
    
    #Initialize game
    pygame.init()

    #Set name
    pygame.display.set_caption("Space game")
    #Set icon
    pygame.display.set_icon(pygame.image.load("./images/ufo.png"))

    #Create enemies
    for k in range(5):
        enemy = ES(screen=screen, player=player)
        enemies.append(enemy)

    def CheckToCloseGame():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.QUIT:
                    global running
                    running = False
    def EnemyActions():
        for a in range(len(enemies)):
            enemies[a].EnemyMovementAndRotation(player=player)
            enemies[a].EnemyShoot(player)
    #Clock
    start_ticks = pygame.time.get_ticks()


    while running:
        #Set background color
        screen.fill((0, 0, 0))
       #Checks if escape button is pressed, if it is, it closes the game
        CheckToCloseGame()


        #Get second for timer
        seconds =(pygame.time.get_ticks()-start_ticks) / 1000
        
          
        EnemyActions()
        player.PlayerActions(enemies)
        pygame.display.update()

    pygame.display.quit()
    pygame.quit()
    
if __name__ == "__main__":
    main()