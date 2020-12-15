#with open("test.txt") as file:
with open("input.txt") as file:
    data = file.read().split(",")

numbers = {}

for idx, starting_number in enumerate(data):
    numbers[int(starting_number)] = idx

current_pos = int(len(data))
last_number = int(data[-1])

prevNumberFirstTime = True
distancePrevNumber = 0

# 30000000 works with this solution ok'ish, takes about half a minute
while(current_pos < 30000000):

    if(prevNumberFirstTime):
        found_number = 0
    else:
        found_number = distancePrevNumber

    if found_number not in numbers:
        prevNumberFirstTime = True
    else:
        distancePrevNumber = current_pos - numbers[found_number]
        prevNumberFirstTime = False
    numbers[found_number] = current_pos

    current_pos += 1

print("Result 15_02: " + str(found_number))
