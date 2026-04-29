init python:
    def handle_drop_on_tableau_empty_cell(col = 0):
        def callback(drop, drags):
            # TODO:
            renpy.notify(drags[0].drag_name)

        return callback

    def check_tableau_card_draggable(col = 0, row = 0):
        # TODO:
        # 1. 检查是否是合法的一叠牌
        # 2. 检查是否有足够的空位
        return True

    # 当拖动一张纸牌时，把后面的牌也一起拖动
    # 考虑到 check_tableau_card_draggable 已经检查过了
    # 所以这里就不检查了，直接开始
    def handle_tableau_card_drag_joined(col = 0, row = 0):
        def callback(drag):
            join_list = [(drag, 0, 0)]
            # 1. 通过 col row 拿到后面的牌
            # 注意：这里是 row 是当前的 drag 所以 row + 1
            cards = game.piles[col][row + 1:]
            for i, card in enumerate(cards):
                # 然后因为要避让第一张牌，所以 (i + 1)
                y = (i + 1) * MINI_CARD_HEIGHT
                # 2. 通过牌遍历 drag.drag_group.children 找到 drag 对象
                for d in drag.drag_group.children:
                    if d.drag_name == card.name:
                        # 3. 加入到 join_list
                        join_list.append((d, 0, y))
            return join_list
        return callback

    def handle_tableau_card_dragged(card, col = 0, row = 0):
        def callback(drags, drop):
            if not drop:
                for i, drag in enumerate(drags):
                    x = game.xpos_of(col)
                    y = game.ypos_of(col, row + i)
                    drag.snap(x, y, delay = .2)
                return
            # TODO:
            # 1. 要通过 drop 来判断目标 col row
            # 2. 判断目标的类型
            # 可能的类型有：
            # - 原位置
            # - 桌面区
            # - 中转区 - 只考虑单张牌
            # - 回收区 - 只考虑单张牌
            # 3. 确认能否移动
            # 4. 变更数据
            return

        return callback

    def handle_tableau_card_snapped(col, row):
        # TODO:
        def callback(drag, x, y, completed):
            pass
        return callback


screen tableau_card(card, col = 0, row = 0):
    drag:
        drag_name card.name
        xpos game.xpos_of(col)
        ypos game.ypos_of(col, row)

        draggable check_tableau_card_draggable(col, row)
        dragged handle_tableau_card_dragged(card, col, row)
        snapped handle_tableau_card_snapped(col, row)
        drag_joined handle_tableau_card_drag_joined(col, row)

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
