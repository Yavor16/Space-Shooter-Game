import pygame
from StartMenu_STATE import Button as Bttn
from Ingame_STATE import IngameActions as IA
from PauseMenu_STATE import PauseManu as PM
from SaveAndLoadStats import SaveAndLoad as saveAndLoad

#Initialize game
pygame.init()
#Set name
pygame.display.set_caption("Space game")
#Set icon
pygame.display.set_icon(pygame.image.load("./images/ufo.png"))

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("./images/backgrounds/background.png")

showPauseMenu = False

saveAndLoadGameSave = saveAndLoad() 
ingame_STATE = IA(screen=screen, saveAndLoad=saveAndLoadGameSave)
startMenu_STATE = Bttn(screen=screen, saveAndLoad=saveAndLoadGameSave, player=ingame_STATE.player)
pauseMenu_STATE = PM(screen=screen, player = ingame_STATE.player, saveAndLoad=saveAndLoadGameSave)

def main():
    def CheckIfEscapeIsPressed():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.QUIT:
                    global showPauseMenu
                    pauseMenu_STATE.showMenu = (False, True)[pauseMenu_STATE.showMenu == False] 
    
    def RestartGame():
        global ingame_STATE
        del ingame_STATE
        
        ingame_STATE = IA(screen=screen, saveAndLoad=saveAndLoadGameSave)
    
    while True:
        if startMenu_STATE.running is False :
            if ingame_STATE.player.health <= 0 : startMenu_STATE.running = True, RestartGame()
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
    saveAndLoadGameSave.LoadGame()
    main()