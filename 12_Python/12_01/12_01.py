from enum import Enum

class Direction(Enum):
    north   = 0
    east    = 1
    south   = 2
    west    = 3

class CShip:
    def __init__(self):
        self.current_direction = Direction.east
        self.xPos = 0
        self.yPos = 0

    def rotateShip(self, degree):
        self.current_direction = Direction((self.current_direction.value + int(degree / 90)) % 4)

    def moveForward(self, command, distance):
        moveDirection = ""

        if command == "F":
            moveDirection = ship.current_direction
        else:
            moveDirection = command

        if moveDirection == "E" or moveDirection == Direction.east:
            ship.xPos += distance
        elif moveDirection == "W" or moveDirection == Direction.west:
            ship.xPos -= distance
        elif moveDirection == "S" or moveDirection == Direction.south:
            ship.yPos -= distance
        elif moveDirection == "N" or moveDirection == Direction.north:
            ship.yPos += distance


if __name__ == "__main__":
    #with open("test.txt") as file:
    with open("input.txt") as file:
        commands = file.read().split("\n")
        ship = CShip()

    for command in commands:
        distance = int(command[1:])
        direction = command[0]
        rotation = False

        if direction == "L":
            ship.rotateShip(360 - distance)
        elif direction == "R":
            ship.rotateShip(distance)
        else:
            ship.moveForward(direction, distance)

    result = abs(ship.xPos) + abs(ship.yPos)
    print("\nResult 12_01: " + str(result))

