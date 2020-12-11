
class CSeat:
  def __init__(self, xPos, yPos, posType, occupied):
    self.xPos = xPos
    self.yPos = yPos
    self.posType = posType
    self.occupied = occupied
    self.occupiedNeighbours = 0
    self.nextOccState = None

class CMap:
    def __init__(self):
        self.xPos_max = 0
        self.yPos_max = 0
        self.change_iterations = 0
        self.seats = None
        self.changed = True
        self.occupiedSeats = 0

    def initMap(self, x_max, y_max):
        self.xPos_max = x_max
        self.yPos_max = y_max
        self.seats = [[None for j in range(x_max)] for i in range(y_max)]


    def check_direction(self, shiftRange, xShiftMultiplier, yShiftMultiplier, seat):
        foundNeightbours = 0
        for shift in range(1, shiftRange):
            seat_to_check = self.seats[seat.yPos + shift * yShiftMultiplier][seat.xPos + shift * xShiftMultiplier]
            if seat_to_check.occupied == True:
                foundNeightbours += 1
                break
            elif seat_to_check.occupied == False:
                break

        return foundNeightbours

    def countNeightbours(self):
        for y in range(self.yPos_max):
            for x in range(self.xPos_max):
                seat = self.seats[y][x]
                if seat.posType == "seat":
                    seat.occupiedNeighbours = 0

                    seat.occupiedNeighbours += self.check_direction(seat.xPos+1              , -1,  0, seat) # looking left
                    seat.occupiedNeighbours += self.check_direction(self.xPos_max - seat.xPos, +1,  0, seat) # looking right
                    seat.occupiedNeighbours += self.check_direction(seat.yPos+1              ,  0, -1, seat) # looking up
                    seat.occupiedNeighbours += self.check_direction(self.yPos_max - seat.yPos,  0, +1, seat) # looking down

                    seat.occupiedNeighbours += self.check_direction(min(seat.xPos+1, seat.yPos+1)                            , -1, -1, seat) # looking left up
                    seat.occupiedNeighbours += self.check_direction(min(self.xPos_max - seat.xPos, seat.yPos+1)              , +1, -1, seat) # looking right up
                    seat.occupiedNeighbours += self.check_direction(min(seat.xPos+1, self.yPos_max - seat.yPos)              , -1, +1, seat) # looking left down
                    seat.occupiedNeighbours += self.check_direction(min(self.xPos_max - seat.xPos, self.yPos_max - seat.yPos), +1, +1, seat) # looking right down


    def switchNewstate(self):
        for y in range(self.yPos_max):
            for x in range(self.xPos_max):
                seat = self.seats[y][x]

                if seat.occupied is not seat.nextOccState:
                    self.changed = True
                seat.occupied = seat.nextOccState
                seat.nextOccState = None

    def performStep(self):
        self.changed = False
        self.countNeightbours()
    
        for y in range(self.yPos_max):
            for x in range(self.xPos_max):
                seat = self.seats[y][x]

                if seat.posType == "seat":
                    if seat.occupiedNeighbours >= 5:
                        seat.nextOccState = False
                    elif seat.occupiedNeighbours == 0:
                        seat.nextOccState = True
                    else:
                        seat.nextOccState = seat.occupied

        self.change_iterations += 1
        self.switchNewstate()

    def printMap(self):
        for y in range(self.yPos_max):
            for x in range(self.xPos_max):
                seat = self.seats[y][x]
                if seat.posType == "seat" and seat.occupied == True:
                    print('#', end='')
                elif seat.posType == "seat" and seat.occupied == False:
                    print('L', end='')
                else:
                    print('.', end='')

            print("")
        print("")

    def countOccSeats(self):
        for y in range(self.yPos_max):
            for x in range(self.xPos_max):
                seat = self.seats[y][x]

                if seat.occupied == True and seat.posType == "seat":
                    self.occupiedSeats += 1

def readInData():
    rows = data.split("\n")

    seatMap = CMap()
    seatMap.initMap(len(rows[0]), len(rows))

    for y_cnt, row in enumerate(rows):
        for x_cnt, place in enumerate(row):
            if place == "L":
                posType = "seat"
                occupied = False
            elif place == "#":
                posType = "seat"
                occupied = True
            else:
                posType = "floor"
                occupied = None

            newSeat = CSeat(x_cnt, y_cnt, posType, occupied)
            seatMap.seats[y_cnt][x_cnt] = newSeat

    return seatMap


if __name__ == "__main__":
    #with open("test.txt") as file:
    with open("input.txt") as file:
        data = file.read()

    seatMap = readInData()
    #seatMap.printMap()

    while(seatMap.changed):
        seatMap.performStep()
        #seatMap.printMap()

    seatMap.countOccSeats()
    #seatMap.printMap()

    print("Result 11_02: " + str(seatMap.occupiedSeats))