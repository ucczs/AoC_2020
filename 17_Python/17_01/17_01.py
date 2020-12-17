import numpy as np
import itertools

class MapCoordiante:
    def __init__(self, activeState, neighboursActive):
        self.activeState = activeState
        self.neighboursActive = neighboursActive

class Map:
    # map[Z][Y][X]
    def __init__(self, xMax, yMax, zMax):
        self.xMax = xMax
        self.yMax = yMax
        self.zMax = zMax
        self.coordinates = np.zeros((zMax, yMax, xMax))
        self.neightboursCnt = np.zeros((zMax, yMax, xMax))
        self.activeTotal = 0

    def countActive(self):
        for xCoord in range(self.xMax):
            for yCoord in range(self.yMax):
                for zCoord in range(self.zMax):
                    if self.coordinates[zCoord][yCoord][xCoord] == True:
                        self.activeTotal += 1

    def printMap(self):
        print("New State:")
        for zCoord in range(self.zMax):
            print("\n")
            for yCoord in range(self.yMax):
                for xCoord in range(self.xMax):
                    if self.coordinates[zCoord][yCoord][xCoord] == True:
                        print("#", end="")
                    else:
                        print(".", end="")
                print()

    def updateState(self):
        for xCoord in range(self.xMax):
            for yCoord in range(self.yMax):
                for zCoord in range(self.zMax):

                    # currently active
                    if self.coordinates[zCoord][yCoord][xCoord] == True:
                        if not (self.neightboursCnt[zCoord][yCoord][xCoord] == 2 or self.neightboursCnt[zCoord][yCoord][xCoord] == 3):
                            self.coordinates[zCoord][yCoord][xCoord] = False

                    # currently inactive
                    else:
                        if self.neightboursCnt[zCoord][yCoord][xCoord] == 3:
                            self.coordinates[zCoord][yCoord][xCoord] = True

    def countNeighbours(self):
        self.neightboursCnt = np.zeros((self.zMax, self.yMax, self.xMax))

        for xCoord in range(self.xMax):
            for yCoord in range(self.yMax):
                for zCoord in range(self.zMax):
                    for xDiff, yDiff, zDiff in itertools.product(set(range(-1,2)), repeat=3):
                        if xDiff == 0 and yDiff == 0 and zDiff == 0:
                            continue
                        elif zCoord+zDiff < 0 or yCoord+yDiff < 0 or xCoord+xDiff < 0:
                            continue
                        elif zCoord+zDiff >= self.zMax or yCoord+yDiff >= self.yMax or xCoord+xDiff >= self.xMax:
                            continue
                        elif self.coordinates[zCoord+zDiff][yCoord+yDiff][xCoord+xDiff] == True:
                            self.neightboursCnt[zCoord][yCoord][xCoord] += 1

    def expandMap(self):

        zMinExtended = False
        zMaxExtended = False
        for xCoord in range(self.xMax):
            for yCoord in range(self.yMax):
                if (not zMinExtended) and (self.coordinates[0][yCoord][xCoord] == True):
                    self.coordinates = np.insert(self.coordinates, 0, 0, axis=0)
                    self.zMax += 1
                    zMinExtended = True
                if (not zMaxExtended) and (self.coordinates[self.zMax-1][yCoord][xCoord] == True):
                    self.coordinates = np.insert(self.coordinates, self.zMax, 0, axis=0)
                    self.zMax += 1
                    zMaxExtended = True

        yMinExtended = False
        yMaxExtended = False
        for xCoord in range(self.xMax):
            for zCoord in range(self.zMax):
                if (not yMinExtended) and (self.coordinates[zCoord][0][xCoord] == True):
                    self.coordinates = np.insert(self.coordinates, 0, 0, axis=1)
                    self.yMax += 1
                    yMinExtended = True
                if (not yMaxExtended) and (self.coordinates[zCoord][self.yMax-1][xCoord] == True):
                    self.coordinates = np.insert(self.coordinates, self.yMax, 0, axis=1)
                    self.yMax += 1
                    yMaxExtended = True

        xMinExtended = False
        xMaxExtended = False
        for zCoord in range(self.zMax):
            for yCoord in range(self.yMax):
                if (not xMinExtended) and (self.coordinates[zCoord][yCoord][0] == True):
                    self.coordinates = np.insert(self.coordinates, 0, 0, axis=2)
                    self.xMax += 1
                    xMinExtended = True
                if (not xMaxExtended) and (self.coordinates[zCoord][yCoord][self.xMax-1] == True):
                    self.coordinates = np.insert(self.coordinates, self.xMax, 0, axis=2)
                    self.xMax += 1
                    xMaxExtended = True

def fillMap(rows, Map3D):
    for yCoord, row in enumerate(rows):
        for xCoord, energyState in enumerate(row):
            if energyState == '.':
                Map3D.coordinates[0][yCoord][xCoord] = False
            else:
                Map3D.coordinates[0][yCoord][xCoord] = True

if __name__ == "__main__":
    #with open("test.txt") as file:
    with open("input.txt") as file:
        data = file.read()

    rows = data.split("\n")
    xMax = len(rows[0])
    yMax = len(rows)
    zMax = 1

    Map3D = Map(xMax, yMax, zMax)
    fillMap(rows, Map3D)

    Map3D.expandMap()

    for i in range(6):
        Map3D.countNeighbours()
        Map3D.updateState()
        Map3D.expandMap()
        #Map3D.printMap()

    Map3D.countActive()
    result = Map3D.activeTotal

    print("\nResult 17_01: " + str(result))
