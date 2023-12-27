import random

def placeholder_array(hand):
    placeholder = []
    for index, element in enumerate(hand):
        if isinstance(element, tuple):
            placeholder.append(f"Card {index + 1}")
    return placeholder

def Create_new_deck():   
    symbols = ['Swords', 'Cups', 'Coins', 'Clubs']
    #Defining the numbers per symbol
    numbers = list(range(1, 13))
    standard_cards = [(number, symbol) for symbol in symbols for number in numbers]
    jokers = [('joker', 'Standard'), ('joker', 'Standard')]
    deck = standard_cards + jokers
    return deck


def shuffle(deck):
    random.shuffle(deck)
    return deck


def deal_cards(deck, num_cards):
    hand =  deck[:num_cards]
    del deck[:num_cards]
    return hand


def emptyDeck(deck, card_on_table): # Not tested
    deck = random.shuffle(card_on_table)
    card_on_table.clear()
    card_on_table.insert(0, deck[0])
    del deck[0]
    return deck, card_on_table

def burn(hand, main_deck, index_of_hand):
    if index_of_hand < len(hand):
        if hand[index_of_hand][0] == 'joker':  # Check if the card in the hand at the specified index is a Joker
            main_deck.insert(0, hand[index_of_hand])
            del hand[index_of_hand]

        elif hand[index_of_hand][0] == main_deck[0][0]:  # Compare the selected card from hand to the first card in the main deck
            main_deck.insert(0, hand[index_of_hand])  # Re-add the matched card to the top of the deck\
            del hand[index_of_hand]


def burn_from_hand(hand, card_on_table, placeholder):
    # 1st check | Unable to burn if you have less than 3 cards
    if len(placeholder) < 3:
        return print("Unable to burn, you must have at least 1 card remaining after burning")
    
    print(hand)
    select_card1 = int(input("Select the 1st card you want to burn: "))
    card1 = select_card1 - 1 

    # 2nd Check | A joker can be burnt by itself if selected
    if hand[card1][0] == 'joker':
        card_on_table.insert(0, hand[card1])
        hand[card1] == ''

    # How many cards to burn? 2 or 3?
    elif (card1 >= 0 and card1 < len(hand)):
        another_card = (input("Is there a 3rd card? "))
        another_card.lower()

        if another_card == "yes": # Player decided to burn 3 cards at a time
            if len(placeholder) < 4:
                return print("Unable to burn, you must have at least 1 card remaining after burning")
            
            if select_card1 == select_card2 or select_card2 == select_card3 or select_card1 == select_card3:
                return print("You picked the same card twice, try again")
            
            select_card2 = int(input("Select the 2nd card you want to burn: "))
            # 4th Checking bounds of cards after 1 | Card 2
            if (select_card2 - 1) >= 0 and (select_card2 - 1) < len(hand):
                card2 = select_card2 - 1  
            else:
                return print("Your 2nd pick is not within your hand")

            select_card3 = int(input("Select the 3rd card you want to burn: "))
            # 4th Checking bounds of cards after 1 | Card 3
            if (select_card3 - 1) >= 0 and (select_card3 - 1) < len(hand):
                card3 = select_card3 - 1  
            else:
                return print("Your 3rd pick is not within your hand")
            
            #Current Bug: At the time of deleting the card from the hand, the index gets moved
            # 3rd Check | Matching numbers  
            if hand[card1][0] == hand[card2][0] and hand[card1][0] == hand[card3][0]:
                card_on_table.insert(0, hand[card1])
                card_on_table.insert(0, hand[card2])
                card_on_table.insert(0, hand[card3])
                hand[card1] = ''
                hand[card2] = ''
                hand[card3] = ''
            else:
                return print("One of the cards you selected does not match")
        
        else: # Meaning that player decided to only burn 2 
            select_card2 = int(input("Select the 2nd card you want to burn: "))
            if select_card2 == select_card1:
                return print("You picked the same card twice, try again")
            
            # 4th Checking bounds of cards after | Card 2 
            if (select_card2 - 1) >= 0 and (select_card2 - 1) < len(hand):
                card2 = select_card2 - 1  
            else:
                return print("Your 2nd pick is not within your hand")

            #Current Bug: At the time of deleting the card from the hand, the index gets moved
            if hand[card1][0] == hand[card2][0]:
                # 3rd Check | Matching numbers 
                card_on_table.insert(0, hand[card1])
                card_on_table.insert(0, hand[card2])
                hand[card1] = ''
                hand[card2] = ''
            else:
                return print("One of the cards you selected does not match")
    else: 
        return print("The card you selected is not in your hand, Try again")



    


def use_power(card1, hand, card_on_table):
    if card1 < len(hand):
        if hand[card1][0] == 7:  # Check if the card in the hand at the specified index is a Joker
                card_on_table.insert(0, hand[card1])
                del hand[card1]
                print("You can see one of your cards")
        elif hand[card1][0] == 8:  # Check if the card in the hand at the specified index is a Joker
                card_on_table.insert(0, hand[card1])
                del hand[card1]
                print("You can see one of your opponent's card")
        elif hand[card1][0] == 9:  # Check if the card in the hand at the specified index is a Joker
                card_on_table.insert(0, hand[card1])
                del hand[card1]
                print("You can trade one of your card to your opponent's card without looking")
        else:
            print("This card does not have any power")     


def pick_from_table(hand, card_on_table):  # Completed
    print(hand)
    select_card = int(input("What card do you want to swap?: "))
    card1 = select_card - 1
    if (card1 >= 0 and card1 < len(hand)):
        temp = hand[card1]
        hand[card1] = card_on_table[0]
        card_on_table[0] = temp
        return hand, card_on_table
    else:
        print("You picked a card outside of the range")
        pick_from_table(hand, card_on_table)
         

def take_card(hand, card_on_table, deck, placeholder):  # Completed
    print("You got: ", deck[0])
    
    print("1. Swap a card in your hand")
    print("2. Drop")
    pick = int(input("Your option: "))
    
    if(pick == 1):
            print(hand)
            select_card = int(input("What card do you want to pick?: "))
            card1 = select_card - 1
            if card1 >= 0 and card1 < len(hand):
                if hand[card1] == '':
                    print("Card picked is not within range, try again")
                    take_card(hand, card_on_table, deck, placeholder)

                temp = hand[card1]
                hand[card1] = deck[0]
                card_on_table.insert(0, temp)
                del deck[0]
            else:
                print("Card picked is not within range, try again")
                take_card(hand, card_on_table, deck, placeholder)

    elif(pick == 2):
        print("You drop the card")
        card_on_table.insert(0, deck[0])
        del deck[0]
    else:
        print("Not a valid a option")
        take_card(hand, card_on_table, deck)


def call(hand):  # Current bug: Index goes of of bounds with Joker 
    for i, card in enumerate(hand):
        # Check if the card is a joker and replace it with 20
        if card[0] == 'joker':
            hand[i] = (20, card[1])
        # Check if the card is the 12 of Swords and replace it with 0
        elif card[0] == 12 and card[1] == 'Swords':
            hand[i] = (0, card[1])

    # Perform the sum operation after converting jokers to 20 and 12 of Swords to 0
    
    total_sum = sum(card[0] for card in hand)
    print("This is your final Sum:", total_sum)
    return total_sum
