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
            # 中转区（索引 12-15）
            for col in range(12, 16):
                if game.piles[col]:
                    use free_cell_card(game.piles[col][-1], col)
                else:
                    use free_cell_empty_cell(col)

            # 回收区（索引 8-11）
            for col in range(8, 12):
                if game.piles[col]:
                    use foundations_card(game.piles[col][-1], col)
                else:
                    use foundations_empty_cell(col)

            # 桌面区
            for i, col in enumerate(game.piles[:8]):
                use tableau_empty_cell(i)
                if col:
                    for j, card in enumerate(col):
                        use tableau_card(card, i, j)

            # 调试信息
            drag:
                draggable False
                droppable False
                xpos 20
                ypos 800
                frame:
                    xalign .5
                    yalign 1.0
                    vbox:
                        spacing 4
                        hbox:
                            spacing 4
                            label "桌面区"
                            for col in game.piles[:8]:
                                text "%d" % len(col)
                        hbox:
                            spacing 4
                            label "中转区"
                            for col in game.piles[12:16]:
                                text "%d" % len(col)
                        hbox:
                            spacing 4
                            label "回收区"
                            for col in game.piles[8:12]:
                                text "%d" % len(col)
