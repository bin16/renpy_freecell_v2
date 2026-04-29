# 纸牌 class
init python:
    class FreeCellGame:
        # 区域索引
        # 0-7  桌面区 (8列)
        # 8-11 回收区 (4堆)
        # 12-15 中转区 (4个格子)

        def __init__(self):
            # 16个区域，每个区域是一个 list
            # 索引 0-7 桌面区，索引 8-11 回收区，索引 12-15 中转区
            self.piles = [[] for _ in range(16)]
            self.piles[1] = [
                Card(Card.DIAMONDS, 2),
                Card(Card.DIAMONDS, 1),
            ]
            self.piles[2] = [
                Card(Card.HEARTS, 2),
                Card(Card.HEARTS, 1),
            ]

        # 桌面区索引范围
        TABLEAU_RANGE = range(0, 8)
        # 回收区索引范围
        FOUNDATION_RANGE = range(8, 12)
        # 中转区索引范围
        FREECELL_RANGE = range(12, 16)

        def xpos_of(self, col_index):
            if col_index < 8:
                return TABLEAU_LEFT + col_index * (CARD_WIDTH + GAP)
            elif col_index < 12:
                return FOUNDATION_LEFT + (col_index - 8) * (CARD_WIDTH + GAP)
            else:
                return FREE_CELL_LEFT + (col_index - 12) * (CARD_WIDTH + GAP)

        def ypos_of(self, col_index, row_index = 0):
            if col_index < 8:
                return TABLEAU_TOP + MINI_CARD_HEIGHT * row_index
            elif col_index < 12:
                return PADDING
            else:
                return PADDING
