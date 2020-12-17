
class ValidNumberRule:
    def __init__(self, name, min1, max1, min2, max2):
        self.name = name
        self.min1 = min1
        self.max1 = max1
        self.min2 = min2
        self.max2 = max2

def extractTickets(data):
    tickets = data.split("\n")[1:]

    tickets = [ticket.split(",") for ticket in tickets]
    for idx, ticket in enumerate(tickets):
        tickets[idx] = [int(x) for x in ticket]

    return tickets

def extractRules(data):
    ruleCollection = []

    for rule in data:
        name = rule[:rule.find(":")]
        range1 = rule[rule.find(":")+2:rule.find(" or ")]
        range2 = rule[rule.find(" or ")+4:]

        min1 = int(range1[0:range1.find("-")])
        max1 = int(range1[range1.find("-")+1:])
        min2 = int(range2[0:range2.find("-")])
        max2 = int(range2[range2.find("-")+1:])

        newRule = ValidNumberRule(name, min1, max1, min2, max2)
        ruleCollection.append(newRule)

    return ruleCollection

def getInvalidNumbers(tickets, ruleCollection):
    invalidNumbers = []

    for ticket in tickets:
        for ticketNumber in ticket:
            ticketNumberValid = False
            for rule in ruleCollection:
                if ((ticketNumber <= rule.max1 and ticketNumber >= rule.min1) or
                    (ticketNumber <= rule.max2 and ticketNumber >= rule.min2)):
                    ticketNumberValid = True
                    break

            if (not ticketNumberValid):
                invalidNumbers.append(ticketNumber)

    return invalidNumbers

if __name__ == "__main__":
    #with open("test.txt") as file:
    with open("input.txt") as file:
        data = file.read()

    sections = data.split("\n\n")

    myTicket = sections[1].split("\n")[1].split(",")
    myTicket = [int(x) for x in myTicket]

    tickets = extractTickets(sections[2])
    ruleCollection = extractRules(sections[0].split("\n"))

    invalidNumbers = getInvalidNumbers(tickets, ruleCollection)
    result = sum(invalidNumbers)

    print("\nResult 16_01: " + str(result))
