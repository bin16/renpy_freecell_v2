# 使用 renpy 实现空当接龙的尝试

## 引擎与交互

### 点击移动

点击一张牌时，优先考虑能否放进回收区，其次能否放在桌面区的某张牌下面，其次看能否放在桌面区的空位，最后看能不能放在回收区。

### 拖拽与点击

```renpy
init python:
    handle_card_drop(drags, drop):
        if not drop:
            # 纸牌归位
            drags[0].snap(drags[0].start_x, drags[0].start_y)
            # 注意：对于拖拽一叠牌的情况下，也要归位其他纸牌
            # 注意：使用 drag_joined 跟随移动的纸牌，他们的 start_x start_y 是 0
            pass
        # 变更纸牌的位置
        return

    # 当点击一张纸牌
    handle_card_tap(drag):
        # 只有当纸牌位于某个队列的末尾的时候，才响应点击行为
        # 顺序查找可以移动的目标位置
        # 移动纸牌或者给出提示
        # 对于回收区，不响应点击，只允许拖动
        pass

    # 这个函数，用于查找这张牌「后面」的牌
    # 用于一次移动一整叠牌
    handle_card_joined(drag):
        joined_list = [(drag, 0, 0)]
        # TODO: 查找后面的牌，按照顺序排列，注意 y 的偏移
        return joined_list

screen deck:
    # draggroup 的子元素只可以是 drag
    # 对于不能参与互动的纸牌，禁用它的 draggable
    draggroup:
        drag:
            drag_name "s:1"
            xpos 100
            ypos 100

            draggable True # 对于不能移动的牌，设置为 False
            drag_raise False # 对于移动一整叠牌的时候，似乎不太需要这样做
            dragged handle_card_drop
            drag_joined handle_card_joined
            clicked handle_card_tap

            frame:
                xsize 100
                ysize 100
                background Solid("#eee")
                text "♠️A":
                    xalign .5
                    yalign .5
```

### 数据管理

理论上，需要一个全局的 object 存储所有纸牌的位置关系，然后计算 x y 布置 drag 元素。
