init python:
    def handle_drop_on_tableau_empty_cell(col = 0):
        def callback(drop, drags):
            # TODO:
            renpy.notify(drags[0].drag_name)

        return callback

    def handle_drag_tableau_card(card, col = 0, row = 0):
        def callback(drags, drop):
            if not drop:
                drags[0].snap(drags[0].start_x, drags[0].start_y)
                return
            return

screen tableau_card(card, col = 0, row = 0):
    drag:
        drag_name ("CRAD_%d_%d" % (col, row))
        xpos game.xpos_of(col)
        ypos game.ypos_of(col, row)

        dragged handle_drag_tableau_card(card, col, row)

        use paper_card(card)

screen tableau_empty_cell(col = 0, row = 0):
    drag:
        draggable False
        drag_name ("TABLEAU_CELL_%d" % col)
        xpos game.xpos_of(col)
        ypos game.ypos_of(col, row)

        if len(game.piles[col]) == 0:
            dropped handle_drop_on_tableau_empty_cell(col)

        use empty_cell()
