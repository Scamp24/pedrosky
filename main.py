import game_functions


deck = game_functions.Create_new_deck()
game_functions.shuffle(deck)
hand = game_functions.deal_cards(deck, 4)
card_on_table = game_functions.deal_cards(deck, 1)


while(len(hand) != 0):
    placeholder = game_functions.placeholder_array(hand)
    

    # [Add] 2 arrays | 1 for place holder loop to card 1 up to < len, keep the hand array to call and update values
    # [Add] Stats (Actions, Cards burned, powers used) In the future, Use counters for this)
    # [Add] if main deck is empty then deal another game then reshuffle the main deck with the cards on table

    print("This is your hand:", placeholder)
    print("This is your hand:", hand)
    print("This is the card on table", card_on_table[0])

    print("1. Pick From the Main deck") # [In Progress] | 75%  
    print("2. Swap with card on the table") # [Completed] | 100%
    print("3. Burn") # [Completed] | 100% 
    print("4. Call game") # [Completed]| 100%

    choice = input("What do you want to do: ")
    if choice == '1':
        game_functions.take_card(hand, card_on_table, deck, placeholder)
        pass

    elif choice == '2':
        game_functions.pick_from_table(hand, card_on_table)
        pass
    
    elif choice == '3':
        game_functions.burn(hand,card_on_table, placeholder)
        pass
    
    elif choice == '4': 
        print("Your final hand was:", hand)
        game_functions.call(hand)
        pass
    else: 
        print("That is not an option, please try again")
    