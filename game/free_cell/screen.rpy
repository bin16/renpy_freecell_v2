default game = FreeCellGame()

screen free_cell_game_screen():
    frame:
        xpadding 32
        ypadding 32
        xalign .5
        yalign .5
        xsize DESKTOP_WIDTH
        ysize DESKTOP_HEIGHT
        draggroup:
            # 中转区
            use empty_cell(8)
            use empty_cell(9)
            use empty_cell(10)
            use empty_cell(11)

            # 回收区
            use empty_cell(12)
            use empty_cell(13)
            use empty_cell(14)
            use empty_cell(15)

            # 桌面区
            for i, col in enumerate(game.piles[:8]):
                use empty_cell(i)

screen empty_cell(index = 0):
    drag:
        xpos game.xpos_of(index)
        ypos game.ypos_of(index)
        draggable False
        frame:
            xysize (CARD_WIDTH, CARD_HEIGHT)
            background Solid("#eee")
            text "[[     ]":
                xalign .5
                yalign .5
