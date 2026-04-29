# 纸牌 class
init python:
    class FreeCellGame:
        # 区域索引
        # 0-7  桌面区 (8列)
        # 8-11 回收区 (4堆)
        # 12-15 中转区 (4个格子)

        shuffle_count = 0

        def __init__(self):
            # 16个区域，每个区域是一个 list
            # 索引 0-7 桌面区，索引 8-11 回收区，索引 12-15 中转区
            self.piles = [[] for _ in range(16)]
            self.shuffle_count = 0
            self.shuffle()

        def shuffle(self):
            self.piles = [[] for _ in range(16)]
            cards = []
            for i in range (13):
                cards.append(Card(Card.HEARTS, 1 + i))
                cards.append(Card(Card.SPADES, 1 + i))
                cards.append(Card(Card.DIAMONDS, 1 + i))
                cards.append(Card(Card.CLUBS, 1 + i))
            renpy.random.shuffle(cards)
            self.piles[0] = cards[:7]
            self.piles[1] = cards[7:14]
            self.piles[2] = cards[14:21]
            self.piles[3] = cards[21:28]
            self.piles[4] = cards[28:34]
            self.piles[5] = cards[34:40]
            self.piles[6] = cards[40:46]
            self.piles[7] = cards[46:52]
            self.shuffle_count += 1
            renpy.retain_after_load()
            renpy.restart_interaction()

        def debug_quick_win(self):
            self.piles = [[] for _ in range(16)]
            for i in range (12):
                self.piles[8].append(Card(Card.HEARTS, 1 + i))
                self.piles[9].append(Card(Card.SPADES, 1 + i))
                self.piles[10].append(Card(Card.DIAMONDS, 1 + i))
                self.piles[11].append(Card(Card.CLUBS, 1 + i))
            self.piles[0] = [
                Card(Card.HEARTS, 13),
                Card(Card.SPADES, 13),
                Card(Card.DIAMONDS, 13),
                Card(Card.CLUBS, 13),
            ]
            self.shuffle_count += 1
            renpy.retain_after_load()
            renpy.restart_interaction()

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

        def card(self, col, row):
            return self.piles[col][row]

        # ========== 查找方法 ==========

        def find_card(self, card_name):
            """通过 card.name 查找纸牌位置，返回 (col, row) 或 None"""
            for col in range(16):
                for row, c in enumerate(self.piles[col]):
                    if c.name == card_name:
                        return (col, row)
            return None

        def find_empty(self, name):
            """通过空位的 drag_name（如 'FREE:12'）查找列索引，或 None"""
            # name 格式: "FREE:col"
            if name.startswith("FREE:"):
                try:
                    col = int(name[5:])
                    if 0 <= col < 16 and len(self.piles[col]) == 0:
                        return col
                except ValueError:
                    pass
            return None

        # ========== 空位数统计 ==========

        def count_empty_freecells(self):
            """中转区空位数"""
            return sum(1 for col in self.FREECELL_RANGE if len(self.piles[col]) == 0)

        def count_empty_tableau_cols(self):
            """桌面区空列数"""
            return sum(1 for col in self.TABLEAU_RANGE if len(self.piles[col]) == 0)

        def max_moveable_cards(self):
            """supermove 最多可移动的牌数"""
            return (self.count_empty_freecells() + 1) * (2 ** self.count_empty_tableau_cols())

        # ========== 序列合法性判断 ==========

        def is_valid_sequence(self, cards):
            """检查一叠牌是否合法：颜色交替、数字连续倒序"""
            if not cards:
                return True
            for i in range(len(cards) - 1):
                cur = cards[i]
                nxt = cards[i + 1]
                # 颜色必须不同（一个红一个黑）
                if cur.is_red() == nxt.is_red():
                    return False
                # 数字必须差 1（cur 比 nxt 大 1）
                if cur.number - nxt.number != 1:
                    return False
            return True

        def can_move_to(self, cards, target_col):
            """检查 cards（已验证为合法序列）能否移动到 target_col"""
            if not cards:
                return False

            # 桌面区
            if target_col in self.TABLEAU_RANGE:
                # 目标列空：检查 supermove 限制
                if len(self.piles[target_col]) == 0:
                    return len(cards) <= self.max_moveable_cards()
                # 目标列非空：最底部的牌必须与 cards[0] 颜色不同且数字差 1
                target_top = self.piles[target_col][-1]
                return (cards[0].is_red() != target_top.is_red() and
                        cards[0].num_diff(target_top) == 1)

            # 回收区：只接受单张牌
            if target_col in self.FOUNDATION_RANGE:
                if len(cards) != 1:
                    return False
                card = cards[0]
                # 目标堆为空：只能放 A（数字 1）
                if len(self.piles[target_col]) == 0:
                    return card.number == 1
                # 目标堆非空：花色相同且数字连续
                top = self.piles[target_col][-1]
                return card.suit == top.suit and card.number == top.number + 1

            # 中转区：只接受单张牌
            if target_col in self.FREECELL_RANGE:
                if len(cards) != 1:
                    return False
                return len(self.piles[target_col]) == 0

            return False

        def move_cards(self, cards, from_col, from_row, to_col):
            """将 cards 从 from_col:from_row 移动到 to_col，更新数据"""
            # 从原位置移除
            self.piles[from_col][from_row:from_row + len(cards)] = []
            # 追加到目标位置
            self.piles[to_col].extend(cards)

            renpy.retain_after_load()
            renpy.restart_interaction()

        # ========== 点击移动查找 ==========

        # 点击移动失败原因
        MOVE_NO_TARGET = 0
        MOVE_INVALID_SEQUENCE = 1
        MOVE_NO_SPACE = 2

        def find_click_move_target(self, card, col, row):
            """查找点击 card 后可以移动到的目标位置，按优先级返回 (to_col, reason) 或 (None, reason)"""
            cards = self.piles[col][row:]

            # 检查是否构成合法序列
            if not self.is_valid_sequence(cards):
                return (None, self.MOVE_INVALID_SEQUENCE)
            # 检查 supermove 限制
            if len(cards) > self.max_moveable_cards():
                return (None, self.MOVE_NO_SPACE)

            # 1. 回收区（只接受单张牌）
            if len(cards) == 1:
                for target_col in self.FOUNDATION_RANGE:
                    if self.can_move_to(cards, target_col):
                        return (target_col, None)

            # 2. 桌面区（堆叠到某张牌下面）
            for target_col in self.TABLEAU_RANGE:
                if len(self.piles[target_col]) > 0 and self.can_move_to(cards, target_col):
                    return (target_col, None)

            # 3. 桌面区空列
            for target_col in self.TABLEAU_RANGE:
                if len(self.piles[target_col]) == 0 and self.can_move_to(cards, target_col):
                    return (target_col, None)

            # 4. 中转区（只接受单张牌）
            if len(cards) == 1:
                for target_col in self.FREECELL_RANGE:
                    if self.can_move_to(cards, target_col):
                        return (target_col, None)

            return (None, self.MOVE_NO_TARGET)
