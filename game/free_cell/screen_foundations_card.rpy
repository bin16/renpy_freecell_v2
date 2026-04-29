screen foundations_card(card, col = 12):
    drag:
        draggable False
        drag_name ("foundations---CRAD_%d" % col)
        xpos game.xpos_of(col)
        ypos game.ypos_of(col)

        use paper_card(card)

screen foundations_empty_cell(col = 12):
    drag:
        draggable False
        drag_name ("foundations--EMPTY_%d" % col)
        xpos game.xpos_of(col)
        ypos game.ypos_of(col)

        use empty_cell()
