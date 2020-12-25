
class Tile:
    def __init__(self, xPos, yPos, blackColor):
        self.xPos = xPos
        self.yPos = yPos
        self.blackColor = blackColor
        self.blackNeightboursCnt = None
        self.nextBlackColor = None

    def switchColor(self):
        if self.nextBlackColor != None:
            self.blackColor = self.nextBlackColor
            self.nextBlackColor = None

def getNextCommand(line):
    if line[0] == "e":
        x = 2
        y = 0
        line = line[1:]
    elif line[:2] == "se":
        x = 1
        y = -1
        line = line[2:]
    elif line[:2] == "sw":
        x = -1
        y = -1
        line = line[2:]
    elif line[0] == "w":
        x = -2
        y = 0
        line = line[1:]
    elif line[:2] == "nw":
        x = -1
        y = 1
        line = line[2:]
    elif line[:2] == "ne":
        x = 1
        y = 1
        line = line[2:]

    return x, y, line

def flipTileAtPos(tiles, xPos, yPos):
    found = False
    for tile in tiles:
        if tile.xPos == xPos and tile.yPos == yPos:
            tile.blackColor = not tile.blackColor
            found = True

    if not found:
        newTile = Tile(xPos, yPos, True)
        tiles.append(newTile)

def countBlack(tiles):
    count = 0
    for tile in tiles:
        if tile.blackColor == True:
            count += 1

    return count

def isPosBlack(tiles, xPos, yPos):
    for tile in tiles:
        if tile.xPos == xPos and tile.yPos == yPos:
            if tile.blackColor == True:
                return True
    return False

def countNeighbours(tiles):
    validNeightbourCombination = [(2,0), (-2,0), (1,1), (-1,1), (1,-1), (-1,-1)]
    for tile in tiles:
        neightbourCnt = 0
        for neightbour in validNeightbourCombination:
            xPosCheck = tile.xPos + neightbour[0]
            yPosCheck = tile.yPos + neightbour[1]
            if isPosBlack(tiles, xPosCheck, yPosCheck):
                neightbourCnt += 1

        tile.blackNeightboursCnt = neightbourCnt

def performStep(tiles):
    for tile in tiles:
        if tile.blackColor == True:
            if tile.blackNeightboursCnt == 0 or tile.blackNeightboursCnt > 2:
                tile.nextBlackColor = False
            else:
                tile.nextBlackColor = True

        if tile.blackColor == False:
            if tile.blackNeightboursCnt == 2:
                tile.nextBlackColor = True
            else:
                tile.nextBlackColor = False

    for tile in tiles:
        tile.switchColor()

def creatNeightbours(tiles):
    validNeightbourCombination = [(2,0), (-2,0), (1,1), (-1,1), (1,-1), (-1,-1)]
    for tile in tiles:
        if tile.blackColor == True:
            for neightbour in validNeightbourCombination:
                neighbourExists = False
                for tile_neighbour in tiles:
                    if (tile.xPos + neightbour[0] == tile_neighbour.xPos and
                        tile.yPos + neightbour[1] == tile_neighbour.yPos):
                        neighbourExists = True
                        break

                if neighbourExists == False:
                    newTile = Tile(tile.xPos + neightbour[0], tile.yPos + neightbour[1], False)
                    tiles.append(newTile)

    return tiles

def removeWhiteOnlyTiles(tiles):
    validNeightbourCombination = [(2,0), (-2,0), (1,1), (-1,1), (1,-1), (-1,-1)]

    for tile in tiles:
        blackFound = False
        if tile.blackColor == False:
            for neightbour in validNeightbourCombination:
                for tile_neighbour in tiles:
                    if (tile.xPos + neightbour[0] == tile_neighbour.xPos and
                        tile.yPos + neightbour[1] == tile_neighbour.yPos) and tile_neighbour.blackColor == True:
                        blackFound = True
                        break

            if blackFound == False:
                tiles.remove(tile)

#with open("test.txt") as file:
with open("input.txt") as file:
    data = file.read()

instructions = data.split("\n")

tiles = []

for instruction in instructions:
    line = instruction
    xPos = 0
    yPos = 0
    while(line):
        x, y, line = getNextCommand(line)
        xPos += x
        yPos += y

    flipTileAtPos(tiles, xPos, yPos)

print(countBlack(tiles))

for i in range(100):
    tiles = creatNeightbours(tiles)
    countNeighbours(tiles)
    removeWhiteOnlyTiles(tiles)
    performStep(tiles)
    print(str(i+1) + ": " + str(countBlack(tiles)))

result = countBlack(tiles)

print(result)