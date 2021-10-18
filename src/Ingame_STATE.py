from Player import PlayerShip as PS
from Enemy import EnemyShip as ES
from UserInterface import UserInterface as UI
from StrongerEnemy import BossEnemy as StrongerEnemy
from Levels import Level as Level

class IngameActions():
    def __init__(self, screen, saveAndLoad):
        self.screen = screen
        self.player = PS(screen=screen, saveAndLoad=saveAndLoad)
        self.enemies = []
        self.finishedSpawningEne = False
        self.ui = UI(screen=screen,player=self.player)
        self.levels = Level()
        self.index = 0

    def SpawnEnemies(self):
        allLevelsList = self.AddLevelsToList()
                
        currentLevel = allLevelsList[self.index]
        self.ui.level = currentLevel[0]

        for a in range(currentLevel[1][0]):
            enemy = StrongerEnemy(screen=self.screen, player=self.player, damage=currentLevel[1][1])
            self.enemies.append(enemy)

        for k in range(currentLevel[1][2]):
            enemy = ES(screen=self.screen, player=self.player, damage=currentLevel[1][3])
            self.enemies.append(enemy)


        self.finishedSpawningEne = True
        
    def EnemyActions(self):
        for a in range(len(self.enemies)):
            if self.enemies[a].health > 0:
                self.enemies[a].AllEnemyEvents()
   
    def IngameActions(self):

        if not self.finishedSpawningEne:
            self.SpawnEnemies()
        if len(self.enemies) is 0:
            self.index+=1
            self.SpawnEnemies()
        #All enemy actions
        self.EnemyActions()
        #All player actions
        self.player.PlayerActions(self.enemies)
        #Updates UI
        self.ui.UIUpdate()
    
    def AddLevelsToList(self):
        eachLevel = list()
        
        if self.index == len(self.levels.levels) - 1:
            self.levels.CreateLevels()

        for item in self.levels.levels.items():
            eachLevel.append(item)    

        return eachLevel