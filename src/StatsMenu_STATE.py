import pygame
class StatsMenu():
    def __init__(self, screen, saveAndLoad):
        
        self.font = pygame.font.SysFont('arial', 35, False,False)
        self.screen = screen
   
        self.background = pygame.image.load("./images/backgrounds/bg-menu.jpg")
        self.background = pygame.transform.scale(self.background,(800,600))

        self.backBttn = pygame.image.load("./images/buttons/leftarrow.png")
        self.backBttn = pygame.transform.scale(self.backBttn,(32,32))
        self.backBttnImageRect = self.backBttn.get_rect()
        self.backBttnImageRect.center = (200,150)
       
        self.showMenu = False
        self.textes = {}
        self.saveAndLoad = saveAndLoad
    
    def Draw(self, screen):
        screen.blit(self.background, (0,0))
        screen.blit(self.backBttn, (self.backBttnImageRect.x, self.backBttnImageRect.y))
    
        self.DisplayText()
        
        pos = pygame.mouse.get_pos()
        mousePresses = pygame.mouse.get_pressed()

        if self.backBttnImageRect.collidepoint(pos) and mousePresses[0]:
            self.showMenu = False
            
    def AddTextToMenu(self):
        enemiesKilled = self.font.render("Enemies killed: " + str(self.saveAndLoad.enemiesKilled), False, (0, 250, 154))
        deaths = self.font.render("Deaths: " + str(self.saveAndLoad.deaths), False, (0, 250, 154))
        timePlayed = self.font.render("Time played(h): " + str(self.saveAndLoad.displayTime), False, (0, 250, 154))
        bestScore  = self.font.render("Best score: " + str(self.saveAndLoad.bestScore), False, (0, 250, 154))

        return {bestScore     : (200, 460),
                deaths        : (200, 260),
                timePlayed    : (200, 160),
                enemiesKilled : (200, 360)}

    def DisplayText(self):
        data = self.AddTextToMenu()
        for value, key in data.items():
            self.screen.blit(value, key)
    
