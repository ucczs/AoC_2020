from collections import defaultdict

#with open("test.txt") as file:
with open("./input.txt") as file:
    data = file.read()

lines = data.split("\n")

result = 0
for line in lines:
    words = line.split()
    low, high = [int(x) for x in words[0].split("-")]
    requChar = words[1][0]
    password = words[-1]

    counts = defaultdict(int)
    for ch in password:
        counts[ch] += 1
    if low <= counts[requChar] <= high:
        result += 1

print(result)


