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

def new_game(hand):
    print("\n You are allowed to see 2 cards once")

    try:
        select_card1 = int(input("Select the card you want to see, Card: "))
        card1 = select_card1 - 1
    except ValueError:
        print("\n Invalid, input a number \n")
        return new_game(hand)

    if (card1 >= 0 and card1 < len(hand)):
        try:
            select_card2 = int(input("Select another card you want to see, Card: "))
            print("")
            card2 = select_card2 - 1 
        except ValueError:
            print("\n Invalid, input a number \n")
            return new_game(hand)
        
        if (card2 >= 0 and card2 <len(hand)) and card1 != card2:
            print("Card ", select_card1, "is ", hand[card1])
            print("Card ", select_card2, "is ", hand[card2],"\n" )
        else:
            print("\n The card you want to see is not in your hand or is the same as the previous, try again \n")
            new_game(hand)
    else:
        print("\n The card you want to see is not in your hand, try again \n")
        new_game(hand)
    

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

def burn(hand, card_on_table, placeholder):
    if len(placeholder) < 2:
        return print("\n Unable to burn, you must have at least 1 card remaining after burning \n")
    
    try:
        select_card1 = int(input("Select the 1st card you want to burn: "))
        card1 = select_card1 - 1 
    except ValueError:
        return print("\n Invalid, input a number \n")

    if hand[card1] == '':
        return print("\n Card picked is not within range, try again \n")

    if hand[card1][0] == 'joker':
        card_on_table.insert(0, hand[card1])
        hand[card1] = ''
    
    elif (card1 >= 0 and card1 < len(hand)):
        choice = input("How many cards are your burning? ")
        if choice == '1':
            if hand[card1][0] == card_on_table[0][0]:
                card_on_table.insert(0, hand[card1])
                hand[card1] = ''
            else:
                return print("The selected card does not match the card on table")

        elif choice == '2':
            if len(placeholder) < 3:
                print("Not enough card to burn 2 cards")
            else:
                burn_2_cards(select_card1,card1, hand, card_on_table)

        elif choice == '3':
            if len(placeholder) < 4:
                print("Not enough cards to burn 3")
            else:
                burn_3_cards(select_card1,card1, hand, card_on_table)
        else: 
            print("That is not within your card range")

def burn_2_cards(select_card1, card1, hand, card_on_table):
    try:
        select_card2 = int(input("Select the 2nd card you want to burn: "))
    except ValueError:
        return print("\n Invalid, input a number \n")
    
    if select_card2 == select_card1:
        return print("\n You picked the same card twice, try again \n")
            
    # 4th Checking bounds of cards after | Card 2 
    if (select_card2 - 1) >= 0 and (select_card2 - 1) < len(hand):
        card2 = select_card2 - 1  
    else:
        return print("\n Your 2nd pick is not within your hand \n")

    if hand[card1][0] == hand[card2][0]:
    # 3rd Check | Matching numbers 
        card_on_table.insert(0, hand[card1])
        card_on_table.insert(0, hand[card2])
        hand[card1] = ''
        hand[card2] = ''
    else:
        return print("\n One of the cards you selected does not match \n")


def burn_3_cards(select_card1, card1, hand, card_on_table):
    try:
        select_card2 = int(input("Select the 2nd card you want to burn: "))
    except ValueError:
        return print("\n Invalid, input a number \n")
        # Checking bounds of cards after 1 | Card 2
    if (select_card2 - 1) >= 0 and (select_card2 - 1) < len(hand):
        card2 = select_card2 - 1  
    else:
        return print("\n Your 2nd pick is not within your hand \n")
    
    try:
        select_card3 = int(input("Select the 3rd card you want to burn: "))
    except ValueError:
        return print("\n Invalid, input a number \n")
    # 4th Checking bounds of cards after 1 | Card 3
    if (select_card3 - 1) >= 0 and (select_card3 - 1) < len(hand):
        card3 = select_card3 - 1  
    else:
        return print("\n Your 3rd pick is not within your hand \n")
            
    if select_card1 == select_card2 or select_card2 == select_card3 or select_card1 == select_card3:
        return print("\n You picked the same card twice, try again \n")
            
    # Check | Matching numbers  
    if hand[card1][0] == hand[card2][0] and hand[card1][0] == hand[card3][0]:
        card_on_table.insert(0, hand[card1])
        card_on_table.insert(0, hand[card2])
        card_on_table.insert(0, hand[card3])
        hand[card1] = ''
        hand[card2] = ''
        hand[card3] = ''
    else:
        return print("\n One of the cards you selected does not match \n")



