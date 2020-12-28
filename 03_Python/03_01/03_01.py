#with open("test.txt") as file:
with open("./input.txt") as file:
    data = file.read().split("\n")

forest = []
for line in data:
    forest.append(list(line))

row = 0
column = 0
collision = 0

while row + 1 < len(forest):
    column += 3
    row += 1
    if forest[row][column % len(forest[0])] == '#':
        collision += 1

print(collision)
