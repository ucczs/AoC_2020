import re

#with open("test.txt") as file:
with open("./input.txt") as file:
    data = file.read().split("\n")

result = 0
passport = {}

for line in data:
    if not line:
        valid = True

        if 'byr' in passport:
            byrChar = passport['byr']
            byr = int(byrChar)
            if len(byrChar) != 4 or not(1920 <= byr <= 2002):
                valid = False
        else:
            valid = False

        if 'iyr' not in passport or not (2010 <= int(passport['iyr']) <= 2020):
            valid = False

        if 'eyr' not in passport or not (2020 <= int(passport['eyr']) <= 2030):
            valid = False

        if 'hgt' in passport:
            hgtChar = passport['hgt']
            if len(hgtChar) > 2:
                if not re.findall(r'[a-zA-Z]', hgtChar[:-2]):
                    hgt = int(hgtChar[:-2])
                    if hgtChar.endswith("in"):
                        if not 59 <= hgt <= 76:
                            valid = False
                    elif hgtChar.endswith("cm"):
                        if not 150 <= hgt <= 193:
                            valid = False
                else:
                    valid = False
            else:
                valid = False
        else:
            valid = False

        if 'hcl' in passport:
            if passport['hcl'][0] != '#':
                valid = False
            elif not re.findall(r'[0-9a-f]{6}', passport['hcl']):
                valid = False
        else:
            valid = False

        if 'ecl' not in passport or passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            valid = False

        if 'pid' in passport:
            if len(passport['pid']) != 9 or not re.findall(r'[0-9]{9}', passport['pid']):
                valid = False
        else:
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