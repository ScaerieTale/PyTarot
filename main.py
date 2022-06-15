import spread
divining = True
while divining is True:
    spread_choice = int(input("Choose how many cards to draw: "))
    if spread_choice > 22:
        print("There are only 22 cards total within the Major Arcana deck.  Each card may only be drawn once per session.")
    elif spread_choice < 0:
        print("Please choose a positive number...")
    elif spread_choice > 0 and spread_choice <= 22:
        spread.spread_of_(spread_choice)
        
    else:
        print("Do not trifle lightly where angels fear to tread.")
    
    reshuffle = input("Reshuffle the deck and try again? (y/n): ").lower
    if reshuffle == 'n' or reshuffle == 'no':
        input("Be sure to write down or copy and paste your reading. :)")
        divining = False