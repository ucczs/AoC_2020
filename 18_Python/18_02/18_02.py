
def doCalculation(calc):
    result = 1

    if calc.find("+") >= 0:
        mutiplication = calc.split("*")
        for element in mutiplication:
            addition = element.split("+")
            addition = list(map(int, addition))
            add_sum = sum(addition)
            result *= add_sum
    
    else:
        calcMulti = calc.split("*")
        for element in calcMulti:
            result *= int(element)

    return result

#with open("test.txt") as file:
with open("input.txt") as file:
    data = file.read()

calculations = data.replace(" ", "").split("\n")

result_list = []

for calculation in calculations:

    while(calculation.find("(") >= 0):
        startIdx = None
        for idx, element in enumerate(calculation):
            if element == "(":
                insidePar = True
                startIdx = idx
            if element == ")":
                extractedCalc = calculation[startIdx:idx+1]
                resultInner = doCalculation(extractedCalc[1:-1])
                calculation = calculation.replace(extractedCalc, str(resultInner))
                break

    result_list.append(doCalculation(calculation))

print("Result 18_02: " + str(sum(result_list)))
