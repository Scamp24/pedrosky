# PEDROSKY - Card Game

Card game played with a deck of 50 Spanish playing cards, comprising numbers 1-12 with symbols: Swords, Coins, Clubs, and Cups, along with two joker cards. The objective is to call the game when having the lowest sum within your hand.

This repository aims to create a single player version of the game to recreate functionalities of the game in Python. 

# Game requirements 
- 2-4 players 👤
- 1 Deck of Spanish playing cards 
  
# Game Setup ( 2x Pending GIFs) ✅
- Shuffle and deal cards to players until each has 4 cards. (Pending GIF) ✅

- Place remaining cards as the main deck and reveal the top card as the "current card on table." (Pending GIF) ✅
- The direction of the game is always to the right (From left to right from where game started) 

# Game Area ( 1 Big image) ✅
Explain the 3 zones (Hand, Main deck and Card on table)
<img src="https://github.com/Scamp24/pedrosky/assets/61484587/5798470b-502a-4a5e-9c37-1e14ed314e60" width="700" height="500">




# Gameplay ( 1 x Pending GIFS) 
- Each player holds 4 cards as their "hand" but can only view 2 initially.
- Players select 2 cards from their hand to view once (unchangeable until their turn). (Pending GIF)
- Players can't change cards position when playing
- The player who received their hand first starts the game.
- On a turn, players draw from the main deck to swap or discard cards on their hand. 
- Player burn or swap cards until the game is called. Must remain at least with 1 card 
- When the game is called, every player gets the sum of their hand and a winner is determined. 

# Actions ( Pending GIFS) 
List of possible actions within a turn, only 1 action per turn is allowed

## Burn (3 x)
Burning means disposing 1 or more cards in your hand that have a matching numbers. There a multiple ways to burn but the only requirement before burning anything is to at least have 1 card in your hand after burning, if this is not consider then its not possible. Whenever cards are burned they are dispose into the card on table.
- Burning from your hand: If in the player's hand there is 2 or 3 matching numbers then cards could be burned
- Burning from your hand to the card on table: If there's 1 or more cards in player's hand that matches the number of the card on table, it is allowed to burn
- Burning from picking from the main deck: When a player draw from the main deck and the card's number matches 1 or more in the player's hand, it is allowed to burn

## Draw Card ( 2x)
In the player's turn, there's is the possibility of either burning or getting a card from the main deck to futher progress with their game, after picking a card there is 2 options
- **Burn**: If there's the possibility to burn a card
- **Swap**: The player could swap the card for one of the card in the hand and dispose it to the card on table
- **Dispose**: The player does not want the current card that it draw, the card is throw to the card on table

## Swap ( 1x )
The player could swap a card from their hand to the card on table

**Note**: A player can't just add the card to the hand, it must do one of the actions above 

## Call Game ( 1x )
The player feels certain that it has the lowest sum in the table, player must hit the table twice and all players from the table must reveal their hands. Game ends

# Powers (x4 )
## During the game
 7, 8, 9, and Joker have powers whenever a player draw a card from the main deck.
- 7: Reveals a card from the player's hand.
- 8: Reveals a card from another player's hand.
- 9: Allows a blind swap between player hands.
- Joker: Acts as any number but not symbol. Can burn any single card in a hand. Whenever its in your hand, it can burn but itself

If the player desires to use a power, then it must announce to the table that it will use the power and dispose it to the card on table. Power usage is completely optional and cards are treated as numbers regardless wether a power was used or not. 

## Game is called
- 12 of Swords: This card whenever is kept in the player's hand at the end of the game, this card value is 0. In other words the best card
- Joker: This card whenever is kept in player's hand at the end of the game, this card value is 20. The worst card when game is called

# Penalties (1x )
- When a player intends to burn a card and the action is no possible, player must add to their hand the card on table

# Standard Game Setting: Points System
This game is based on a point system where every player start with 0 points 
## How does it work?
Whenever a game is called, the winner will substract the sum of the hand with the points (Eg: 0  --> Game is won with a sum of 2 -->  -2) the rest of the players will have to add the sum of their hands to their points (Eg: 0 --> lost game with 11 --> 11).
## How a winner its determined?
Whichever player reaches the 100 point mark, must exit the table. The winner is the last player on the table.
## What is a winning/losing condition?
The player that called the game MUST be the lowest sum in case its not the player must add +10 points for not winning. The rest of the player follow a behaviour of losing even if they tied or beat the caller. Calling a game is betting you own the lowest sum

