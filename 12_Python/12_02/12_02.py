class CShip:
    def __init__(self):
        self.xPos = 0
        self.yPos = 0
        self.xPos_wayPoint = 10
        self.yPos_wayPoint = 1

    def rotateShip(self, degree):
        xPos_WP_old = self.xPos_wayPoint
        yPos_WP_old = self.yPos_wayPoint

        if degree == 90:
            self.xPos_wayPoint = yPos_WP_old
            self.yPos_wayPoint = -xPos_WP_old
        elif degree == 180:
            self.xPos_wayPoint = -xPos_WP_old
            self.yPos_wayPoint = -yPos_WP_old
        elif degree == 270:
            self.xPos_wayPoint = -yPos_WP_old
            self.yPos_wayPoint = xPos_WP_old

    def moveForward(self, command, distance):
        if command == "F":
            self.xPos += (self.xPos_wayPoint * distance)
            self.yPos += (self.yPos_wayPoint * distance)

        elif command == "E":
            self.xPos_wayPoint += distance
        elif command == "W":
            self.xPos_wayPoint -= distance
        elif command == "S":
            self.yPos_wayPoint -= distance
        elif command == "N":
            self.yPos_wayPoint += distance


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
    print("\nResult 12_02: " + str(result))
