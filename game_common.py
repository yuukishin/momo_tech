# ゲームのセットアップをする
def setupGame(width, height):
    import pygame as pg, sys
    pg.init()
    screen = pg.display.set_mode((width, height))

# 画面を表示する
def showGame(pg, times):
    pg.display.update()
    # 1秒間にtimes以下のスピードにする
    pg.time.Clock().tick(times)


# 閉じるボタンが押されたら終了する
def quitGame(pg, sys):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
