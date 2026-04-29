# 纸牌的定义
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

