#with open("test.txt") as file:
with open("input.txt") as file:
    data = file.read()

lines = data.split("\n")

earliest_time = int(lines[0])

buses = lines[1].split(",")
found_time = 0
used_bus = 0
for timestamp in range(earliest_time, earliest_time+59):
    for bus in buses:
        if bus == 'x':
            continue
        else:
            if timestamp % int(bus) == 0:
                found_time = timestamp
                used_bus = int(bus)
                break
    if found_time > 0:
        break

result = (timestamp - earliest_time) * used_bus
print("\nResult 13_01: " + str(result))
