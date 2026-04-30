default game = FreeCellGame()

screen free_cell_game_screen():
    frame:
        id ("free_cell_%s" % str(game.shuffle_count))
        background Solid("#44891a")
        xpadding 32
        ypadding 32
        xalign .5
        yalign .5
        xsize DESKTOP_WIDTH
        ysize DESKTOP_HEIGHT
        draggroup:
            id "free_cell_draggroup"

            # 中转区（索引 12-15）
            for col in range(12, 16):
                use free_cell_empty_cell(col)
                if game.piles[col]:
                    use free_cell_card(game.piles[col][-1], col)

            # 回收区（索引 8-11）
            for col in range(8, 12):
                use foundations_empty_cell(col)
                if game.piles[col]:
                    for row, card in enumerate(game.piles[col]):
                        use foundations_card(card, col, row) id ("F_%d:%d_%d:%s" % (game.shuffle_count, col, row, card.name))

            # 桌面区
            for i, col in enumerate(game.piles[:8]):
                use tableau_empty_cell(i)
                if col:
                    for j, card in enumerate(col):
                        use tableau_card(card, i, j)

            if game.is_won():
                drag:
                    draggable False
                    droppable False
                    xpos 0
                    ypos 900
                    frame:
                        background Frame("panel.png", 12, 12)
                        hbox:
                            label "你胜利了！":
                                text_size 26
                            imagebutton:
                                idle "new_game_button_idle"
                                hover "new_game_button_hover"
                                action [
                                    Function(game.shuffle),
                                    Return(),
                                ]
            else:
                # 调试信息
                drag:
                    draggable False
                    droppable False
                    xpos 0
                    ypos 900
                    frame:
                        background Frame("panel.png", 12, 12)
                        xalign .5
                        yalign 1.0
                        vbox:
                            spacing 4
                            hbox:
                                spacing 4
                                # label "桌面区"
                                # for col in game.piles[:8]:
                                #     text "%d" % len(col)
                                # label "中转区"
                                # for col in game.piles[12:16]:
                                #     text "%d" % len(col)
                                # label "回收区"
                                # for col in game.piles[8:12]:
                                #     text "%d" % len(col)

                                imagebutton:
                                    idle "new_game_button_idle"
                                    hover "new_game_button_hover"
                                    action [
                                        Function(game.shuffle),
                                        Return(),
                                    ]

                                imagebutton:
                                    idle "restart_button_idle"
                                    hover "restart_button_hover"
                                    action [
                                        Function(game.restart),
                                        Return(),
                                    ]

                                # textbutton _("新游戏｜随机"):
                                #     action Function(game.shuffle)
                                # textbutton "DEBUG 快速胜利":
                                #     text_size 24
                                #     action [
                                #         Function(game.debug_quick_win),
                                #         Return(),
                                #     ]
                                # text "shuffle_count: [game.shuffle_count]"

image new_game_button_idle:
    "new_game_button-hover-sheet.png"
    crop (0, 140*3, 150, 42)

image new_game_button_hover:
    "new_game_button-hover-sheet.png"
    crop (0, 0, 150, 42)
    pause .05
    crop (0, 42, 150, 42)
    pause .05
    crop (0, 42*2, 150, 42)
    pause .05
    crop (0, 42*3, 150, 42)
    pause .05
    crop (0, 42*4, 150, 42)
    pause .05
    crop (0, 42*5, 150, 42)
    pause .05
    crop (0, 42*6, 150, 42)
    pause .05
    crop (0, 42*7, 150, 42)
    pause .05
    crop (0, 42*8, 150, 42)
    pause .05
    crop (0, 42*9, 150, 42)
    pause .05
    crop (0, 42*10, 150, 42)
    pause .05
    repeat

image restart_button_idle:
    "restart_button-hover-sheet.png"
    crop (0, 0, 108, 42)

image restart_button_hover:
    "restart_button-hover-sheet.png"
    crop (0, 0, 108, 42)
    pause .05
    crop (0, 42, 108, 42)
    pause .05
    crop (0, 42*2, 108, 42)
    pause .05
    crop (0, 42*3, 108, 42)
    pause .05
    crop (0, 42*4, 108, 42)
    pause .05
    crop (0, 42*5, 108, 42)
    pause .05
    crop (0, 42*6, 108, 42)
    pause .05
    crop (0, 42*7, 108, 42)
    pause .05
    crop (0, 42*8, 108, 42)
    pause .05
    crop (0, 42*9, 108, 42)
    pause .05
    crop (0, 42*10, 108, 42)
    pause .05
    repeat
