import lark

#with open("test.txt") as file:
with open("input.txt") as file:
    data = file.read()

sections = data.split("\n\n")
rules = sections[0]
messages = sections[1].split("\n")

rules = rules.replace("8: 42", "8: 42 | 42 8")
rules = rules.replace("11: 42 31", "11: 42 31 | 42 11 31")

translatedRules = rules
for i in range(10):
    translatedRules = translatedRules.replace(str(i), chr(97+i))

parser = lark.Lark(translatedRules, start="a")

count = 0
for msg in messages:
    try:
        parser.parse(msg)
        count += 1
    except:
        pass

print(count)