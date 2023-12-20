import game_functions


deck = game_functions.Create_new_deck()
game_functions.shuffle(deck)
hand = game_functions.deal_cards(deck, 4)
card_on_table = game_functions.deal_cards(deck, 1)


while(len(hand) != 0):
    print("This is your hand:", hand)
    print("This is the card on table", card_on_table)

    print("1. Pick From the Main deck") # Re-invent call dispose from method and ask if you want to keep deck, main deck, or both.
    print("2. Swap with card on the table")
    print("3. Burn from deck")
    print("4. Burn to table")
    print("5. Use Power")
    print("6. Call game")

    choice = input("What do you want to do:")
    if choice == '1':
        game_functions.take_card(hand, card_on_table, deck)
        pass

    elif choice == '2':
        game_functions.pick_from_table(hand, card_on_table)
        pass
    
    elif choice == '3':
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
    

        


# So this works


            
#burn(hand, card_on_table, 1)

#print("This is your hand after burning", hand)
# print("Card on table is this:", card_on_table)




# burn_from_hand(0,2)
     
    
# use_power(1)
    
#print("This is your hand after power use", hand)
#print("Card on table is this:", card_on_table)

         
# pick_from_table(0)

#print("This is your hand after switching from table", hand)
# print("Card on table is this:", card_on_table)



# take_card(1,0)

#print("This is your hand after picking from main deck", hand)
# print("Card on table is this:", card_on_table)



# print(f"This is your final score:", call())





    


