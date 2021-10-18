import pygame
class UserInterface():
    def __init__(self, screen, player):
        self.font = pygame.font.SysFont('arial', 30, False,False)
        self.start_ticks = pygame.time.get_ticks()
        self.player = player
        self.minutes:int = 0
        self.screen = screen
        self.level = 0

    def CalculateTime(self):
        time =int((pygame.time.get_ticks()-self.start_ticks) / 1000) 
        
        if time != 0 and time % 60 == 0 :
            self.minutes= time / 60

        seconds = time - self.minutes *60
        #self. minutes = time - self.hours * 60

        self.player.timePlayed = int(self.minutes)
        return (self.minutes, seconds)

    def DisplayClock(self):
        minutes = int(self.CalculateTime()[0])
        seconds = int(self.CalculateTime()[1])

        if seconds < 10:
            seconds = "0" + str(seconds)
        if minutes < 10:
            minutes = "0" + str(minutes)

        img = self.font.render(f"{minutes}:{seconds}", True, (255,255,255))
        self.screen.blit(img, (0, 110))

    def DisplayText(self, text:str, thing, position):
        img = self.font.render(f"{text}: " + str(thing), True, (255,255,255))
        self.screen.blit(img, position)


    def UIUpdate(self):
        self.DisplayClock()
        self.DisplayText(text="Wave", thing=self.level, position=(00, 60))
        self.DisplayText(text="Score", thing = self.player.score, position= (0, 85))
        self.HealthBar()
    
    def HealthBar(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (0 , 0, 100 * 2, 30))
        pygame.draw.rect(self.screen, (0, 255, 0), (0 , 0, self.player.health * 2, 30))

  
  