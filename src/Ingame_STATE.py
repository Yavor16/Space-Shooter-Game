from Player import PlayerShip as PS
from Enemy import EnemyShip as ES
from UserInterface import UserInterface as UI
from StrongerEnemy import BossEnemy as StrongerEnemy
class IngameActions():
    def __init__(self, screen, saveAndLoad):
        self.screen = screen
        self.player = PS(screen=screen, saveAndLoad=saveAndLoad)
        self.enemies = []
        self.finishedSpawningEne = False
        self.ui = UI(screen=screen,player=self.player)
    
    def SpawnEnemies(self):
        for k in range(5):
            enemy = ES(screen=self.screen, player=self.player)
            self.enemies.append(enemy)

        for a in range(2):
            enemy = StrongerEnemy(screen=self.screen, player=self.player)
            self.enemies.append(enemy)
        self.finishedSpawningEne = True
        
    def EnemyActions(self):
        for a in range(len(self.enemies)):
            if self.enemies[a].health > 0:
                self.enemies[a].AllEnemyEvents()
   
    def IngameActions(self):
        if not self.finishedSpawningEne:
            self.SpawnEnemies()

        #All enemy actions
        self.EnemyActions()
        #All player actions
        self.player.PlayerActions(self.enemies)
        #Updates UI
        self.ui.UIUpdate()
            