# List of Game Settings
- Standard mode: Points System
- playing with no points for fun/practice.
-  Playing with more decks but this would mean that the hand must be double and player always sees half of the deck (Eg: Playing 2 decks, Hands must be 8 cards, player is allowed to see 4). No deck limit
- League Mode: Counting win as 3 points, Ties as 1 point, losses as 0 points. Unlimited amount of games
- Win mode: Only counting wins
-  Custom: Own rules 

# Edge Cases ( 3x except ties) 
- No card on table: There is a rare chance that the card on table is missing after the first few rounds, in this case no card has to be added from the main deck to the table but rather the game continues. Eventually there will be a guarantee throughout the game that a card will be on the table.
- No cards in the main deck: In a long game, after the main deck is depleted, the cards coming the stack on the table must be shuffle and placed in the main deck and a card must be draw to have a card on table. Game resumes after this
- Swap 2 cards for 1: Whenever a player's hand is down to the last 2 cards, by rule a player must hold at least 1 card during the whole game. However if the remaning 2 cards are able to be burn there is the possibility of burning those 2 cards and replacing the empty hand with the card that was on the table before burning, this would guarantee that the player's hand is holding at least 1 card. This action is not limited to the last 2 cards
- Ties: In a game setting when players are not using points, the winner are all the players that tied with the player that made the call. In a game setting with point, refer to the point system.

# Real life version vs Repository
Since this is a single player version and there's no functionality to add more players or CPU opponents, therefore they are certain functionalities missing 

# Developer's Notes 

The objective was creating a single player version of the game in python to help visualize how it could be done. This is just the bare logics of the game, for the future is to develop in either PC or Mobile version of this game with 2 goals in mind:

- Add CPU opponent, meaning that it would require some sort of AI to play vs the player
- Add Multiplayer | Possibly cross-platform

## Developer Profile
Hello, I'm Salomon and I'm the creator of this repository (@Scamp24). This game was introduced to me a few years ago by one of my friends and I enjoyed playing it. After I started college I wanted to keep playing but sometimes I don't have someone to play right away, for this I wanted to build a python version of the game functionalities to envision to create this game in either PC or Mobile platform and have friends play vs me. 

I've teached this game to more than 100+ people and I have full understanding of the mechanics and a large repertoire of strategies upon my sleeve which I share with everyone. My love for this game is huge, this game is a little bit of luck but despite of the luck you might fool or outsmart your opponents and get the win. game gets more fun and complicated once you have mastered playing with one deck, you start playing with more and more decks. The main benefit which I believe this game brings is that you keep your brain and memory active at all times, it could be compared with chess at a different scale but surely it requires getting your head to think of your next moves and your opponent's moves in advanced. 

## What's next?

This was just an attempt to recreate the basic function of the game in a programming enviroment. I'm planning to learn some swift to inspect the limitations and capacity to build this game IOS natively and have it on my phone on the go. For PC I have some experience and I could build it in Python and make it an executable with all the dependencies. However I believe there is a large range of opportunities here, I could build this on website using some javascript, react, node and more web dev technologies. The other big opportunity is to build in a game engine, fortunately this will be a 2D game so no 3D work is being done, with the intention of having no issues with GPU 

## Next Step

The next step involves, choosing which tech stack I want to start learning and attempt to translate the logic that I have with python which mainly would be the back-end and learn the front-end of the platform I would be developing. As of now I don't believe there's a need for a Database unless the user progress, stats, level and multiplayer get implemented somewhere in the future.

## For you
You have the full logic of this game in this repository, if you want to clone it and explore more functions feel free to so! If there's a bug in the code, you are more than welcome to clone and request any changes.

## Conclusion

This project had another objective in my life which was creating the habit of building something in my free time and something that I love. I time myself the amount of time I spent to this project daily to avoid burnout during these holidays (Winter 2023). I've incredibly motivated and I have also the discipline to learn new stuff and get out of my comfort zone. Everything flows when you love what you do and I hope the next repository will be a huge step into my life and career. 

