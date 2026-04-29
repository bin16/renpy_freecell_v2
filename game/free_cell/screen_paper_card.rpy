# paper card to display
screen paper_card(card, size = "sm"):
    frame:
        # background Solid("#e92")
        xysize (CARD_WIDTH, CARD_HEIGHT)
        text card.name:
            xalign 0
            yalign 0
