# ゲームの準備をする
import pygame as pg, sys
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ROCKET_WIDTH = 50
ROCKET_HIGHT = 50
DEFAULT_ROCKET_X = 400
DEFAULT_ROCKET_Y = 500
DEFAULT_BULLET_X = 400
DEFAULT_BULLET_Y = -100
BULLET_WIDTH = 16
BULLET_HEIGHT = 16
UFO_WIDTH = 50
UFO_HEIGHT = 50

pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 自機データ
myimg = pg.image.load("images/myship.png")
myimg = pg.transform.scale(myimg, (ROCKET_WIDTH, ROCKET_HIGHT))
myrect = pg.Rect(DEFAULT_ROCKET_X, DEFAULT_ROCKET_Y, ROCKET_WIDTH, ROCKET_HIGHT)
# 弾データ
bulletimg = pg.image.load("images/bullet.png")
bulletimg = pg.transform.scale(bulletimg, (BULLET_WIDTH, BULLET_HEIGHT))
bulletrect = pg.Rect(DEFAULT_BULLET_X, DEFAULT_BULLET_Y, BULLET_WIDTH, BULLET_HEIGHT)
# UFOデータ
ufoimg = pg.image.load("images/UFO.png")
ufoimg = pg.transform.scale(ufoimg, (UFO_WIDTH, UFO_HEIGHT))
ufos = []
for i in range(10):
    ux = random.randint(0, 800)
    uy = -100 * i
    ufos.append(pg.Rect(ux, uy, UFO_WIDTH, UFO_HEIGHT))
# ボタンデータ
replay_img = pg.image.load("images/replaybtn.png")
# メインループで使う変数
pushFlag = False
page = 1


# ボタンを押したらnewpageにジャンプする
def button_to_jump(btn, newpage):
    global page, pushFlag
    # ユーザーからの入力を調べる
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    # 左クリックが押されたら
    if mdown[0]:
        pg.mixer.Sound("sounds/pi.wav").play()
        # ボタンがユーザーの入力範囲と衝突してかつプッシュフラグがfalseであった場合
        if btn.collidepoint(mx, my) and pushFlag == False:
            page = newpage
            pushFlag = True
    else:
        pushFlag = False


# ゲームステージ
def gamestage():
    # 画面を初期化する
    global vx, vy
    global page
    screen.fill(pg.Color("NAVY"))
    # ユーザーからの入力を調べる
    (mx, my) = pg.mouse.get_pos()
    mdown = pg.mouse.get_pressed()
    # ロケットの処理
    myrect.x = mx - ROCKET_WIDTH / 2
    screen.blit(myimg, myrect)
    # 弾の処理
    # 左クリックが押されてかつ弾の位置がスクリーンの頂点に達したら
    if mdown[0] and bulletrect.y < 0:
        bulletrect.x = myrect.x + ROCKET_WIDTH / 2 - BULLET_WIDTH / 2
        bulletrect.y = myrect.y
        pg.mixer.Sound("sounds/pi.wav").play()
    # 弾が一番上に達していなかったら
    if bulletrect.y >= 0:
        bulletrect.y += -30
        screen.blit(bulletimg, bulletrect)
    # UFOの処理
    for ufo in ufos:
        ufo.y += 10
        screen.blit(ufoimg, ufo)
        if ufo.y > SCREEN_HEIGHT:
            ufo.x = random.randint(0, SCREEN_WIDTH)
            ufo.y = -100
        # ロケットとUFOの衝突処理
        if ufo.colliderect(myrect):
            page = 2
            pg.mixer.Sound("sounds/down.wav").play()
        # 弾とUFOの衝突処理
        if ufo.colliderect(bulletrect):
            ufo.y = -100
            ufo.x = random.randint(0, 800)
            bulletrect.y = -100
            pg.mixer.Sound("sounds/piko.wav").play()


# データのリセット
def gamereset():
    myrect.x = 400
    myrect.y = 500
    bulletrect.y = -100
    for i in range(10):
        ufos[i] = pg.Rect(random.randint(0, 800), -100 * i, 50, 50)


# ゲームオーバー
def gameover():
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, (320, 480))
    button_to_jump(btn1, 1)


# ループ
while True:
    if page == 1:
        gamestage()
    if page == 2:
        gameover()
    pg.display.update()
    pg.time.Clock().tick(60)
    # 閉じるボタンが押されたら終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
