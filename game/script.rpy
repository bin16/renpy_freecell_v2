# 游戏在此开始。

define config.default_language = "english"

label start:
    call screen free_cell_game_screen()
    jump start
    # return
