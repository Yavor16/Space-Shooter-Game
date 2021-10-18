import pygame
from StatsMenu_STATE import StatsMenu as SM

class Button():
    def __init__(self, screen, saveAndLoad, player):
        self.screen =  screen
        
        self.background = pygame.image.load("./images/backgrounds/bg-menu.jpg")
        self.background = pygame.transform.scale(self.background,(800,600))

        self.startBttn = pygame.image.load("./images/buttons/start.png")
        self.startImageRect = self.startBttn.get_rect()
        self.startImageRect.center = (400,200)

        self.exitBttn = pygame.image.load("./images/buttons/exit.png")
        self.exitImageRect = self.exitBttn.get_rect()
        self.exitImageRect.center = (400,350)
        
        self.statsBttn = pygame.image.load("./images/buttons/stats.png")
        self.statsImageRect = self.statsBttn.get_rect()
        self.statsImageRect.center = (600,150)

        self.saveAndLoad = saveAndLoad
        self.statusMenu_STATE = SM(screen = self.screen, saveAndLoad=saveAndLoad)
        self.player = player
        self.running = True
        
    def CheckIfEscapeIsPressed(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.QUIT:
                    self.running = False

    def Draw(self, screen):
        screen.blit(self.background, (0,0))
        self.CheckIfEscapeIsPressed()

        screen.blit(self.startBttn, (self.startImageRect.x, self.startImageRect.y))
        screen.blit(self.exitBttn, (self.exitImageRect.x, self.exitImageRect.y))
        screen.blit(self.statsBttn, (self.statsImageRect.x, self.statsImageRect.y))
              
        pos = pygame.mouse.get_pos()
        mousePresses = pygame.mouse.get_pressed()

        if self.statsImageRect.collidepoint(pos) and mousePresses[0]:
            self.statusMenu_STATE.showMenu = True
            
        if self.statusMenu_STATE.showMenu is True:
            self.statusMenu_STATE.Draw(self.screen)
        else:      
            if self.startImageRect.collidepoint(pos) and mousePresses[0]:
                self.running = False
            if self.exitImageRect.collidepoint(pos) and mousePresses[0]:
                self.saveAndLoad.SaveGame(deaths = self.player.deaths, score=self.player.score, enemiesKilled = self.player.enemiesKilled, timePlayed = self.player.timePlayed)
                pygame.display.quit()
                pygame.quit()
        