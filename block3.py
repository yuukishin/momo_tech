# ゲームの準備をする
import pygame as pg, sys
import random

# 変数宣言
SCREEN_WIDTH = 800
SCREEN_HIGHT = 600
DEFAULT_BALL_POSITON_X = 400
DEFAULT_BALL_POSITON_Y = 450
DEFAULT_BAR_POSITON_X = 400
DEFAULT_BAR_POSITON_Y = 500

BALL_WIDTH = 30
BALL_HIGHT = 30
BAR_WIDTH = 100
BAR_HEIGHT = 20

# 初期処理
pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
# バーデータ
barrect = pg.Rect(DEFAULT_BAR_POSITON_X, DEFAULT_BAR_POSITON_Y, BAR_WIDTH, BAR_HEIGHT)
# ボールデータ
ballimg = pg.image.load("images/kaeru.png")
ballimg = pg.transform.scale(ballimg, (BALL_WIDTH, BALL_HIGHT))
ballrect = pg.Rect(
    DEFAULT_BALL_POSITON_X, DEFAULT_BALL_POSITON_Y, BALL_WIDTH, BALL_HIGHT
)
# ボタンデータ
replay_img = pg.image.load("images/replaybtn.png")

# ブロックデータ
blocks = []
for yy in range(4):
    for xx in range(7):
        blocks.append(pg.Rect(50 + xx * 100, 40 + yy * 50, 80, 30))

# メインループで使う変数
pushFlag = False
page = 1
score = 0

# 移動量
vx = random.randint(-10, 10)
vy = -5


# ボタンジャンプ関数
def button_to_jump(btn, newpage):
    global page, pushFlag
    # ユーザーからの入力を調べる
    mdown = pg.mouse.get_pressed()
    # マウスの位置座標を取得
    (mx, my) = pg.mouse.get_pos()
    # 左クリックが押された際に
    if mdown[0]:
        if btn.collidepoint(mx, my) and pushFlag == False:
            pg.mixer.Sound("sounds/pi.wav").play()
            page = newpage
            pushFlag = True
    else:
        pushFlag = False


# ゲームステージ
def gamestage():
    # 画面を初期化する
    global vx, vy
    global page
    global score
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
    if ballrect.x < 0 or ballrect.x > 800 - 30:
        vx = -vx
    # ボールとバーの衝突判定
    if barrect.colliderect(ballrect):
        # x座標の移動量
        # ボールの中心に近いほど 0
        # ボールのx座標 > バーのx座標だと xは右方向にとぶ
        # ボールのx座標 < バーのx座標だと xは右方向にとぶ
        vx = ((ballrect.x + 30 / 2) - (barrect.x + 100 / 2)) / 4
        vy = random.randint(-7, -2)
        pg.mixer.Sound("sounds/pi.wav").play()
    if ballrect.y > 600:
        page = 2
        pg.mixer.Sound("sounds/pon.wav").play()
    ballrect.x += vx
    ballrect.y += vy
    screen.blit(ballimg, ballrect)
    # ブロックの処理
    n = 0
    for block in blocks:
        pg.draw.rect(screen, pg.Color("GOLD"), block)
        # ブロックとボールが衝突したらボールを跳ね返してブロックを消す
        if block.colliderect(ballrect):
            pg.mixer.Sound("sounds/piko.wav").play()
            vy = -vy
            blocks[n] = pg.Rect(0, 0, 0, 0)
            score += 1
            if score == 28:
                pg.mixer.Sound("sounds/up.wav").play()
                page = 3
        n += 1


# データのリセット
def gamereset():
    global vx, vy
    global score
    global blocks
    vx = random.randint(-10, 10)
    vy = -5
    ballrect.x = DEFAULT_BALL_POSITON_X
    ballrect.y = DEFAULT_BAR_POSITON_Y
    score = 0
    blocks = []
    for yy in range(4):
        for xx in range(7):
            blocks.append(pg.Rect(xx * 100 + 50, yy * 50 + 40, 80, 30))


# ゲームクリア
def gameclear():
    gamereset()
    screen.fill(pg.Color("GOLD"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMECLEAR", True, pg.Color("RED"))
    screen.blit(text, (60, 200))
    btn1 = screen.blit(replay_img, (320, 400))
    button_to_jump(btn1, 1)


# ゲームオーバー
def gameover():
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, (320, 480))
    button_to_jump(btn1, 1)


# メインループ
while True:
    if page == 1:
        gamestage()
    elif page == 2:
        gameover()
    elif page == 3:
        gameclear()
    # 画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 閉じるボタンが押されたら終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
