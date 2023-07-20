# ゲームの準備をする
import pygame as pg, sys
import game_common
pg.init()
screen = pg.display.set_mode((800,600))
img1 = pg.image.load("images/flower4.png")
img1 = pg.transform.scale(img1, (50, 50))
myrect = pg.Rect(100,100,50,50)

# この下をずっとループする
while True:
    # 画面を初期化する
    screen.fill(pg.Color("WHITE"))
    # 絵を描いたり判定したりする
    myrect.x = myrect.x + 1
    myrect.y = myrect.y - 1
    # pg.draw.rect(screen, pg.Color("YELLOW"), myrect)
    # 読み込んだ画像を描画する
    screen.blit(img1, myrect)
    # 画面を表示する
    game_common.showGame(pg, 60)
    # 閉じるボタンが押されたら終了する
    game_common.quitGame(pg, sys)