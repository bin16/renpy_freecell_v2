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
            use free_cell_empty_cell(8)
            use free_cell_empty_cell(9)
            use free_cell_empty_cell(10)
            use free_cell_empty_cell(11)

            # 回收区
            use foundations_empty_cell(12)
            use foundations_empty_cell(13)
            use foundations_empty_cell(14)
            use foundations_empty_cell(15)

            # 桌面区
            for i, col in enumerate(game.piles[:8]):
                use tableau_empty_cell(i)
                if col and len(col) > 0:
                    for j, card in enumerate(col):
                        # 第 i 列，第 j 张纸牌
                        use tableau_card(card, i, j)

            use demo_card()
