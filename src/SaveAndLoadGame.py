import pickle
from Statistics import Stats as stats

class SaveAndLoad():
    def __init__(self, enemieKilled, deaths, timePlayed, bestScore):
        self.enemieKilled = enemieKilled
        self.deaths = deaths
        self.timePlayed = timePlayed
        self.bestScore = bestScore
        self.savedStats = stats()
        self.loadedStats = 0
    def SaveStats(self):
        with open("savegame", "wb") as f:
            pickle.dump(self.savedStats, f)

    def LoadStats(self):
        with open("savegame", "rb") as f:
            self.loadedStats = pickle.load(f)

    