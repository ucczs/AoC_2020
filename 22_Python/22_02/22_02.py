import copy

def handAlreadyPlayed(playedHands, currentHand):
    for playedHand in playedHands:
        if currentHand[0] == playedHand[0] and currentHand[1] == playedHand[1]:
            return True
    return False

def getScore(winner_hand):
    result = 0
    for idx, card in enumerate(winner_hand):
        result += ((len(winner_hand) - idx) * card )
    return result

def playGame(player1, player2):
    playedHands = set()
    while(True):
        currentHand = [tuple(player1), tuple(player2)]
        if handAlreadyPlayed(playedHands, currentHand):
            score = getScore(player1)
            return 1, score

        playedHands.add(tuple(currentHand))

        if len(player1) <= player1[0] or len(player2) <= player2[0]:
            if player1[0] > player2[0]:
                battleResult = 1
            else:
                battleResult = 2
        else:
            player1_sub = player1[1:1+player1[0]]
            player2_sub = player2[1:1+player2[0]]
            battleResult, _ = playGame(player1_sub, player2_sub)

        if battleResult == 1:
            player1.append(player1[0])
            player1.append(player2[0])
        else:
            player2.append(player2[0])
            player2.append(player1[0])

        player1 = player1[1:]
        player2 = player2[1:]

        if player1 == []:
            score = getScore(player2)
            return 2, score
        elif player2 == []:
            score = getScore(player1)
            return 1, score



#with open("test.txt") as file:
#with open("test2.txt") as file:
with open("input.txt") as file:
    data = file.read()

players_data = data.split("\n\n")
player1 = players_data[0].split("\n")[1:]
player2 = players_data[1].split("\n")[1:]

player1 = [ int(x) for x in player1 ]
player2 = [ int(x) for x in player2 ]

winner, score = playGame(player1, player2)

print("\nResult 22_02: " + str(score))
