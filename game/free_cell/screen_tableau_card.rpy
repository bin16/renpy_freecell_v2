init python:
    def handle_drop_on_tableau_empty_cell(col=0):
        def callback(drop, drags):
            result = game.find_card(drags[0].drag_name)
            if result is None:
                return
            from_col, from_row = result
            card = game.piles[from_col][from_row]

            # 尝试移动（单张牌）
            if game.can_move_to([card], col):
                game.move_cards([card], from_col, from_row, col)
                return
            else:
                # 归位
                for i, drag in enumerate(drags):
                    x = game.xpos_of(from_col)
                    y = game.ypos_of(from_col, from_row + i)
                    drag.snap(x, y, delay=.2)
        return callback

    def check_tableau_card_draggable(col=0, row=0):
        cards = game.piles[col][row:]
        if not cards:
            return False
        # 检查是否构成合法序列
        if not game.is_valid_sequence(cards):
            return False
        # 检查 supermove 限制
        if len(cards) > game.max_moveable_cards():
            return False
        return True

    def handle_tableau_card_drag_joined(col=0, row=0):
        def callback(drag):
            join_list = [(drag, 0, 0)]
            cards = game.piles[col][row + 1:]
            for i, card in enumerate(cards):
                y = (i + 1) * MINI_CARD_HEIGHT
                for d in drag.drag_group.children:
                    if d.drag_name == card.name:
                        join_list.append((d, 0, y))
                        break
            return join_list
        return callback

    def handle_tableau_card_dragged(card, col=0, row=0):
        def callback(drags, drop):
            if not drop:
                for i, drag in enumerate(drags):
                    x = game.xpos_of(col)
                    y = game.ypos_of(col, row + i)
                    drag.snap(x, y, delay=.2)
                return

            # 解析目标位置
            to_col = None
            cards = game.piles[col][row:]

            # 目标是否为空位
            empty_col = game.find_empty(drop.drag_name)
            if empty_col is not None:
                to_col = empty_col
            else:
                # 目标是否是牌（查找该牌所在位置）
                result = game.find_card(drop.drag_name)
                if result:
                    to_col = result[0]

            if to_col is None:
                return

            if game.can_move_to(cards, to_col):
                game.move_cards(cards, col, row, to_col)
                return
            else:
                # 归位
                for i, drag in enumerate(drags):
                    x = game.xpos_of(col)
                    y = game.ypos_of(col, row + i)
                    drag.snap(x, y, delay=.2)
        return callback

    def handle_tableau_card_snapped(col, row):
        def callback(drag, x, y, completed):
            if completed and hasattr(drag, '_click_move_target'):
                target_col = drag._click_move_target
                delattr(drag, '_click_move_target')
                cards = game.piles[col][row:]
                game.move_cards(cards, col, row, target_col)
        return callback

    def handle_tableau_card_clicked(card, col, row):
        def callback(drag):
            target_col, reason = game.find_click_move_target(card, col, row)
            if reason == game.MOVE_NO_SPACE:
                renpy.notify("空间不足")
                return
            if reason == game.MOVE_INVALID_SEQUENCE:
                renpy.notify("无法移动")
                return
            if target_col is None:
                renpy.notify("无处可放")
                return

            cards = game.piles[col][row:]
            # 标记 click-move 目标，snapped 中用于更新数据
            drag._click_move_target = target_col

            # 同时 snap 所有被移动的牌
            for i, c in enumerate(cards):
                for d in drag.drag_group.children:
                    if d.drag_name == c.name:
                        x = game.xpos_of(target_col)
                        y = game.ypos_of(target_col, len(game.piles[target_col]) + i)
                        d.snap(x, y, delay=.2)
                        break
        return callback


screen tableau_card(card, col=0, row=0):
    drag:
        drag_name card.name
        xpos game.xpos_of(col)
        ypos game.ypos_of(col, row)

        draggable check_tableau_card_draggable(col, row)
        dragged handle_tableau_card_dragged(card, col, row)
        snapped handle_tableau_card_snapped(col, row)
        drag_joined handle_tableau_card_drag_joined(col, row)
        clicked handle_tableau_card_clicked(card, col, row)

        use paper_card(card)

screen tableau_empty_cell(col=0):
    drag:
        draggable False
        drag_name ("FREE:%d" % col)
        xpos game.xpos_of(col)
        ypos game.ypos_of(col, 0)

        # if len(game.piles[col]) == 0:
        #     dropped handle_drop_on_tableau_empty_cell(col)

        use empty_cell()
