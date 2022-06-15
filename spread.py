from random import randint

def spread_of_(num):
    major_arcana_deck = ['The Fool', 'The Magician', 'The High Priestess', 
'The Empress', 'The Emperor', 'The Hierophant', 
'The Lovers', 'The Chariot','Strength', 
'The Hermit', 'Wheel of Fortune', 'Justice', 
'The Hanged Man', 'Death', 'Temperance', 
'The Devil', 'The Tower', 'The Star', 
'The Moon', 'The Sun', 'Judgement', 
'The World']
    """Draw a single card and print its face and position to console."""
    for i in range(num):

        card = major_arcana_deck[randint(0, len(major_arcana_deck) -1)]
        major_arcana_deck.remove(card)
        position = randint(0, 1)
        if position == 0:
            print(f"{card} is upright.")
        else:
            print(f"{card} is reversed.")