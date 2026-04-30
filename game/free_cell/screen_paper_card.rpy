# paper card to display
screen paper_card(card):
    if card.suit == Card.HEARTS:
        add ("poker/poker_hearts_%d.png" % card.number)
    elif card.suit == Card.CLUBS:
        add ("poker/poker_clubs_%d.png" % card.number)
    elif card.suit == Card.SPADES:
        add ("poker/poker_spades_%d.png" % card.number)
    elif card.suit == Card.DIAMONDS:
        add ("poker/poker_diamonds_%d.png" % card.number)
    else:
        frame:
            xysize (CARD_WIDTH, CARD_HEIGHT)
            text card.name:
                xalign 0
                yalign 0
