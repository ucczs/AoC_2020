import itertools

#previous_valid_numbers = 5
previous_valid_numbers = 25

#with open("test.txt") as file:
with open("input.txt") as file:
    data = file.read()

sum_to_find = 0

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
        sum_to_find = numberToCheck
        break


result_found = False
for idx, first_number in enumerate(numbers):
    sumOfPrevious = 0
    number_list =[]

    for idx2, number in enumerate(numbers[idx:]):
        sumOfPrevious += number
        number_list.append(number)
        if sumOfPrevious > sum_to_find:
            break
        elif sumOfPrevious == sum_to_find:
            result = min(number_list) + max(number_list)
            result_found = True

    if result_found:
        break

print("Result 09_02: " + str(result))
