
#with open("test.txt") as file:
with open("input.txt") as file:
    data = file.read()

players_data = data.split("\n\n")
player1 = players_data[0].split("\n")[1:]
player2 = players_data[1].split("\n")[1:]

player1 = [ int(x) for x in player1 ]
player2 = [ int(x) for x in player2 ]

while(True):
    if player1[0] > player2[0]:
        player1.append(player1[0])
        player1.append(player2[0])

    else:
        player2.append(player2[0])
        player2.append(player1[0])

    player1 = player1[1:]
    player2 = player2[1:]

    if player1 == []:
        winner = player2
        break
    elif player2 == []:
        winner = player1
        break

result = 0
for idx, card in enumerate(winner):
    result += ((len(winner) - idx) * card )

print("\nResult 22_01: " + str(result))