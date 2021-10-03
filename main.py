import pygame
from Player import PlayerShip as PS
from Enemy import EnemyShip as ES

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

    running = True

    while running:

        #Set background color
        screen.fill((0, 0, 0))
        
       
        for event in pygame.event.get():
            if event.type == pygame.K_ESCAPE or event.type == pygame.QUIT:
                running = False

        player.PlayerMove(event=event)
        player.RotateToMouse(window=screen)

        enemy.EnemyMovement()        
        enemy.RotateEnemy(player)
        
        pygame.display.update()

    pygame.display.quit()
    pygame.quit()
    

if __name__ == "__main__":
    main()