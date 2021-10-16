import pygame
from Player import PlayerShip as PS
from Enemy import EnemyShip as ES
from UserInterface import UserInterface as UI
from StartMenu_STATE import Button as Bttn
from Ingame_STATE import IngameActions as IA
#Initialize game
pygame.init()
#Set name
pygame.display.set_caption("Space game")
#Set icon
pygame.display.set_icon(pygame.image.load("./images/ufo.png"))

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("./images/background.png")

running = True

startMenu_STATE = Bttn(screen=screen)
ingame_STATE = IA(screen=screen)

def main():
    def CheckToCloseGame():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.QUIT:
                    global running
                    running = False
                    
    while running:
        if startMenu_STATE.running is False:
            #Set background image    
            screen.blit(background, (0,0))
            #Checks if escape button is pressed, if it is, it closes the game
            CheckToCloseGame()

            ingame_STATE.IngameActions()
            
        else:
            startMenu_STATE.Draw(screen=screen)
          
        pygame.display.update()

    pygame.display.quit()
    pygame.quit()
    
if __name__ == "__main__":
    main()