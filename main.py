import game_functions


deck = game_functions.Create_new_deck()
game_functions.shuffle(deck)
hand = game_functions.deal_cards(deck, 4)
card_on_table = game_functions.deal_cards(deck, 1)

new_game = True

while(len(hand) != 0):
    placeholder = game_functions.placeholder_array(hand)

    # [Enhance] Visual look of the statements
    # [Fix] Some input are int and might lead to error when strings are registered
    # [Add] if main deck is empty then deal another game then reshuffle the main deck with the cards on table

    print("This is your hand:", placeholder)
    # print("This is your hand:", hand) # This is used to check the hand
    print("\n This is the card on table", card_on_table[0])

    if (new_game):
        game_functions.new_game(hand)
        new_game = False

    print("1. Pick From the Main deck") # [Completed] | 100% 
    print("2. Swap with card on the table") # [Completed] | 100%
    print("3. Burn") # [Completed] | 100% 
    print("4. Call game") # [Completed]| 100%

    choice = input("\nWhat do you want to do: ")
    print()
    if choice == '1':
        game_functions.take_card(hand, card_on_table, deck, placeholder)
        pass

    elif choice == '2':
        game_functions.pick_from_table(hand, card_on_table, placeholder)
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
    