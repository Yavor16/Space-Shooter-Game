import pickle

class SaveAndLoad():
    def __init__(self):
        self.deaths = 0
        self.enemiesKilled = 0
        self.bestScore = 0
        self.timePlayed = 0
        self.displayTime = 0

    def SaveGame(self, deaths, score, enemiesKilled, timePlayed):

        self.deaths += deaths
        self.enemiesKilled += enemiesKilled
        #self.bestScore += score
        self.timePlayed += timePlayed
        self.bestScore = (self.bestScore, score)[score > self.bestScore]
        print(self.bestScore)
        with open("savegame", "wb") as f:
            pickle.dump((self.timePlayed, self.bestScore, self.enemiesKilled, self.deaths), f)
            f.close()
            
    def LoadGame(self):
        try:
            with open("savegame", "rb") as f:
                loadedSave = list()
                
                while True:
                    try: loadedSave.append(pickle.load(f))
                    except EOFError: break

                self.timePlayed = loadedSave[0][0]
                self.bestScore = loadedSave[0][1]
                self.enemiesKilled = loadedSave[0][2]
                self.deaths = loadedSave[0][3]
                
                self.FromMinutesToHours()

                f.close()
        except Exception:
            self.SaveGame(0,0,0,0)
    
    def FromMinutesToHours(self):
        if self.timePlayed < 60:
           self.displayTime = self.timePlayed / 100
        else:
            self.displayTime = int(self.timePlayed / 60)
    