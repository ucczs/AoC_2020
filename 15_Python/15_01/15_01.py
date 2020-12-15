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

while(current_pos < 2020):

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

print("\nResult 15_01: " + str(used_number))
