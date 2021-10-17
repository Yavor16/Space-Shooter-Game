import pygame

class PauseManu():
    def __init__(self, screen):
        self.screen = screen
        self.showMenu = False

        self.background = pygame.image.load("./images/backgrounds/bg-menu.jpg")
        self.background = pygame.transform.scale(self.background,(800,600))

        self.exitBttn = pygame.image.load("./images/buttons/exit.png")
        self.exitImageRect = self.exitBttn.get_rect()
        self.exitImageRect.center = (400,350)
        
        self.continueBttn = pygame.image.load("./images/buttons/continue.png")
        self.continueBttn = pygame.transform.scale(self.continueBttn, ((128, 40)))
        self.continueImageRect = self.exitBttn.get_rect()
        self.continueImageRect.center = (400,250)
        
    def Draw(self, screen):
        screen.blit(self.background, (0,0))
       
        screen.blit(self.continueBttn, (self.continueImageRect.x, self.continueImageRect.y))
        screen.blit(self.exitBttn, (self.exitImageRect.x, self.exitImageRect.y))
        
        pos = pygame.mouse.get_pos()
        mousePresses = pygame.mouse.get_pressed()

        if self.continueImageRect.collidepoint(pos) and mousePresses[0]:
            self.showMenu = False
        if self.exitImageRect.collidepoint(pos) and mousePresses[0]:
            pygame.display.quit()
            pygame.quit()