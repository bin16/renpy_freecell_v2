screen free_cell_card(card, col = 12):
    drag:
        drag_name ("FREE_CELL---CRAD_%d" % col)
        xpos game.xpos_of(col)
        ypos game.ypos_of(col)

        use paper_card(card)

screen free_cell_empty_cell(col = 12):
    drag:
        draggable False
        drag_name ("FREE_CELL--EMPTY_%d" % col)
        xpos game.xpos_of(col)
        ypos game.ypos_of(col)

        use empty_cell()
