# Kings, Queens, Jacks and Aces Card Game
# 20221101 v1.4
# 20221103 Now managed in GitHub

# Imports
import random as rnd

# Variables
players = [[], []]
pile = []
numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
jacks = [1, 1, 1, 1]
queens = [2, 2, 2, 2]
kings = [3, 3, 3, 3]
aces = [4, 4, 4, 4]
deck = numbers + jacks + queens + kings + aces

# Shuffle Deck
deck_shuffled = rnd.sample(deck, len(deck))

# Print deck
# print("Unshuffled Deck")
# print(deck)
# print("Shuffled Deck")
# print(deck_shuffled)

# Deal cards between the 2 players
for card in range(52):
    if card % 2 == 0:  # If an even number add to player1
        players[0].append(deck_shuffled[card])
    else:
        players[1].append(deck_shuffled[card])

# Play Game - Deal all cards onto pile
c_player = 1  # Current Player (0 & 1 )
while ((len(players[0]) > 0) or (len(players[1]) > 0)) is True:  # Player 0 or 1 still have cards
    c_player ^= 1  # Flip between 1 and 0
    print('c_player:', c_player)
    pile.append(players[c_player].pop(0))
    print("Pile:", pile)
    top_card_pos = len(pile)
    # print(top_card_pos)
    # print(pile[top_card_pos-1])
    top_card_val = pile[top_card_pos - 1]

print('Game Over')

    # if last_card == 0:
    #     for cards in range(1)
    #     pile.append(player2[0])
    # player1(pop(0))
    # last_card = len(pile)
