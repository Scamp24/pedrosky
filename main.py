import game_functions


deck = game_functions.Create_new_deck()
game_functions.shuffle(deck)
hand = game_functions.deal_cards(deck, 4)
card_on_table = game_functions.deal_cards(deck, 1)


while(len(hand) != 0):
    # [Add] 2 arrays | 1 for place holder loop to card 1 up to < len, keep the hand array to call and update values
    # [Add] Stats (Actions, Cards burned, powers used) In the future, Use counters for this)
    # [Add] if main deck is empty then deal another game then reshuffle the main deck with the cards on table

    print("This is your hand:", hand)
    print("This is the card on table", card_on_table)

    print("1. Pick From the Main deck") # [Add] Keep or drop on table | 80% 
    print("2. Swap with card on the table") # [Completed] | 100%
    print("3. Burn in hand") # [In Progress] | 80%, Test pending
    print("4. Burn to table") # [In Progress] | Desc: A card from my hand is the same as the card on table (Single card burn)
    print("5. Use Power") # [In Progress]
    print("6. Call game") # [In Progress]

    choice = input("What do you want to do: ")
    if choice == '1':
        game_functions.take_card(hand, card_on_table, deck)
        pass

    elif choice == '2':
        game_functions.pick_from_table(hand, card_on_table)
        pass
    
    elif choice == '3':
        game_functions.burn_from_hand(hand, card_on_table)
        pass
    
    elif choice == '4':
        pass
    
    elif choice == '5':
        pass
    
    elif choice == '6': 
        game_functions.call(hand)
        print("Your final hand was:", hand)
        hand.clear()
        pass
    else: 
        print("That is not an option, please try again")
    

            
#burn(hand, card_on_table, 1)

#print("This is your hand after burning", hand)
# print("Card on table is this:", card_on_table)


     
    
# use_power(1)
    
#print("This is your hand after power use", hand)
#print("Card on table is this:", card_on_table)

         
# pick_from_table(0)

#print("This is your hand after switching from table", hand)
# print("Card on table is this:", card_on_table)









    


