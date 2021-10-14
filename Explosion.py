import pygame

class Exposion(pygame.sprite.Sprite):
    def __init__(self, x ,y) :
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 6):
            img = pygame.image.load(f"./images/explosion sprites/exp{num}.png")
            img = pygame.transform.scale(img, (100, 100))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0
        self.toPlay = False

    def update(self):
        explosiongSpeed = 110
        self.counter+=1

        if self.counter >= explosiongSpeed and self.index < len(self.images ) - 1:
            self.counter = 0
            self.index +=1
            self.image = self.images[self.index]
        if self.index >= len(self.images) - 1 and self.counter >= explosiongSpeed:
            self.kill()