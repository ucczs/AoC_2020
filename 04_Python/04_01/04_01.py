#with open("test.txt") as file:
with open("./input.txt") as file:
    data = file.read().split("\n")

result = 0
passport = {}

for line in data:
    if not line:
        valid = True
        for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            if field not in passport:
                valid = False
        
        if valid:
            result += 1
        passport = {}
    else:
        words = line.split()
        for word in words:
            key, value = word.split(":")
            passport[key] = value

print(result)