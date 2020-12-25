
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
        if tile[0] == xPos and tile[1] == yPos:
            tile[2] = not tile[2]
            found = True

    if not found:
        tiles.append([xPos, yPos, True])

def countBlack(tiles):
    count = 0
    for tile in tiles:
        if tile[2] == True:
            count += 1

    return count

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

result = countBlack(tiles)

print(result)