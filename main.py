import pygame
from Player import PlayerShip as PS
from Enemy import EnemyShip as ES
from UserInterface import UserInterface as UI


screen = pygame.display.set_mode((800, 600))
player = PS(screen=screen)
running = True
enemies = []


def main():
    
    #Initialize game
    pygame.init()
    #Set name
    pygame.display.set_caption("Space game")
    #Set icon
    pygame.display.set_icon(pygame.image.load("./images/ufo.png"))
    
    ui = UI(screen=screen,player=player)

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
            if enemies[a].health > 0:
                enemies[a].AllEnemyEvents()
            
    while running:
        #Set background color
        screen.fill((0, 0, 0))
        #Updates UI
        ui.UIUpdate()
        #Checks if escape button is pressed, if it is, it closes the game
        CheckToCloseGame()
          
        EnemyActions()
        player.PlayerActions(enemies)
        pygame.display.update()

    pygame.display.quit()
    pygame.quit()
    
if __name__ == "__main__":
    main()