class InstructionClass:
  def __init__(self, action, offset):
    self.position = 0
    self.action = action
    self.offset = offset
    self.visited = False

class InstructionSetClass:
    def __init__(self):
        self.instructionSet = []
        self.numberElements = 0
        self.accumulator_val = 0

    def __addInstruction(self, instruction):
        instruction.position = self.numberElements
        self.instructionSet.append(instruction)
        self.numberElements += 1

    def __performInstruction(self, idx):
        if instructionCollection.instructionSet[idx].action == "nop":
            idx += 1
        elif instructionCollection.instructionSet[idx].action == "acc":
            self.accumulator_val += instructionCollection.instructionSet[idx].offset
            idx += 1
        elif instructionCollection.instructionSet[idx].action == "jmp":
            idx += instructionCollection.instructionSet[idx].offset
        else:
            print("Error in instructions")

        return idx

    def extractInstructionsInfoAndAddToSet(self, instructions):
        for instruction in instructions:
            action = instruction[:instruction.find(" ")]
            offset = int(instruction[instruction.find(" ")+1:])

            newInstruction = InstructionClass(action, offset)
            self.__addInstruction(newInstruction)

    def getAccValueWhenVisitedTwice(self):
        current_pos = 0

        while True:
            if instructionCollection.instructionSet[current_pos].visited:
                break
            elif current_pos > len(instructionCollection.instructionSet):
                print("Instruction set left.")
                exit()
            else:
                instructionCollection.instructionSet[current_pos].visited = True

            current_pos = self.__performInstruction(current_pos)

        return self.accumulator_val


if __name__ == "__main__":
    #with open("test.txt") as file:
    with open("input.txt") as file:
        data = file.read()

    instructions = data.split("\n")

    instructionCollection = InstructionSetClass()
    instructionCollection.extractInstructionsInfoAndAddToSet(instructions)
    accumulator = instructionCollection.getAccValueWhenVisitedTwice()

    print("\nResult 08_01: " + str(accumulator))
