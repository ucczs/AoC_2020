class Cup:
    def __init__(self, value):
        self.value = value
        self.next = None

def printCurrentOrder(startingCup):
    startVal = startingCup.value
    currentCup = startingCup
    print(startVal, end=" ")
    currentCup = currentCup.next

    while(currentCup.value != startVal):
        print(currentCup.value, end=" ")
        currentCup = currentCup.next

    print()

TOTAL_NUMBERS = 1000000

#with open("test.txt") as file:
with open("input.txt") as file:
    data = file.read()

cups = {}
for number in range(1, TOTAL_NUMBERS + 1):
    cups[number] = Cup(number)

for idx in range(TOTAL_NUMBERS + 1):
    if idx < len(data) - 1:
        cups[int(data[idx])].next = cups[int(data[idx+1])]
    elif idx == len(data)-1:
        cups[int(data[idx])].next = cups[len(data)+1]
    elif idx > len(data) and idx < TOTAL_NUMBERS:
        cups[idx].next = cups[idx+1]
    elif idx == TOTAL_NUMBERS:
        cups[idx].next = cups[int(data[0])]

currentCup = cups[int(data[0])]

for i in range(10000000):
    moveOne = currentCup.next
    moveThree = currentCup.next.next.next

    moveValues = [moveOne.value, moveOne.next.value, moveThree.value]
    target = currentCup.value - 1 if currentCup.value > 1 else TOTAL_NUMBERS
    while(target in moveValues):
        target -= 1
        if target == 0:
            target = TOTAL_NUMBERS

    currentCup.next = moveThree.next
    moveThree.next = cups[target].next
    cups[target].next = moveOne

    currentCup = currentCup.next

result = cups[1].next.value * cups[1].next.next.value

print(result)
