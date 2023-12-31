# PEDROSKY - Card Game

Card game played with a deck of 50 Spanish playing cards, comprising numbers 1-12 with symbols: Swords, Coins, Clubs, and Cups, along with two joker cards. The objective is to call the game when having the lowest sum within your hand.

This repository aims to create a single player version of the game to recreate functionalities of the game in Python. 

# Game requirements 
- 2-4 players 👤
- 1 Deck of Spanish playing cards 
  
# Game Setup ( 2x Pending GIFs)
- Shuffle and deal cards to players until each has 4 cards. (Pending GIF)
- Place remaining cards as the deck and reveal the top card as the "current card on table." (Pending GIF)
- The direction of the game is always to the right (From left to right from where game started) 

# Game Area ( 1 Big image) 
Explain the 3 zones (Hand, Main deck and Card on table)

# Gameplay ( 4 x Pending GIFS) 
- Each player holds 4 cards as their "hand" but can only view 2 initially. (Pending GIF)
- Players select 2 cards from their hand to view once (unchangeable until their turn). (Pending GIF)
- The player who received their hand first starts the game.
- On a turn, players draw from the main deck to swap or discard cards on their hand. (Pending GIF)
- Player burn or swap cards until the game is called. Must remain at least with 1 card 
- When the game is called, every player gets the sum of their hand and a winner is determined. (Pending GIF)

# Actions ( Pending GIFS) 
List of possible actions within a turn
## Burn
Burning means disposing 1 or more cards in your hand that have a matching numbers. There a multiple ways to burn but the only requirement before burning anything is to at least have 1 card in your hand after burning, if this is not consider then its not possible. Whenever cards are burned they are dispose into the card on table.
- Burning from your hand
If in the player's hand there is 2 or 3 matching numbers then cards could be burned




# Penalties
- When a player intends to burn a card and the action is no possible, player must add to their hand the card on table


# Edge Cases 

# Dictionary? 
For futher clarity here is a summarize version of the terminology used in the description and gameplay:


# Powers
Special cards 7, 8, 9, and Joker have powers whenever a player draw a card from the main deck.
7: Reveals a card from the player's hand.
8: Reveals a card from another player's hand.
9: Allows a blind swap between player hands.
Joker: Acts as any number but not symbol. Can burn any single card in a hand. Whenever its in your hand, it can burn but itself 

# Real life version vs Repository
Since this is a single player version and there's no functionality to add more players or CPU opponents, therefore they are certain functionalities missing 

# Developer's Notes

The objective was createa a single player version of the game in python to help visualize how it could be done. This is just the bare logics of the game, for the future is to develop in either PC or Mobile version of this game with 2 goals in mind:

- Add CPU opponent, meaning that it would require some sort of AI to play vs the player
- Add Multiplayer | Possibly cross-platform


