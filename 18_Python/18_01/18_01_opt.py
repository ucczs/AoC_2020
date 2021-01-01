
class Number:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Number(self.number + other.number)

    def __sub__(self, other):
        return Number(self.number * other.number)

    def __str__(self):
        return str(self.number)

def getLineResult(line):
    evalString = ""
    inNumber = False

    for ch in line:
        if ch in "01234556789" and not inNumber:
            evalString += "Number(" + ch
            inNumber = True
        elif (ch == " " or ch == ")") and inNumber:
            evalString += ")" + ch
            inNumber = False
        else:
            evalString += ch

    if inNumber:
        evalString += ")"

    evalString = evalString.replace("*", "-")

    return eval(evalString).number

#with open("test.txt") as file:
with open("input.txt") as file:
    data = file.read().split("\n")

result = 0
for line in data:
    result += getLineResult(line)

print(result)