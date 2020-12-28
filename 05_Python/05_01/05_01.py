
#with open("test.txt") as file:
with open("./input.txt") as file:
    data = file.read().split("\n")

result = 0

for line in data:
    
    row = 0
    rowHalfDiff = 64

    seat = 0
    seatHalfDiff = 4

    for char in line:
        if char == 'B':
            row += rowHalfDiff
        rowHalfDiff /= 2

        if char == 'R':
            seat += seatHalfDiff
            seatHalfDiff /= 2
        elif char == 'L':
            seatHalfDiff /= 2

        seat_id = int(row*8 + seat)

        result = max(result, seat_id)

print(result)