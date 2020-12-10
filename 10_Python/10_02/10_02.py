
# ugly hard coded part
# returns the numbers of the combinations which are possible
# besides the standard combination (leave no out)
def getNumbOfCombinations(diff_set):
    if len(diff_set) <= 3:
        return 0
    elif len(diff_set) == 4:
        return 1
    elif len(diff_set) == 5:
        if ( sum(diff_set) == 9):
            return 3
        else:
            return 2
    elif len(diff_set) == 6:
        if(diff_set[1] == 2 or diff_set[4] == 2):
            return 5
        elif(diff_set[2] == 2):
            return 4
        else:
            return 6
    elif len(diff_set) == 7:
        return 12
    else:
        print("no of combinations not found")
        return -1


#with open("test1.txt") as file:
#with open("test2.txt") as file:
with open("input.txt") as file:
    data = file.read()

adapters = list(map(int, data.split("\n")))
adapters.sort()

adapters.insert(0, 0)
adapters.append(max(adapters)+3)

# handle the beginning as there were a diff of 3 before
diff_list = [3]
for idx, adapter in enumerate(adapters):
    if idx+1 < len(adapters):
        diff_list.append(adapters[idx+1] - adapters[idx])

combination_list = []

for idx, diff in enumerate(diff_list):
    if diff == 3 or diff == 2:
        combination_found = False
        idx_moving = idx
        diff_set = [3]

        while(combination_found == False):
            idx_moving += 1
            
            if idx_moving >= len(diff_list):
                combination_found = True
            else:
                diff_set.append(diff_list[idx_moving])

            if diff_set[-1] == 3 or diff_set[-1] == 2:
                combination_list.append(getNumbOfCombinations(diff_set)+1)
                diff_set = [3]
                combination_found = True

result = 1
for combi in combination_list:
    result *= combi

print("Result 10_02: " + str(result))
