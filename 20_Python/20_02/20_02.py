
def print_tile(tile):
    for row in tile.rows:
        print(row)

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

def getOpposite(direction):
    if direction == UP:
        return DOWN
    elif direction == DOWN:
        return UP
    elif direction == LEFT:
        return RIGHT
    elif direction == RIGHT:
        return LEFT

class Tile:
    def __init__(self, tile_id=None):
        self.tile_id = tile_id
        self.rows = []
        self.borders = dict()
        self.size = None

    def getId(self):
        return self.tile_id

    def appendRow(self, line):
        if self.size is None:
            self.size = len(line)
        self.rows.append(line)
        if len(self.rows) == self.size:
            self.defineBorders()

    def getBorder(self, direction):
        return self.borders[direction]

    def getImage(self):
        for row in self.rows[1:-1]:
            yield row[1:-1]

    def rotateTile(self):
        matrix = dict()
        for y, line in enumerate(self.rows):
            for x, ch in enumerate(line):
                rx, ry = y, self.size - 1 - x
                matrix[(rx, ry)] = ch
        self.rearrangeMap(matrix)

    def flipTile(self):
        matrix = dict()
        for y, line in enumerate(self.rows):
            for x, ch in enumerate(line):
                fx, fy = self.size - 1 - x, y
                matrix[(fx, fy)] = ch
        self.rearrangeMap(matrix)

    def rearrangeMap(self, matrix):
        n = len(self.rows)
        self.rows = []
        for y in range(n):
            row = ""
            for x in range(n):
                row += matrix[(x, y)]
            self.rows.append(row)
        self.defineBorders()

    def align(self, border, direction):
        aligned = False
        for flipTile in range(2):
            if aligned:
                break
            if flipTile == 1:
                self.flipTile()
            for _ in range(4):
                self.rotateTile()
                current_border = self.getBorder(direction)
                if current_border == border:
                    aligned = True
                    break

    def defineBorders(self):
        self.borders[UP] = self.rows[0]
        self.borders[DOWN] = self.rows[-1]

        self.borders[LEFT] = ""
        self.borders[RIGHT] = ""
        for row in self.rows:
            self.borders[LEFT] += row[0]
            self.borders[RIGHT] += row[-1]

    def getPossibleBorders(self):
        for border in self.borders.values():
            yield border
            yield border[::-1]

class Map:
    def __init__(self, tiles):
        self.tiles = tiles
        self.sameBorders = self.findSameBorders()

    def findSameBorders(self):
        sameBorders = dict()
        for tile_id, tile in self.tiles.items():
            for border in tile.getPossibleBorders():
                if border not in sameBorders:
                    sameBorders[border] = set()
                sameBorders[border].add(tile_id)
        return sameBorders

    def getTileInDirection(self, current_tile, direction):
        tiles_row = []
        while True:
            tiles_row.append(current_tile)
            border = current_tile.getBorder(direction)
            valid_tiles = self.sameBorders[border].copy()
            valid_tiles.remove(current_tile.getId())
            if len(valid_tiles) == 1:
                tile_id = list(valid_tiles)[0]
                current_tile = self.tiles[tile_id]
                current_tile.align(border, getOpposite(direction))
            else:
                break
        return tiles_row

    def createMap(self):
        _, current_tile = list(self.tiles.items())[0]
        leftBorderTile = self.getTileInDirection(current_tile, LEFT)[-1]
        upLeftTile = self.getTileInDirection(leftBorderTile, UP)[-1]
        tilesMap = dict()
        yMax = 0
        xMax = 0
        for y, leftTile in enumerate(self.getTileInDirection(upLeftTile, DOWN)):
            yMax = max(yMax, y)
            for x, tile in enumerate(self.getTileInDirection(leftTile, RIGHT)):
                xMax = max(xMax, x)
                tilesMap[(x, y)] = tile
        return (xMax, yMax), tilesMap

def readTiles(data):
    tiles = dict()
    current_tile = None
    for line in data:
        if line == "":
            continue
        if line.startswith("Tile"):
            tile_number = int(line[5:-1])
            current_tile = Tile(tile_number)
            tiles[tile_number] = current_tile
        else:
            current_tile.appendRow(line)
    return tiles

def checkPatternAtLocation(image, x, y):
    size = image.size
    if x+19 >= size:
        return False
    if y+3 >= size:
        return False
    rows = image.rows
    if rows[y][x + 18] == "#" and \
       rows[y+1][x] == "#" and rows[y+1][x+5] == "#" and rows[y+1][x+6] == "#" and \
       rows[y+1][x+11] == "#" and rows[y+1][x+12] == "#" and \
       rows[y+1][x+17] == "#" and rows[y+1][x+18] == "#" and rows[y+1][x+19] == "#" and \
       rows[y+2][x+1] == "#" and rows[y+2][x+4] == "#" and rows[y+2][x+7] == "#" and \
       rows[y+2][x+10] == "#" and rows[y+2][x+13] == "#" and rows[y+2][x+16] == "#":
        return True
    else:
        return False

def findPattern(image):
    patternCnt = 0
    for y in range(image.size):
        for x in range(image.size):
            monster_here = checkPatternAtLocation(image, x, y)
            if monster_here:
                patternCnt += 1
    return patternCnt

def getNumberOfPixelsWithoutPattern(rows, patternCnt):
    pixelTotal = 0
    for row in rows:
        for pixel in row:
            if pixel == "#":
                pixelTotal += 1
    return pixelTotal - patternCnt * 15

def getPixelsWithoutPattern(imageSize, tilesMap):
    xMax, yMax = imageSize
    rows = []
    for y in range(yMax + 1):
        newRowElements = []
        for x in range(xMax + 1):
            tile = tilesMap[(x, y)]
            for n, row in enumerate(tile.getImage()):
                if n >= len(newRowElements):
                    newRowElements.append([])
                newRowElements[n].append(row)
        new_rows = []
        for chunks in newRowElements:
            new_rows.append("".join(chunks))
        rows.extend(new_rows)
    image = Tile(0)
    for row in rows:
        image.appendRow(row)
    patternCnt = 0
    for _ in range(2):
        if patternCnt > 0:
            break
        for _ in range(4):
            image.rotateTile()
            patternCnt = findPattern(image)
            if patternCnt > 0:
                break

    result = getNumberOfPixelsWithoutPattern(image.rows, patternCnt)
    return result

if __name__ == "__main__":
    #with open("test.txt") as file:
    with open("input.txt") as file:
        data = file.read()
    
    data = data.split("\n")

    tileCollection = readTiles(data)
    tilesMap = Map(tileCollection)

    imageDimensions, tilesMap = tilesMap.createMap()
    result = getPixelsWithoutPattern(imageDimensions, tilesMap)

    print("Result 20_02: " + str(result))
