from random import randint
# import the Major Arcana Deck and create an easier to type short var name locally
from deck import major_arcana_deck
mad = major_arcana_deck

def spread_of_(num):
    """Draw a single card and print its face and position to console."""
    for i in range(num):
        card = mad[randint(0, len(mad))]
        card.pop(mad)
        position = randint(0, 1)
        if position == 0:
            print(f"{card} is upright.")
        else:
            print(f"{card} is reversed.")