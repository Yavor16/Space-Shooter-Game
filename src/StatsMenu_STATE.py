import pygame

class StatsMenu():
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load("./images/backgrounds/bg-menu.jpg")
        self.background = pygame.transform.scale(self.background,(800,600))

        self.backBttn = pygame.image.load("./images/buttons/leftarrow.png")
        self.backBttn = pygame.transform.scale(self.backBttn,(32,32))
        self.backBttnImageRect = self.backBttn.get_rect()
        self.backBttnImageRect.center = (200,150)
       
        self.showMenu = False

    def Draw(self, screen):
        screen.blit(self.background, (0,0))
       
        screen.blit(self.backBttn, (self.backBttnImageRect.x, self.backBttnImageRect.y))
        
        pos = pygame.mouse.get_pos()
        mousePresses = pygame.mouse.get_pressed()

        if self.backBttnImageRect.collidepoint(pos) and mousePresses[0]:
            self.showMenu = False
        