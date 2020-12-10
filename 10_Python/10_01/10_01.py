
#with open("test1.txt") as file:
#with open("test2.txt") as file:
with open("input.txt") as file:
    data = file.read()

adapters = list(map(int, data.split("\n")))

jolt_1_diff = []
jolt_3_diff = []

adapters.sort()

adapters.insert(0, 0)
adapters.append(max(adapters)+3)

for idx, adapter in enumerate(adapters):
    diff = 0
    if idx+1 >= len(adapters):
        continue
    else:
        diff = adapters[idx+1] - adapters[idx]
        if diff == 1:
            jolt_1_diff.append(idx)
        elif diff == 3:
            jolt_3_diff.append(idx)


result = len(jolt_1_diff) * len(jolt_3_diff)
print("\nResult 10_01: " + str(result))
