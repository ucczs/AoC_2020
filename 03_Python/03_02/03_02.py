#with open("test.txt") as file:
with open("./input.txt") as file:
    data = file.read().split("\n")

forest = []
for line in data:
    forest.append(list(line))

slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

result = 1
for deltaColumn, deltaRow in slopes:
    row = 0
    column = 0
    collision = 0

    while row + 1 < len(forest):
        column += deltaColumn
        row += deltaRow
        if forest[row][column % len(forest[0])] == '#':
            collision += 1

    result *= collision


print(result)
