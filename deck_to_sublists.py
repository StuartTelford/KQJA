# Scratchfile
# Divide cards between 2 sublists, 1 for each player alternately
# 20221105 1.0

deck_shuffled = [
        0, 0, 2, 3, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 0, 4, 3, 1, 2,
        0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 4, 0, 0, 3]

players = [[],[]]

# Deal cards between the 2 players
for card in range(52):
    if card % 2 == 0: # If an even number add to player1
        players[0].append(deck_shuffled[card])
    else:
        players[1].append(deck_shuffled[card])

print(players)
print('')
print('Player1',players[0])
print('Player2',players[1])