import pygame
from Statistics import Stats as Stats
from SaveAndLoadGame import SaveAndLoad as SAL

class StatsMenu():
    def __init__(self, screen):
        
        self.font = pygame.font.SysFont('arial', 35, False,False)
        self.stats = Stats()
        self.screen = screen
   
        self.background = pygame.image.load("./images/backgrounds/bg-menu.jpg")
        self.background = pygame.transform.scale(self.background,(800,600))

        self.backBttn = pygame.image.load("./images/buttons/leftarrow.png")
        self.backBttn = pygame.transform.scale(self.backBttn,(32,32))
        self.backBttnImageRect = self.backBttn.get_rect()
        self.backBttnImageRect.center = (200,150)
       
        self.showMenu = False
        self.loadGame = SAL(self.stats.enemieKilled, self.stats.deaths, self.stats.timePlayed, self.stats.bestScore)
        self.loadGame.LoadStats()
        self.stats.enemieKilled = self.loadGame.loadedStats.enemieKilled 
        self.stats.deaths = self.loadGame.loadedStats.deaths
        self.stats.bestScore = self.loadGame.loadedStats.bestScore
        self.stats.timePlayed = self.loadGame.loadedStats.timePlayed

        self.textes = {}
    
    def Draw(self, screen):
        screen.blit(self.background, (0,0))
        screen.blit(self.backBttn, (self.backBttnImageRect.x, self.backBttnImageRect.y))
    
        self.DisplayText()
        
        pos = pygame.mouse.get_pos()
        mousePresses = pygame.mouse.get_pressed()

        if self.backBttnImageRect.collidepoint(pos) and mousePresses[0]:
            self.showMenu = False
            
    def AddTextToMenu(self):
        enemiesKilled = self.font.render("Enemies killed: " + str(self.stats.enemieKilled), False, (0, 250, 154))
        deaths = self.font.render("Deaths: " + str(self.stats.deaths), False, (0, 250, 154))
        timePlayed = self.font.render("Time played: " + str(self.stats.timePlayed), False, (0, 250, 154))
        bestScore  = self.font.render("Best score: " + str(self.stats.bestScore), False, (0, 250, 154))

        return {bestScore     : (200, 460),
                deaths        : (200, 260),
                timePlayed    : (200, 160),
                enemiesKilled : (200, 360)}

    def DisplayText(self):
        data = self.AddTextToMenu()
        for value, key in data.items():
            self.screen.blit(value, key)
    
