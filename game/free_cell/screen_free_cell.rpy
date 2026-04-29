init python:
    # TODO: delete
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
                for drag in drags:
                    x = game.xpos_of(from_col)
                    y = game.ypos_of(from_col)
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

    def handle_freecell_card_snapped(card, col=12):
        def callback(drag, x, y, completed):
            if completed and hasattr(drag, '_click_move_target'):
                target_col = drag._click_move_target
                delattr(drag, '_click_move_target')
                result = game.find_card(card.name)
                if result:
                    from_col, from_row = result
                    game.move_cards([card], from_col, from_row, target_col)
        return callback

    def handle_freecell_card_clicked(card, col=12):
        def callback(drag):
            result = game.find_card(card.name)
            if result is None:
                return
            from_col, from_row = result
            target_col, reason = game.find_click_move_target(card, from_col, from_row)
            if reason == game.MOVE_NO_SPACE:
                renpy.notify("空间不足")
                return
            if reason == game.MOVE_INVALID_SEQUENCE:
                renpy.notify("无法移动")
                return
            if target_col is None:
                renpy.notify("无处可放")
                return
            drag._click_move_target = target_col
            x = game.xpos_of(target_col)
            y = game.ypos_of(target_col)
            drag.snap(x, y, delay=.2)
        return callback


screen free_cell_card(card, col=12):
    drag:
        id ("game_%s_free_cell_%s_%s" % (str(game.shuffle_count), str(card.suit), str(card.number)))
        draggable True
        drag_name card.name
        xpos game.xpos_of(col)
        ypos game.ypos_of(col)
        dragged handle_freecell_card_dragged(card, col)
        snapped handle_freecell_card_snapped(card, col)
        clicked handle_freecell_card_clicked(card, col)

        use paper_card(card)

screen free_cell_empty_cell(col=12):
    drag:
        draggable False
        drag_name ("FREE:%d" % col)
        xpos game.xpos_of(col)
        ypos game.ypos_of(col)

        # dropped handle_drop_on_freecell(col)

        use empty_cell()
