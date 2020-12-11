
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
        self.seats = []
        self.changed = True
        self.occupiedSeats = 0

    def getPos(self, xPosDes, yPosDes):
        for seat in self.seats:
            if seat.xPos == xPosDes and seat.yPos == yPosDes:
                return seat
        return None

    def setMaxValues(self):
        for seat in self.seats:
            self.xPos_max = max(self.xPos_max, seat.xPos+1)
            self.yPos_max = max(self.yPos_max, seat.yPos+1)

    def countNeightbours(self):
        for seat in self.seats:
            seat.occupiedNeighbours = 0
            for shiftX in range(3):
                xPos_check = seat.xPos - 1 + shiftX
                if xPos_check >= self.xPos_max or xPos_check < 0:
                    continue

                for shiftY in range(3):
                    yPos_check = seat.yPos - 1 + shiftY

                    if yPos_check >= self.yPos_max or yPos_check < 0:
                        continue
                    elif xPos_check == seat.xPos and yPos_check == seat.yPos:
                        continue
                    else:
                        #seat_to_check = self.getPos(xPos_check, yPos_check)
                        seat_to_check = self.seats[yPos_check * self.xPos_max + xPos_check]
                        if seat_to_check.occupied == True:
                            seat.occupiedNeighbours += 1

    def switchNewstate(self):
        for seat in self.seats:
            if seat.occupied is not seat.nextOccState:
                self.changed = True
            seat.occupied = seat.nextOccState
            seat.nextOccState = None

    def performStep(self):
        self.changed = False
        self.countNeightbours()
    
        for seat in self.seats:
            if seat.posType == "seat":
                if seat.occupiedNeighbours >= 4:
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
                seat = self.getPos(x, y)
                if seat.posType == "seat" and seat.occupied == True:
                    print('#', end='')
                elif seat.posType == "seat" and seat.occupied == False:
                    print('L', end='')
                else:
                    print('.', end='')

            print("")
        print("")

    def countOccSeats(self):
        for seat in self.seats:
            if seat.occupied == True and seat.posType == "seat":
                self.occupiedSeats += 1

if __name__ == "__main__":
    #with open("test.txt") as file:
    with open("input.txt") as file:
        data = file.read()

    rows = data.split("\n")
    seatMap = CMap()

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
            seatMap.seats.append(newSeat)

    seatMap.setMaxValues()
    #seatMap.printMap()

    while(seatMap.changed):
        seatMap.performStep()
        #seatMap.printMap()

    seatMap.countOccSeats()
    #seatMap.printMap()

    print("\nResult 11_01: " + str(seatMap.occupiedSeats))