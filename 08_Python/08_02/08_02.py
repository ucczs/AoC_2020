import copy

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
        self.nopInstructionsIdx = []
        self.jmpInstructionsIdx = []

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

    def __getNopJmpInstructionsIdx(self):
        for instruction in self.instructionSet:
            if instruction.action == "nop":
                self.nopInstructionsIdx.append(instruction.position)
            elif instruction.action == "jmp":
                self.jmpInstructionsIdx.append(instruction.position)

    def __changeOneInstruction(self, idx, newInstruction):
        instructionSet_modified = copy.deepcopy(self.instructionSet)
        instructionSet_modified[idx].action = newInstruction

        return instructionSet_modified


    def __lastInstructionReached(self, instructionSet_modified):
        self.accumulator_val = 0

        current_pos = 0
        return_val = False

        while True:
            if instructionSet_modified[current_pos].visited == True:
                break
            else:
                instructionSet_modified[current_pos].visited = True

            if instructionSet_modified[current_pos].action == "nop":
                current_pos += 1
            elif instructionSet_modified[current_pos].action == "acc":
                self.accumulator_val += instructionSet_modified[current_pos].offset
                current_pos += 1
            elif instructionSet_modified[current_pos].action == "jmp":
                current_pos += instructionSet_modified[current_pos].offset
            else:
                print("Error in instructions")

            if instructionSet_modified[-1].visited == True:
                return_val = True
                break

        return return_val


    def getAccWhenReachingLastInstruction(self):
        self.__getNopJmpInstructionsIdx()

        for idx in self.nopInstructionsIdx:
            instructionSet_modified = self.__changeOneInstruction(idx, "jmp")
            if( self.__lastInstructionReached(instructionSet_modified) ):
                return self.accumulator_val

        for idx in self.jmpInstructionsIdx:
            instructionSet_modified = self.__changeOneInstruction(idx, "nop")
            if( self.__lastInstructionReached(instructionSet_modified) ):
                return self.accumulator_val

if __name__ == "__main__":
    #with open("test.txt") as file:
    with open("input.txt") as file:
        data = file.read()

    instructions = data.split("\n")

    instructionCollection = InstructionSetClass()
    instructionCollection.extractInstructionsInfoAndAddToSet(instructions)

    accumulator = instructionCollection.getAccWhenReachingLastInstruction()

    print("Result 08_01: " + str(accumulator))
