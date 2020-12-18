
def doCalculation(calc):
    result = 0
    calcPlus = calc.split("+")

    for element in calcPlus:
        if element.find("*") >= 0:
            calcMultiplication = element.split("*")
            calcMultiplication = list(map(int, calcMultiplication))
            for idx, multi in enumerate(calcMultiplication):
                if idx == 0:
                    result += multi
                else:
                    result *= multi
        else:
            result += int(element)

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
                startIdx = idx
            if element == ")":
                extractedCalc = calculation[startIdx:idx+1]
                resultInner = doCalculation(extractedCalc[1:-1])
                calculation = calculation.replace(extractedCalc, str(resultInner))
                break

    result_list.append(doCalculation(calculation))

print("\nResult 18_01: " + str(sum(result_list)))
