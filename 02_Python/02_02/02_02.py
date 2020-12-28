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

    if (password[low-1] == requChar) ^ (password[high-1] == requChar):
        result += 1

print(result)


