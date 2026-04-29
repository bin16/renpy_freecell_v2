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

    def handle_freecell_card_dragged(card, col=12):
        """中转区单张牌的拖拽"""
        def callback(drags, drop):
            if not drop:
                for drag in drags:
                    x = game.xpos_of(col)
                    y = game.ypos_of(col)
                    drag.snap(x, y, delay=.2)
                return

            # 解析目标位置
            to_col = None

            empty_col = game.find_empty(drop.drag_name)
            if empty_col is not None:
                to_col = empty_col
            else:
                result = game.find_card(drop.drag_name)
                if result:
                    to_col = result[0]

            if to_col is not None and game.can_move_to([card], to_col):
                result = game.find_card(card.name)
                if result:
                    from_col, from_row = result
                    game.move_cards([card], from_col, from_row, to_col)
            else:
                for drag in drags:
                    x = game.xpos_of(col)
                    y = game.ypos_of(col)
                    drag.snap(x, y, delay=.2)
        return callback

    def handle_foundation_card_dragged(card, col=12):
        """回收区单张牌的拖拽"""
        def callback(drags, drop):
            if not drop:
                for drag in drags:
                    x = game.xpos_of(col)
                    y = game.ypos_of(col)
                    drag.snap(x, y, delay=.2)
                return

            # 回收区的牌只能移动到桌面区或中转区
            to_col = None

            empty_col = game.find_empty(drop.drag_name)
            if empty_col is not None:
                to_col = empty_col
            else:
                result = game.find_card(drop.drag_name)
                if result:
                    to_col = result[0]

            if to_col is not None and game.can_move_to([card], to_col):
                result = game.find_card(card.name)
                if result:
                    from_col, from_row = result
                    game.move_cards([card], from_col, from_row, to_col)
            else:
                for drag in drags:
                    x = game.xpos_of(col)
                    y = game.ypos_of(col)
                    drag.snap(x, y, delay=.2)
        return callback


screen free_cell_card(card, col=12):
    drag:
        draggable True
        drag_name card.name
        xpos game.xpos_of(col)
        ypos game.ypos_of(col)
        dragged handle_freecell_card_dragged(card, col)

        use paper_card(card)

screen free_cell_empty_cell(col=12):
    drag:
        draggable False
        drag_name ("FREE:%d" % col)
        xpos game.xpos_of(col)
        ypos game.ypos_of(col)

        dropped handle_drop_on_freecell(col)

        use empty_cell()
