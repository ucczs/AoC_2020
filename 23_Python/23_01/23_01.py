import copy

def findSubstractor(numbers, currentIdx, currentNumber):
    subtractor = 1
    pickupIdx = 1
    while(pickupIdx < 4):
        substraction = currentNumber - subtractor
        if substraction <= 0:
            substraction = max(numbers) + substraction

        if numbers[(currentIdx + pickupIdx)%len(numbers)] == substraction:
            subtractor += 1
            pickupIdx = 1
        else:
            pickupIdx += 1

    return subtractor, substraction

#with open("test.txt") as file:
with open("input.txt") as file:
    data = file.read()

numbers = [ int(x) for x in data ]

currentIdx = 0

for count in range(100):
    currentNumber = numbers[currentIdx]

    substractor, targetNumber = findSubstractor(numbers, currentIdx, currentNumber)

    for k in range(len(numbers)):
        if numbers[k] == targetNumber:
            insertIdx = k
            break

    removedCup = [numbers[(currentIdx+1)%len(numbers)], numbers[(currentIdx+2)%len(numbers)], numbers[(currentIdx+3)%len(numbers)]]

    for i in range(1,4):
        numbers[(currentIdx+i)%len(numbers)] = 0

    for i in range(3):
        numbers.insert((insertIdx+1+i)%12, removedCup[i])

    numbers = list(filter(lambda a: a != 0, numbers))

    currentIdx = (numbers.index(currentNumber) + 1)%len(numbers)


result_startIdx = numbers.index(1) + 1

result = ""
for i in range(len(numbers)-1):
    result += str(numbers[(result_startIdx+i)%len(numbers)])

print(result)