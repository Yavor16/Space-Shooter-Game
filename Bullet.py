import pygame

class Bullet:
    def __init__(self, screen, location):
        self.image = pygame.image.load("./images/bullet.png")
        
        self.screen = screen
        self.x = location[0]
        self.y = location[1] - 40

    def __del__(self):
        self.image = None
        self.screen = None
        self.x = None
        self.y=None

    def MoveBullet(self):
        self.y -= 1
        self.screen.blit(self.image, (self.x, self.y))
    


        