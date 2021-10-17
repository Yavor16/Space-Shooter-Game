import pygame
from StartMenu_STATE import Button as Bttn
from Ingame_STATE import IngameActions as IA
from PauseMenu_STATE import PauseManu as PM

#Initialize game
pygame.init()
#Set name
pygame.display.set_caption("Space game")
#Set icon
pygame.display.set_icon(pygame.image.load("./images/ufo.png"))

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("./images/backgrounds/background.png")

showPauseMenu = False

startMenu_STATE = Bttn(screen=screen)
ingame_STATE = IA(screen=screen)
pauseMenu_STATE = PM(screen=screen)

def main():
    def CheckIfEscapeIsPressed():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.QUIT:
                    global showPauseMenu
                    pauseMenu_STATE.showMenu = (False, True)[pauseMenu_STATE.showMenu == False] 
    while True:
        if startMenu_STATE.running is False:

            #Set background image    
            screen.blit(background, (0,0))
            #Checks if escape button is pressed, if it is, it closes the game
            CheckIfEscapeIsPressed()

            if pauseMenu_STATE.showMenu is True:
                pauseMenu_STATE.Draw(screen=screen)
            else:
                ingame_STATE.IngameActions()
        else:
            startMenu_STATE.Draw(screen=screen)
          
        pygame.display.update()
    
if __name__ == "__main__":
    main()