
def transform(subjectNumber, loopCnt):
    devider = 20201227
    value = subjectNumber

    for _ in range(loopCnt-1):
        value = value * subjectNumber
        value = value % devider
        #print(value)

    return value


def performTransformStep(subjectNumber, currentValue):
    devider = 20201227
    currentValue = (currentValue * subjectNumber) % devider

    return currentValue


def findLoopCount(publicKey):
    loopCnt = 1
    subjectNumber = 7
    currentVal = subjectNumber
    while(True):
        currentVal = performTransformStep(subjectNumber, currentVal)
        if currentVal == publicKey:
            loopCountDoor = loopCnt+1
            break
        else:
            loopCnt += 1

    return loopCountDoor

#with open("test.txt") as file:
with open("input.txt") as file:
    data = file.read()

publicKeyDoor, publicKeyCard = data.split("\n")

publicKeyDoor = int(publicKeyDoor)
publicKeyCard = int(publicKeyCard)

loopCountDoor = findLoopCount(publicKeyDoor)
loopCountCard = findLoopCount(publicKeyCard)

result1 = transform(publicKeyCard, loopCountDoor)
result2 = transform(publicKeyDoor, loopCountCard)

if result1 != result2:
    print("Error, results are not the same!")
else:
    print(result2)

print()
