import random

def Create_new_deck():   
    symbols = ['Swords', 'Cups', 'Coins', 'Clubs']
    #Defining the numbers per symbol
    numbers = list(range(1, 13))
    # Making an array? with number and symbol in each instance of the array
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


def burn(hand, main_deck, index_of_hand):
    if index_of_hand < len(hand):
        if hand[index_of_hand][0] == 'joker':  # Check if the card in the hand at the specified index is a Joker
            main_deck.insert(0, hand[index_of_hand])
            del hand[index_of_hand]

        elif hand[index_of_hand][0] == main_deck[0][0]:  # Compare the selected card from hand to the first card in the main deck
            main_deck.insert(0, hand[index_of_hand])  # Re-add the matched card to the top of the deck\
            del hand[index_of_hand]


def burn_from_hand(card1 , card2, hand, card_on_table):
    firstdelete = min(card1, card2)
    if firstdelete == card2:
        card1, card2 = card2, card1

    if card1 < len(hand) and card2 < len(hand):
        if hand[card1][0] == hand[card2][0]:
            card_on_table.insert(0, hand[card1])
            card_on_table.insert(0, hand[card2])
            del hand[card1]
            del hand[card2 - 1]


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


def pick_from_table(hand, card_on_table):

    # Current bugs for this:
    # The If we get a card out of bounds is not doing the correction 

    # Still figuring it out
    print(hand)
    select_card = int(input("What card do you want to swap?: "))
    card1 = select_card - 1
    while (card1 >= 0 and card1 < len(hand)):  
        hand.append(card_on_table[0])
        card_on_table.insert(0, hand[card1])
        del card_on_table[1]
        del hand[card1]
        return hand, card_on_table
         

def take_card(hand, card_on_table, deck):
    
    hand.append(deck[0])
    print("You got:", deck[0])
    del deck[0]
    
    print("1. Keep and dispose")
    print("2. Keep only")
    dispose = int(input("Your option: "))
    while(dispose > 0 and dispose < 3):
        if(dispose == 1):
                print(hand)
                select_card = int(input("What card do you want to dispose?: "))
                card1 = select_card - 1
                if card1 < len(hand):
                    card_on_table.insert(0, hand[card1])
                    del hand[card1]
        elif(dispose == 2):
            print("You've kept the card")
        else:
            print("Not a valid a option")
        return hand, card_on_table, deck


def call(hand):
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

# Now I added a comment 