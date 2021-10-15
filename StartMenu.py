import pygame

class Button():
    def __init__(self, screen, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()

        self.screen =  screen
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image,(int(width*scale), (int(height * scale))))
        self.imageRect = self.image.get_rect()
        self.imageRect.topleft = (x,y)

    def Draw(self):
        pos = pygame.mouse.get_pos()
        if self.imageRect.collidepoint(pos):
            print("Hover")

        self.screen.blit(self.image, (self.imageRect.x, self.imageRect.y))