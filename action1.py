# ゲームの準備をする
import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((800, 600))
# プレイヤーデータ
myimgR = pg.image.load("images/playerR.png")
myimgR = pg.transform.scale(myimgR, (40, 50))
myimgL = pg.transform.flip(myimgR, True, False)
myrect = pg.Rect(50, 200, 40, 50)
# 障害物データ
boxrect = pg.Rect(300, 200, 100, 100)
# メインループで使う変数
rightFlag = True

# ゲームステージ
def gamestage():
    global rightFlag
    # 画面を初期化する
    screen.fill(pg.Color("DEEPSKYBLUE"))
    vx = 0
    vy = 0
    # ユーザーからの入力を調べる
    key = pg.key.get_pressed()
    # 絵を描いたり判定したりする
    if key[pg.K_RIGHT]:
        vx = 4
        rightFlag = True
    if key[pg.K_LEFT]:
        vx = -4
        rightFlag = False
    if key[pg.K_UP]:
        vy = -4
    if key[pg.K_DOWN]:
        vy = 4
    # プレイヤーの処理
    myrect.x += vx
    myrect.y += vy
    if rightFlag:
        screen.blit(myimgR, myrect)
    else:
        screen.blit(myimgL, myrect)
    # 障害物の処理
    pg.draw.rect(screen, pg.Color("DARKGREEN"), boxrect)

# この下をずっとループする
while True:
    gamestage()
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()