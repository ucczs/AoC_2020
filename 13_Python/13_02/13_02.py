from functools import reduce

# chinese remainder theorem
# example (test2.txt): 17,x,13,19
# x = 0      (mod 17)
# x = 13 - 2 (mod 13)
# x = 19 - 3 (mod 19)
# --> x = ID - idx (mod ID)

# Source: https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
# x = a (mod n)
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


if __name__ == '__main__':
    #with open("test6.txt") as file:
    with open("input.txt") as file:
        data = file.read()

    buses_input = data.split(",")

    buses = []
    for idx, bus_input in enumerate(buses_input):
        if bus_input == "x":
            continue
        else:
            buses.append((int(bus_input), idx))

    n = []
    a = []
    for bus in buses:
        n.append(bus[0])

        if bus[1] == 0:
            a.append(0)
        else:
            a.append(bus[0] - bus[1])

    print("Result 13_02: " + str(chinese_remainder(n, a)))