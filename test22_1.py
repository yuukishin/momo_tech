# ゲームの準備をする
import pygame as pg, sys
import game_common

pg.init()
screen = pg.display.set_mode((800,600))

# この下をずっとループする
while True:
    # 画面を初期化する
    screen.fill(pg.Color("BLACK"))
    # ユーザーからの入力を調べる
    key = pg.key.get_pressed()
    if(key[pg.K_RIGHT]):
        print("RIGHT")
    if(key[pg.K_LEFT]):
        print("LEFT")
    # 画面を表示する
    game_common.showGame(pg, 60)
    # 閉じるボタンを押したら終了する
    game_common.quitGame(pg, sys)
