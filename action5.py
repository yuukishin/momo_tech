# ゲームの準備をする
import pygame as pg, sys
import random

pg.init()
screen = pg.display.set_mode((800, 600))
# プレイヤーデータ
myimgR = pg.image.load("images/playerR.png")
myimgR = pg.transform.scale(myimgR, (40, 50))
myimgL = pg.transform.flip(myimgR, True, False)
myrect = pg.Rect(50, 200, 40, 50)
# 壁データ
walls = [
    pg.Rect(0, 0, 800, 20),
    pg.Rect(0, 0, 20, 600),
    pg.Rect(780, 0, 20, 600),
    pg.Rect(0, 580, 800, 20),
]
# 罠データ
trapimg = pg.image.load("images/uni.png")
trapimg = pg.transform.scale(trapimg, (30, 30))
traps = []
for i in range(20):
    wx = 150 + i * 30
    wy = random.randint(20, 550)
    traps.append(pg.Rect(wx, wy, 30, 30))
# ボタンデータ
replay_img = pg.image.load("images/replaybtn.png")
# メインループで使う変数
rightFlag = True
pushFlag = False
page = 1


# ボタンを押したらnewpageにジャンプする
def button_to_jump(btn, newpage):
    global page, pushFlag
    # ユーザーからの入力を調べる
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint(mx, my) and pushFlag == False:
            # 効果音を鳴らす
            pg.mixer.Sound("sounds/pi.wav").play()
            page = newpage
            pushFlag = True
    else:
        pushFlag = False


# ゲームステージ
def gamestage():
    global rightFlag
    global page
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
    if myrect.collidelist(walls) != -1:
        myrect.x -= vx
        myrect.y -= vy
    if rightFlag:
        screen.blit(myimgR, myrect)
    else:
        screen.blit(myimgL, myrect)
    for wall in walls:
        pg.draw.rect(screen, pg.Color("BLACK"), wall)
    # 罠の処理
    for trap in traps:
        screen.blit(trapimg, trap)
    if myrect.collidelist(traps) != -1:
        pg.mixer.Sound("sounds/down.wav").play()
        page = 2


# データのリセット
def gamereset():
    myrect.x = 50
    myrect.y = 100
    for d in range(20):
        traps[d].x = 150 + d * 30
        traps[d].y = random.randint(20, 550)


# 　ゲームオーバー
def gameover():
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, (320, 480))
    # 絵を描いたり判定する
    button_to_jump(btn1, 1)


# この下をずっとループする
while True:
    if page == 1:
        gamestage()
    elif page == 2:
        gameover()
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
