import itertools

class Rule:
    def __init__(self, letter, ruleReference, number):
        self.letter = letter
        self.ruleReference = ruleReference
        self.number = number

def readInRules(rules):
    rulesCollection = []

    for rule in rules:
        number = int(rule[:rule.find(":")])

        if rule.find("\"") > 0:
            reference = None
            letter = rule[rule.find("\"")+1:-1]
        else:
            letter = None
            reference = []
            if rule.find("|") < 0:
                ruleSection = rule[rule.find(":")+2:].split(" ")
                ruleSection = [ int(x) for x in ruleSection ]
                reference.append(ruleSection)
            else:
                ruleSection1 = rule[rule.find(":")+2:rule.find("|")-1].split(" ")
                ruleSection1 = [ int(x) for x in ruleSection1 ]
                reference.append(ruleSection1)

                ruleSection2 = rule[rule.find("|")+2:].split(" ")
                ruleSection2 = [ int(x) for x in ruleSection2 ]
                reference.append(ruleSection2)

        newRule = Rule(letter, reference, number)
        rulesCollection.append(newRule)

    return rulesCollection

def getRuleNumberX(rules, x):
    return_rule = None

    for rule in rules:
        if rule.number == x:
            return_rule = rule
            break

    return return_rule

def getNumbersOfLeaveRule(rules):
    position = []
    for rule in rules:
        if rule.ruleReference == None:
            position.append(rule.number)

    return position[0], position[1]

def getAllSubCombinations(rule, numb1, numb2, allRules):
    allCombinations = []
    if rule.ruleReference == None:
        allCombinations = rule.number
    else:
        for ruleCluster in rule.ruleReference:
            elementCombinations = []
            for element in ruleCluster:
                if element != numb1 and element != numb2:
                    thisRule = getRuleNumberX(allRules, element)
                    elementCombinations.append(getAllSubCombinations(thisRule, numb1, numb2, allRules))

                else:
                    elementCombinations.append([element])

            allCombinations.append(elementCombinations)

    return allCombinations

def getAllRuleCombinations(rulesCollection):
    ruleZero = getRuleNumberX(rulesCollection, 0)
    numb1, numb2 = getNumbersOfLeaveRule(rulesCollection)

    allCombinations = getAllSubCombinations(ruleZero, numb1, numb2, rulesCollection)
    print(allCombinations)

    return allCombinations

def checkRules(subRules, rulesCollection, message, number1, number2):
    messagePartChecked = 0
    for subRule in subRules:
        result = checkSingleRule(subRule, rulesCollection, message[messagePartChecked:], number1, number2)
        if result == -1:
            return -1
        else:
            messagePartChecked += result
    
    return messagePartChecked

def checkSingleRule(rulesCombinations, rulesCollection, message, number1, number2):
    if message == "":
        return -1

    for subRule in rulesCombinations:
        if subRule == number1:
            rule = getRuleNumberX(rulesCollection, number1)
            if rule.letter == message[0]:
                return 1
            else:
                return -1

        elif subRule == number2:
            rule = getRuleNumberX(rulesCollection, number2)
            if rule.letter == message[0]:
                return 1
            else:
                return -1

        elif isinstance(subRule, list):
            result = checkRules(subRule, rulesCollection, message, number1, number2)
            if result != -1:
                return result
            else:
                continue

    return -1

#with open("test.txt") as file:
with open("input.txt") as file:
    data = file.read()

sections = data.split("\n\n")
rules = sections[0].split("\n")
messages = sections[1].split("\n")

rulesCollection = readInRules(rules)
numb1, numb2 = getNumbersOfLeaveRule(rulesCollection)
ruleCombinations = getAllRuleCombinations(rulesCollection)

validMessages = 0
for message in messages:
    if(checkRules(ruleCombinations[0], rulesCollection, message, numb1, numb2) == len(message)):
        validMessages += 1

print(validMessages)