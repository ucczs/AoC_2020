#with open("test.txt") as file:
with open("input.txt") as file:
    data = file.read()

inputList = data.split("\n\n")

countList = []

for group in inputList:
    answerList = []
    count = 0
    for element in group:
        if element == "\n":
            continue
        elif element not in answerList:
            count += 1
            answerList.append(element)

    countList.append(len(answerList))

print(countList)
result = sum(countList)
print(result)
