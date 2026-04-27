# 纸牌 class
init python:
    class Card:
        # 花色索引
        HEARTS = 0    # ♥️ 红色
        DIAMONDS = 1 # ♦️ 红色
        CLUBS = 2    # ♣️ 黑色
        SPADES = 3   # ♠️ 黑色

        # 花色对应的 emoji
        SUIT_EMOJI = {HEARTS: "♥️", DIAMONDS: "♦️", CLUBS: "♣️", SPADES: "♠️"}
        # 花色对应的名称
        SUIT_NAME = {HEARTS: "hearts", DIAMONDS: "diamonds", CLUBS: "clubs", SPADES: "spades"}
        # 数字对应的名称
        NUMBER_NAME = {1: "A", 11: "J", 12: "Q", 13: "K"}

        def __init__(self, suit, number):
            self.suit = suit
            self.number = number

        def is_red(self):
            """是否是红色（红桃或方块）"""
            return self.suit in (Card.HEARTS, Card.DIAMONDS)

        @property
        def name(self):
            """返回 emoji + 数字，如 ♥️A、♠️10"""
            num_str = Card.NUMBER_NAME.get(self.number, str(self.number))
            return Card.SUIT_EMOJI[self.suit] + num_str

        def num_diff(self, other):
            """返回与另一张牌的数字差值（other.number - self.number）"""
            return other.number - self.number

    class FreeCellGame:
        # 区域索引
        # 0-7  桌面区 (8列)
        # 8-11 回收区 (4堆)
        # 12-15 中转区 (4个格子)

        def __init__(self):
            # 16个区域，每个区域是一个 list
            # 索引 0-7 桌面区，索引 8-11 回收区，索引 12-15 中转区
            self.piles = [[] for _ in range(16)]

        # 桌面区索引范围
        TABLEAU_RANGE = range(0, 8)
        # 回收区索引范围
        FOUNDATION_RANGE = range(8, 12)
        # 中转区索引范围
        FREECELL_RANGE = range(12, 16)

        def pos_of_card(col, i):
            if col < 7:
                # x: 128 is col or card width, 16 is gap
                # y: 64 is card height?
                return ((col * (128 + 16)), (200 + i * 64))
            elif col < 12:
                return (800 + (col - 8) * (128 + 16), 0)
            elif col < 16:
                return ((col - 12) * (128 + 16), 0)

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
