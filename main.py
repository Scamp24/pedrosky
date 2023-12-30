import game_functions


deck = game_functions.Create_new_deck()
game_functions.shuffle(deck)
hand = game_functions.deal_cards(deck, 4)
card_on_table = game_functions.deal_cards(deck, 1)


while(len(placeholder) != 0):
    placeholder = game_functions.placeholder_array(hand)
    

    # [Add] 2 arrays | 1 for place holder loop to card 1 up to < len, keep the hand array to call and update values
    # [Add] Stats (Actions, Cards burned, powers used) In the future, Use counters for this)
    # [Add] if main deck is empty then deal another game then reshuffle the main deck with the cards on table

    print("This is your hand:", placeholder)
    print("This is your hand:", hand)
    print("This is the card on table", card_on_table)

    print("1. Pick From the Main deck") # [Completed] | 100% 
    print("2. Swap with card on the table") # [Completed] | 100%
    print("3. Burn in hand") # [Completed] | 100% 
    print("4. Burn to table") # [In Progress] | Desc: A card from my hand is the same as the card on table (Single card burn)
    print("5. Use Power") # [In Progress]
    print("6. Call game") # [In Progress] | Broken, yet to look for the bug

    choice = input("What do you want to do: ")
    if choice == '1':
        game_functions.take_card(hand, card_on_table, deck, placeholder)
        pass

    elif choice == '2':
        game_functions.pick_from_table(hand, card_on_table)
        pass
    
    elif choice == '3': # Matching numbers from hand but not table (eg: Card on table is 2, but your hand has 3 cards of "4")
        game_functions.burn_from_hand(hand, card_on_table, placeholder)
        pass
    
    elif choice == '4': # Matching numbers from hand and table (eg: Card on table is 4 and your hand has 3 cards of "4")
        game_functions.burn_to_table(hand, card_on_table)
        pass
    
    elif choice == '5':
        # game_functions.use_power()
        pass
    
    elif choice == '6': 
        game_functions.call(hand)
        print("Your final hand was:", hand)
        hand.clear()
        pass
    else: 
        print("That is not an option, please try again")
    