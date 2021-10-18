class Level():
    def __init__(self):
        #Index[0] is how much boss enemies to spawn and index[1] is their damage
        #Index[2] is how much normal enemies to spawn and index[3] is their damage
        
        self.newLevelNum = 9
        self.newEnemiesAmount = 5
        self.levels = {
                "1":(0, 0, 3 , 10),
                "2":(0, 0, 4 , 10),
                "3":(1, 15, 2 , 10),
                "4":(1, 15, 3 , 10),
                "5":(2, 15, 3 , 10),
                "6":(2, 20, 3 , 10),
                "7":(3, 20, 3 , 10),
                "8":(4, 20, 4 , 15)
        }

    def CreateLevels(self):
        self.levels[f"{self.newLevelNum}"] = (self.newEnemiesAmount, 20, self.newEnemiesAmount, 15)
        
        self.newLevelNum+=1
        self.newEnemiesAmount+=1