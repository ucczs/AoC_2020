def printTile(tile):
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
        solution = dict()
        yMax = 0
        xMax = 0
        for y, leftTile in enumerate(self.getTileInDirection(upLeftTile, DOWN)):
            yMax = max(yMax, y)
            for x, tile in enumerate(self.getTileInDirection(leftTile, RIGHT)):
                xMax = max(xMax, x)
                solution[(x, y)] = tile
        return (xMax, yMax), solution

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

def getCornerIDMultiplication(image_size, solution):
    xMax, yMax = image_size

    upLeftTileID = solution[(0, 0)].getId()
    upRightCornerID = solution[(0, xMax)].getId()
    bottomLeftTileID = solution[(yMax, 0)].getId()
    bottomRightTileID = solution[(yMax, xMax)].getId()

    result = upLeftTileID * upRightCornerID * bottomLeftTileID * bottomRightTileID

    return result

if __name__ == "__main__":
    #with open("test.txt") as file:
    with open("input.txt") as file:
        data = file.read()
    
    data = data.split("\n")

    tileCollection = readTiles(data)
    tilesMap = Map(tileCollection)

    imageDimensions, tilesMap = tilesMap.createMap()
    result = getCornerIDMultiplication(imageDimensions, tilesMap)
    print("\nResult 20_01: " + str(result))
