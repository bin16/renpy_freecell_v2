screen foundations_card(card, col=12):
    drag:
        draggable True
        drag_name card.name
        xpos game.xpos_of(col)
        ypos game.ypos_of(col)
        dragged handle_foundation_card_dragged(card, col)

        use paper_card(card)

screen foundations_empty_cell(col=12):
    drag:
        draggable False
        drag_name ("FREE:%d" % col)
        xpos game.xpos_of(col)
        ypos game.ypos_of(col)

        dropped handle_drop_on_foundations(col)

        use empty_cell()
