import pygame

class Button():
    def __init__(self, screen):
        self.background = pygame.image.load("./images/bg-menu.jpg")
        self.background = pygame.transform.scale(self.background,(800,600))

        self.screen =  screen
        self.startBttn = pygame.image.load("./images/buttons/start.png")
        self.startImageRect = self.startBttn.get_rect()
        self.startImageRect.center = (400,200)

        self.exitBttn = pygame.image.load("./images/buttons/exit.png")
        self.exitImageRect = self.exitBttn.get_rect()
        self.exitImageRect.center = (400,350)
        
        self.running = True

    def CheckToCloseGame(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.QUIT:
                    self.running = False

    def Draw(self, screen):
        screen.blit(self.background, (0,0))
        self.CheckToCloseGame()

        screen.blit(self.startBttn, (self.startImageRect.x, self.startImageRect.y))
        screen.blit(self.exitBttn, (self.exitImageRect.x, self.exitImageRect.y))
        
        pos = pygame.mouse.get_pos()
        mousePresses = pygame.mouse.get_pressed()

        if self.startImageRect.collidepoint(pos) and mousePresses[0]:
            self.running = False
        if self.exitImageRect.collidepoint(pos) and mousePresses[0]:
            pygame.display.quit()
            pygame.quit()
    