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

# 30000000 works with this solution ok'ish, takes about a minute
while(current_pos < 30000000):

    if(prevNumberFirstTime):
        used_number = 0
    else:
        used_number = distancePrevNumber

    if used_number not in numbers or numbers[used_number] == None:
        prevNumberFirstTime = True
    else:
        distancePrevNumber = current_pos - numbers[used_number]
        prevNumberFirstTime = False
    numbers[used_number] = current_pos

    current_pos += 1

print("Result 15_02: " + str(used_number))
