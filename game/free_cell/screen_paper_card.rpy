# paper card to display
screen paper_card(card, size = "sm"):
    frame:
        background Solid("#e92")
        if size == "sm":
            xysize (CARD_WIDTH, MINI_CARD_HEIGHT)
        else:
            xysize (CARD_WIDTH, CARD_HEIGHT)
        text card.name:
            xalign .5
            yalign 0

# drag wrapper for paper card
# may create more wrapper for different zones
screen paper_card_wrapper(card, col_index = 0, row_index = 0):
    drag:
        drag_name ("CARD_%d_%d" % (col_index, row_index))
        xpos game.xpos_of(col_index)
        ypos game.ypos_of(col_index, row_index)
        use paper_card(card)
