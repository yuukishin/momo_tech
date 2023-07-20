# ゲームの準備をする
import pygame as pg, sys
import random

# 変数宣言
SCREEN_WIDTH = 800
SCREEN_HIGHT = 600
BALL_WIDTH = 30
BALL_HIGHT = 30
BAR_WIDTH = 100
BAR_HEIGHT = 20

# 初期処理
pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))

# バーデータ
barrect = pg.Rect(SCREEN_WIDTH / 2, 500, BAR_WIDTH, BAR_HEIGHT)

# ボールデータ
ballimg = pg.image.load("images/kaeru.png")
ballimg = pg.transform.scale(ballimg, (BALL_WIDTH, BALL_HIGHT))
ballrect = pg.Rect(SCREEN_WIDTH / 2, 450, BALL_WIDTH, BALL_HIGHT)
# 移動量
vx = random.randint(-10, 10)
vy = -3


# ゲームステージ
def gamestage():
    # 画面を初期化する
    global vx, vy
    screen.fill(pg.Color("NAVY"))
    # ユーザーからの入力を調べる
    (mx, my) = pg.mouse.get_pos()
    # 絵を描いたり判定したりする
    # バーの処理
    # バーのx座標をマウスのユーザー入力にする
    barrect.x = mx
    pg.draw.rect(screen, pg.Color("CYAN"), barrect)
    # ボールの処理
    if ballrect.y < 0:
        vy = -vy
    if ballrect.x < 0 or ballrect.x > SCREEN_WIDTH - BALL_WIDTH:
        vx = -vx
    # ボールとバーの衝突判定
    if barrect.colliderect(ballrect):
        # x座標の移動量
        # ボールの中心に近いほど 0
        # ボールのx座標 > バーのx座標だと xは右方向にとぶ
        # ボールのx座標 < バーのx座標だと xは右方向にとぶ
        vx = ((ballrect.x + BALL_WIDTH / 2) - (barrect.x + BAR_WIDTH / 2)) / 4
        vy = random.randint(-7, -2)
        pg.mixer.Sound("sounds/pi.wav").play()
    ballrect.x += vx
    ballrect.y += vy
    screen.blit(ballimg, ballrect)

# メインループ
while True:
    gamestage()
    # 画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 閉じるボタンが押されたら終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
