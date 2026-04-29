init python:
    def handle_drop_on_freecell(col=12):
        def callback(drop, drags):
            result = game.find_card(drags[0].drag_name)
            if result is None:
                return
            from_col, from_row = result
            card = game.piles[from_col][from_row]

            if game.can_move_to([card], col):
                game.move_cards([card], from_col, from_row, col)
                return
            else:
                for i, drag in enumerate(drags):
                    x = game.xpos_of(from_col)
                    y = game.ypos_of(from_col, from_row + i)
                    drag.snap(x, y, delay=.2)
        return callback

    def handle_drop_on_foundations(col=12):
        def callback(drop, drags):
            result = game.find_card(drags[0].drag_name)
            if result is None:
                return
            from_col, from_row = result
            card = game.piles[from_col][from_row]

            if game.can_move_to([card], col):
                game.move_cards([card], from_col, from_row, col)
                return
            else:
                for i, drag in enumerate(drags):
                    x = game.xpos_of(from_col)
                    y = game.ypos_of(from_col, from_row + i)
                    drag.snap(x, y, delay=.2)
        return callback


screen free_cell_card(card, col=12):
    drag:
        draggable False
        drag_name card.name
        xpos game.xpos_of(col)
        ypos game.ypos_of(col)

        use paper_card(card)

screen free_cell_empty_cell(col=12):
    drag:
        draggable False
        drag_name ("FREE:%d" % col)
        xpos game.xpos_of(col)
        ypos game.ypos_of(col)

        dropped handle_drop_on_freecell(col)

        use empty_cell()

screen foundations_card(card, col=12):
    drag:
        draggable False
        drag_name card.name
        xpos game.xpos_of(col)
        ypos game.ypos_of(col)

        use paper_card(card)

screen foundations_empty_cell(col=12):
    drag:
        draggable False
        drag_name ("FREE:%d" % col)
        xpos game.xpos_of(col)
        ypos game.ypos_of(col)

        dropped handle_drop_on_foundations(col)

        use empty_cell()
