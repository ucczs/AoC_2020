class BagType:
  def __init__(self, color, contains):
    self.color = color
    self.contains = contains
    self.hasGold = False


def ColorHasGold(color_name, bag_collection):
    for bag in bag_collection:
        if bag.hasGold == True and bag.color == color_name:
            return True

    return False

def getNumbers(bags, colorName):
    sum_bags = 0
    for bag in bags:
        if bag.color == colorName:
            if bag.contains == []:
                sum_bags = 0
            else:
                for insideColor in bag.contains:
                    sum_bags += getNumbers(bags, insideColor[0]) * insideColor[1] + insideColor[1]


    return sum_bags


g_bagCollection = []
bags = []

#with open("test2.txt") as file:
with open("input.txt") as file:
    data = file.read()

rules = data.replace("bags", "bag").split("\n")

for rule in rules:
    idx_bigBag = rule.find("contain")

    bigBag = rule[:idx_bigBag-5]

    insideBags = []


    if rule.find("no other bag") >= 0:
        newBag = BagType(bigBag, [])
        g_bagCollection.append(newBag)
    else:
        rule = rule[idx_bigBag+8:]

        while True:
            number = rule[:rule.find(" ")]

            if(rule.find(",") >= 0):
                insideBag = rule[rule.find(" ")+1:rule.find(",")-4]
                rule = rule[rule.find(",")+2:]
                insideBags.append([insideBag, int(number)])
            else:
                insideBag = rule[rule.find(" ")+1:rule.find(".")-4]
                insideBags.append([insideBag, int(number)])
                break

        newBag = BagType(bigBag, insideBags)
        g_bagCollection.append(newBag)

smth_changed = True
while( smth_changed ):
    smth_changed = False
    for bag in g_bagCollection:
        for insideBag in bag.contains:
            if insideBag[0] == "shiny gold" and bag.hasGold == False:
                bag.hasGold = True
                smth_changed = True
            elif ColorHasGold(insideBag[0], g_bagCollection) and bag.hasGold == False:
                bag.hasGold = True
                smth_changed = True

result = 0

for bag in g_bagCollection:
    if bag.hasGold == True:
        result += 1

result = getNumbers(g_bagCollection, "shiny gold")

print("Result 07_02: " + str(result))













