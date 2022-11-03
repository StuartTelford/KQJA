# Kings, Queens, Jacks and Aces Card Game
# 20221101 v1.4
# 20221103 Now managed in GitHub

# Imports
import random as rnd

# Variables
p1 = []
p2 = []
pile = []
Numbers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Jacks = [1,1,1,1]
Queens = [2,2,2,2]
Kings = [3,3,3,3]
Aces = [4,4,4,4]
deck = Numbers + Jacks + Queens + Kings + Aces

# Shuffle Deck
deck_shuffled = rnd.sample(deck, len(deck))

# Print Deck
# print("*"*50)
# print("\nUnshuffled Deck")
# print(deck)
# print("*"*50)
# print("\nShuffled Deck")
# print(deck_shuffled)
# print("*"*50)

# Deal cards between the 2 players
for card in range(52):
    if card % 2 == 0: # If an even number add to player1
        p1.append(deck_shuffled[card])
    else:
        p2.append(deck_shuffled[card])

# Print cards for both players
print("\nPlayer1's Cards")
print(p1)
print("\nPlayer2's Cards")
print(p2)
print("\n")

# Play Game
c_player = 1  # Current Player
while ((len(p1) > 0) or (len(p2) > 0)) == True :  # Player 1 or 2 still have cards
    pile.append(p1.pop(0))
    print("Pile:",pile)
    top_card_pos = len(pile)
    print(top_card_pos)
    print(pile[top_card_pos-1])
    top_card_val = pile[top_card_pos-1]

    pile.append(p2.pop(0))
    print("Pile:",pile)
    last_card = len(pile)
    print(last_card)
    print(pile[last_card - 1])
    top_card_val = pile[last_card - 1]

    # if last_card == 0:
    #     for cards in range(1)
    #     pile.append(player2[0])
    # player1(pop(0))
    # last_card = len(pile)
    






    
