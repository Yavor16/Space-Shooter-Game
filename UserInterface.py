import pygame

class UserInterface():
    def __init__(self, screen, player):
        self.font = pygame.font.SysFont('arial', 60, False,False)
        self.start_ticks = pygame.time.get_ticks()
        self.player = player
        self.minutes:int = 0
        self.screen = screen
    def CalculateTime(self):
        time =int((pygame.time.get_ticks()-self.start_ticks) / 1000)
        
        if time != 0 and time % 60 == 0 :
            self.minutes= time / 60
        seconds = time - self.minutes *60

        return (self.minutes, seconds)
    def DisplayClock(self):
        minutes = int(self.CalculateTime()[0])
        seconds = int(self.CalculateTime()[1])

        if seconds < 10:
            seconds = "0" + str(seconds)
        if minutes < 10:
            minutes = "0" + str(minutes)
        #print(f"{minutes}:{seconds}")
        img = self.font.render(f"{minutes}:{seconds}", True, (255,255,255))
        self.screen.blit(img, (100, 100))

    def DisplayText(self, text:str, thing):
        img = self.font.render(f"{text}: " + str(thing), True, (255,255,255))
        self.screen.blit(img, (20, 20))
    
    def UIUpdate(self):
        self.DisplayClock()
        self.DisplayText(text="Score", thing = self.player.score)