class MemoryCommand:
  def __init__(self, value, memPos, commandType):
    self.memPos = memPos
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

def getCommandList(data):
    memory_commands = []

    for commands_in in data:
        if commands_in.find("mask") >= 0:
            mask_in = commands_in.split(" ")[-1]
            mask = getMask(mask_in)
            newCommand = MemoryCommand(mask, -1, "mask")
        else:
            memPos = int(commands_in[4:commands_in.find("]")])
            value = int(commands_in[commands_in.find("=")+2:])
            newCommand = MemoryCommand(value, memPos, "write")

        memory_commands.append(newCommand)

    return memory_commands

def performCommands(commands):
    memory = {}
    for command in commands:
        result_mem = []
        if command.commandType == "mask":
            mask = command.value
        else:
            for idx, mask_element in enumerate(mask):
                if mask_element == None:
                    result_mem.append(command.value[idx])
                elif mask_element == 0:
                    result_mem.append("0")
                elif mask_element == 1:
                    result_mem.append("1")
                else:
                    print("Error in command")
            memory[command.memPos] = result_mem

    return memory


if __name__ == "__main__":
    #with open("test.txt") as file:
    with open("input.txt") as file:
        data = file.read().split("\n")

    commands = getCommandList(data)
    memory = performCommands(commands)

    result = 0
    for mem in memory.values():
        result += int(''.join(mem[::-1]), 2)

    print("\nResult 14_01: " + str(result))
