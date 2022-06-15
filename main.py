import spread
divining = True
while divining == True:
    # Get user input and convert it to an integer
    spread_choice = int(input("Choose how many cards to draw: "))
    # Check user input against known bad variables (negative numbers, numbers over 22)
    if spread_choice > 22:
        print("There are only 22 cards total within the Major Arcana deck.  Each card may only be drawn once per session.")
    elif spread_choice <= 0:
        print("Please choose a positive number...")
    # if previous tests pass, then pass the number into spread_of_(num) to draw the requested number of cards
    else:
        spread.spread_of_(spread_choice)
    # Whether or not to reshuffle.  If no, gives user a chance to copy down their results before exiting    
    reshuffle = input("Reshuffle the deck and try again? (y/n): ")
    if reshuffle == 'n':
        divining = False
        break
input("Be sure to write down or copy and paste your reading. :)")