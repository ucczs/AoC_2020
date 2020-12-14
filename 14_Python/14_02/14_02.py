import itertools

class MemoryCommand:
  def __init__(self, value, memPos, commandType):
    self.memPos = "{0:b}".format(memPos)
    self.memPos = self.memPos[::-1]
    self.memPos = '{:<036s}'.format(self.memPos)

    self.commandType = commandType

    if commandType == "mask":
        self.value = value
    else:
        self.value = "{0:b}".format(value)
        self.value = self.value[::-1]
        self.value = '{:<036s}'.format(self.value)

def getMask(maskIn):
    mask = [None for i in range(len(maskIn))]
    for idx, mask_element in enumerate(maskIn):
        if mask_element == "X":
            continue
        else:
            mask[-idx-1] = int(mask_element)

    return mask

def getMemoryAddresses(mask, addr):
    result_mem = []
    addresses = []
    for idx, mask_element in enumerate(mask):
        if mask_element == None:
            result_mem.append("X")
        elif mask_element == 0:
            result_mem.append(addr[idx])
        elif mask_element == 1:
            result_mem.append("1")
        else:
            print("Error in mem addr")

    count_x = result_mem.count("X")

    for combination in list(itertools.product("01", repeat=count_x)):
        result_mem_combination = ''.join(result_mem)
        for idx, element in enumerate(combination):
            result_mem_combination = result_mem_combination.replace("X", element, 1)
        addresses.append(int(result_mem_combination[::-1], 2))

    return addresses


def extractCommands(data):
    commands = []

    for commands_in in data:
        if commands_in.find("mask") >= 0:
            mask_in = commands_in.split(" ")[-1]
            mask = getMask(mask_in)
            newCommand = MemoryCommand(mask, -1, "mask")
        else:
            memPos = int(commands_in[4:commands_in.find("]")])
            value = int(commands_in[commands_in.find("=")+2:])
            newCommand = MemoryCommand(value, memPos, "write")

        commands.append(newCommand)

    return commands

def performCommands(commands):
    memory = {}
    mask = ""
    for command in commands:
        if command.commandType == "mask":
            mask = command.value
        else:
            mem_addresses = getMemoryAddresses(mask, command.memPos)
            for mem_address in mem_addresses:
                memory[mem_address] = command.value

    return memory

if __name__ == "__main__":
    #with open("test.txt") as file:
    with open("input.txt") as file:
        data = file.read().split("\n")

    commands = extractCommands(data)
    memory = performCommands(commands)

    result = 0
    for mem in memory.values():
        result += int(mem[::-1], 2)

    print("Result 14_02: " + str(result))