def use_power(card_on_table, deck, hand, placeholder): # Add to the Picking a card method
    if deck[0][0] == 7:  # Check if the card in the hand at the specified index is a Joker
        print(placeholder)
        try:
            select_card = int(input("You can view one of your cards, which one you want to see?  "))
            card1 = select_card - 1
        except ValueError:
            print("\n Invalid, input a number \n")
            return take_card(hand, card_on_table, deck, placeholder)

        if card1 >= 0 and card1 < len(hand):
            if hand[card1] == '':
                print("\n Card picked is not within range, try again \n")
                take_card(hand, card_on_table, deck, placeholder)
            
            print("Card ", select_card , "is: ", hand[card1])
        else:
            print("\n Card picked is not within range, try again \n")
            take_card(hand, card_on_table, deck, placeholder)

        card_on_table.insert(0, deck[0])
        del deck[0]

        # Add to which card can we see from hand (must print placeholder, and use logic from hand)
    elif deck[0][0] == 8:  # Check if the card in the hand at the specified index is a Joker
        card_on_table.insert(0, deck[0])
        del deck[0]
        print("\n You can see one of your opponent's card \n")
        # Simulated, you could try the but you need to create a 2nd hand
    elif deck[0][0] == 9:  # Check if the card in the hand at the specified index is a Joker
        card_on_table.insert(0, deck[0])
        del deck[0]
        print("\n You can trade one of your card to your opponent's card without looking \n")
        # Simulated, you could try the but you need to create a 2nd hand
        # An alternative is just swaping your own hand but again its not a big deal since its just swapping
    elif deck[0][0] == 'joker':

        print(placeholder)
        try:
            select_card = int(input("You can burn any card with the joker, which card do you want to pick? "))
            card1 = select_card - 1
        except ValueError:
            print("\n Invalid, input a number \n")
            return take_card(hand, card_on_table, deck, placeholder)

        if card1 >= 0 and card1 < len(hand):
            if hand[card1] == '':
                print("\n Card picked is not within range, try again \n")
                take_card(hand, card_on_table, deck, placeholder)
            
            print("Card ", select_card , "is: ", hand[card1])
        else:
            print("\n Card picked is not within range, try again \n")
            take_card(hand, card_on_table, deck, placeholder)

        card_on_table.insert(0, deck[0])
        card_on_table.insert(0, hand[card1])
        del deck[0]
        hand[card1] = ''
        

def pick_from_table(hand, card_on_table, placeholder):  # Completed
    print(placeholder)
    try:
        select_card = int(input("What card do you want to swap?: "))
        card1 = select_card - 1
    except ValueError:
        return print("\n Invalid, input a number \n")

    if hand[card1] == '':
        print("\n Card picked is not within range, try again \n")
        pick_from_table(hand, card_on_table)

    if (card1 >= 0 and card1 < len(hand)):
        temp = hand[card1]
        hand[card1] = card_on_table[0]
        card_on_table[0] = temp
        return hand, card_on_table
    else:
        print("\n Card picked is not within range, try again \n")
        pick_from_table(hand, card_on_table)
         

def take_card(hand, card_on_table, deck, placeholder):  # Completed
    print("You got: ", deck[0])
    
    print("1. Swap a card in your hand")
    print("2. Drop")

    hasPower = False
    if deck[0][0] == 7 or deck[0][0] == 8 or deck[0][0] == 9 or deck[0][0] == 'joker':
        print("3. Use power")
        hasPower = True
    try:
        pick = int(input("Your option: "))
    except ValueError:
        print("\n Invalid, input a number \n")
        return take_card(hand, card_on_table, deck, placeholder)
    
    if(pick == 1):
            print(placeholder)
            try:
                select_card = int(input("What card do you want to pick?: "))
                card1 = select_card - 1
            except ValueError:
                print("\n Invalid, input a number \n")
                return take_card(hand, card_on_table, deck, placeholder)
    

            if card1 >= 0 and card1 < len(hand):
                if hand[card1] == '':
                    print("\n Card picked is not within range, try again \n")
                    take_card(hand, card_on_table, deck, placeholder)

                temp = hand[card1]
                hand[card1] = deck[0]
                card_on_table.insert(0, temp)
                del deck[0]
            else:
                print("\n Card picked is not within range, try again \n")
                take_card(hand, card_on_table, deck, placeholder)

    elif(pick == 2):
        print("You drop the card")
        card_on_table.insert(0, deck[0])
        del deck[0]
    
    elif(pick ==3):
        if hasPower:
            use_power(card_on_table, deck, hand, placeholder)
        else:
            print("\n Not a valid a option \n")
            take_card(hand, card_on_table, deck, placeholder)

    else:
        print("\n Not a valid a option\n")
        take_card(hand, card_on_table, deck, placeholder)


def call(hand):  # Current bug: Index goes of of bounds with Joker 
    total = 0
    for card in hand:
        if isinstance(card, tuple) and len(card) == 2:
            value, suit = card
            if value == 'joker':
                total += 20
            elif value == 12 and suit == 'Swords':
                total += 0
            elif value == '':
                total += 0
            else:
                total += value
    print("This is your final Sum:", total)
    hand.clear()
    return total
    

