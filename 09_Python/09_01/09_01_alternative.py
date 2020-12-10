import itertools

#previous_valid_numbers = 5
previous_valid_numbers = 25

#with open("test.txt") as file:
with open("input.txt") as file:
    data = file.read()

numbers = list(map(int, data.split("\n")))

for idx_overall, numberToCheck in enumerate(numbers):
    valid_number = False
    if idx_overall < previous_valid_numbers:
        continue
    else:
        for a, b in itertools.combinations(numbers[idx_overall-previous_valid_numbers:idx_overall], 2):
            if a + b == numberToCheck:
                valid_number = True

    if valid_number is False:
        print("\nResult 09_01: " + str(numberToCheck))
        break
