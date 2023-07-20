# ゲームの準備をする
import pygame as pg, sys
import game_common
pg.init()
screen = pg.display.set_mode((800,600))
myrect = pg.Rect(100,100,100,150)

# この下をずっとループする
while True:
    # 画面を初期化する
    screen.fill(pg.Color("WHITE"))
    # 絵を描いたり判定したりする
    myrect.x = myrect.x + 1
    pg.draw.rect(screen, pg.Color("YELLOW"), myrect)
    # 画面を表示する
    game_common.showGame(pg, 60)
    # 閉じるボタンが押されたら終了する
    game_common.quitGame(pg, sys)