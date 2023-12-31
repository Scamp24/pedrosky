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

def burn(hand, card_on_table, placeholder):
    if len(placeholder) < 2:
        return print("Unable to burn, you must have at least 1 card remaining after burning")
    
    select_card1 = int(input("Select the 1st card you want to burn: "))
    card1 = select_card1 - 1 

    if hand[card1] == '':
        return print("Card picked is not within range, try again")

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
    select_card2 = int(input("Select the 2nd card you want to burn: "))
    if select_card2 == select_card1:
        return print("You picked the same card twice, try again")
            
    # 4th Checking bounds of cards after | Card 2 
    if (select_card2 - 1) >= 0 and (select_card2 - 1) < len(hand):
        card2 = select_card2 - 1  
    else:
        return print("Your 2nd pick is not within your hand")

    if hand[card1][0] == hand[card2][0]:
    # 3rd Check | Matching numbers 
        card_on_table.insert(0, hand[card1])
        card_on_table.insert(0, hand[card2])
        hand[card1] = ''
        hand[card2] = ''
    else:
        return print("One of the cards you selected does not match")


def burn_3_cards(select_card1, card1, hand, card_on_table):
    select_card2 = int(input("Select the 2nd card you want to burn: "))
        # Checking bounds of cards after 1 | Card 2
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
            
    if select_card1 == select_card2 or select_card2 == select_card3 or select_card1 == select_card3:
        return print("You picked the same card twice, try again")
            
    # Check | Matching numbers  
    if hand[card1][0] == hand[card2][0] and hand[card1][0] == hand[card3][0]:
        card_on_table.insert(0, hand[card1])
        card_on_table.insert(0, hand[card2])
        card_on_table.insert(0, hand[card3])
        hand[card1] = ''
        hand[card2] = ''
        hand[card3] = ''
    else:
        return print("One of the cards you selected does not match")



def use_power(card_on_table, deck, hand, placeholder): # Add to the Picking a card method
    if deck[0][0] == 7:  # Check if the card in the hand at the specified index is a Joker
        print(placeholder)
        select_card = int(input("You can view one of your cards, which one you want to see?  "))
        card1 = select_card - 1

        if card1 >= 0 and card1 < len(hand):
            if hand[card1] == '':
                print("Card picked is not within range, try again")
                take_card(hand, card_on_table, deck, placeholder)
            
            print("Card ", select_card , "is: ", hand[card1])
        else:
            print("Card picked is not within range, try again")
            take_card(hand, card_on_table, deck, placeholder)

        card_on_table.insert(0, deck[0])
        del deck[0]

        # Add to which card can we see from hand (must print placeholder, and use logic from hand)
    elif deck[0][0] == 8:  # Check if the card in the hand at the specified index is a Joker
        card_on_table.insert(0, deck[0])
        del deck[0]
        print("You can see one of your opponent's card")
        # Simulated, you could try the but you need to create a 2nd hand
    elif deck[0][0] == 9:  # Check if the card in the hand at the specified index is a Joker
        card_on_table.insert(0, deck[0])
        del deck[0]
        print("You can trade one of your card to your opponent's card without looking")
        # Simulated, you could try the but you need to create a 2nd hand
        # An alternative is just swaping your own hand but again its not a big deal since its just swapping
    elif deck[0][0] == 'joker':

        print(placeholder)
        select_card = int(input("You can burn any card with the joker, which card do you want to pick? "))
        card1 = select_card - 1

        if card1 >= 0 and card1 < len(hand):
            if hand[card1] == '':
                print("Card picked is not within range, try again")
                take_card(hand, card_on_table, deck, placeholder)
            
            print("Card ", select_card , "is: ", hand[card1])
        else:
            print("Card picked is not within range, try again")
            take_card(hand, card_on_table, deck, placeholder)

        card_on_table.insert(0, deck[0])
        card_on_table.insert(0, hand[card1])
        del deck[0]
        hand[card1] = ''
        

def pick_from_table(hand, card_on_table):  # Completed
    print(hand)
    select_card = int(input("What card do you want to swap?: "))
    card1 = select_card - 1

    if hand[card1] == '':
        print("Card picked is not within range, try again")
        pick_from_table(hand, card_on_table)

    if (card1 >= 0 and card1 < len(hand)):
        temp = hand[card1]
        hand[card1] = card_on_table[0]
        card_on_table[0] = temp
        return hand, card_on_table
    else:
        print("Card picked is not within range, try again")
        pick_from_table(hand, card_on_table)
         

def take_card(hand, card_on_table, deck, placeholder):  # Completed
    print("You got: ", deck[0])
    
    print("1. Swap a card in your hand")
    print("2. Drop")

    hasPower = False
    if deck[0][0] == 7 or deck[0][0] == 8 or deck[0][0] == 9 or deck[0][0] == 'joker':
        print("3. Use power")
        hasPower = True

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
    
    elif(pick ==3):
        if hasPower:
            use_power(card_on_table, deck, hand, placeholder)
        else:
            print("Not a valid a option")
            take_card(hand, card_on_table, deck, placeholder)

    else:
        print("Not a valid a option")
        take_card(hand, card_on_table, deck, placeholder)


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
    hand.clear()

    return total_sum
