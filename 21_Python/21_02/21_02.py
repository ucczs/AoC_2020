class Allergen:
    def __init__(self, name, isPossiblyInside):
        self.name = name
        self.isPossiblyInside = [isPossiblyInside]
        self.defined = False

def getAllergen(allergeneName, allergensCollection):
    for allergene in allergensCollection:
        if allergene.name == allergeneName:
            return allergene

    return None

def removeIngredientFromAllergens(ingredient, allergensCollection):
    for allergen in allergensCollection:
        for possibleIn in allergen.isPossiblyInside:
            if ingredient in possibleIn:
                possibleIn.remove(ingredient)


def readInFoods(foods):
    allergensCollection = []
    unknownIngredientCollection = []

    for food in foods:
        ingredients = food[0:food.find("(")-1].split(" ")
        allergens = food[food.find("contains")+9:].replace(",", "").replace(")", "").split(" ")
        
        unknownIngredientCollection += ingredients
        for allergenName in allergens:
            allergen = getAllergen(allergenName, allergensCollection)

            if allergen == None:
                newAllergen = Allergen(allergenName, ingredients)
                allergensCollection.append(newAllergen)
            else:
                allergen.isPossiblyInside.append(ingredients)

    unknownIngredientCollection = list(set(unknownIngredientCollection))

    return allergensCollection, unknownIngredientCollection


#with open("test.txt") as file:
with open("input.txt") as file:
    data = file.read()

foods = data.split("\n")

allergensCollection = []
unknownIngredientCollection = []

allergensCollection, unknownIngredientCollection = readInFoods(foods)
changes = True

while(changes):
    changes = False
    for allergen in allergensCollection:
        if not allergen.defined:
            candidates = []
            for ingredient in allergen.isPossiblyInside[0]:
                foundInAllFood = True
                for foodToCheck in allergen.isPossiblyInside[1:]:
                    if ingredient not in foodToCheck:
                        foundInAllFood = False

                if foundInAllFood:
                    candidates.append(ingredient)

            if len(candidates) == 1:
                changes = True
                removeIngredientFromAllergens(candidates[0], allergensCollection)
                unknownIngredientCollection.remove(candidates[0])
                allergen.defined = True
                allergen.isPossiblyInside = candidates[0]

result = 0
for unknowIngredient in unknownIngredientCollection:
    result += data.count(unknowIngredient + " ")

allergenDict = {}
for allergen in allergensCollection:
    allergenDict[allergen.name] = allergen.isPossiblyInside

result = ""
for key, value in sorted(allergenDict.items()):
    result += (value + ",")

print("Result 21_02: " + str(result[:-1]))