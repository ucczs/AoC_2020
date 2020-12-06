#with open("test.txt") as file:
with open("input.txt") as file:
    data = file.read()

inputList = data.split("\n\n")

countList = []

for group in inputList:
    answerList = []
    allAnswerCount = 0
    for element in group:
        if element == "\n":
            continue
        elif element not in answerList:
            answerList.append(element)

    members = group.split("\n")
    for answer in answerList:
        allAnswered = True
        for member in members:
            if answer not in member:
                allAnswered = False

        if allAnswered:
            allAnswerCount += 1

    countList.append(allAnswerCount)

print(countList)
result = sum(countList)
print(result)
