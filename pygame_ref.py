import pygame as pg, sys

# ゲーム全体への命令

# ゲームの初期化
pg.init()
# ゲームの終了
pg.quit()
# プログラムを終了する
sys.exit()
# ゲーム用ウィンドウを作成する
screen = pg.display.set_mode((width, height))

# 図形を描写する

# 画面を塗りつぶす
screen.fill(color)
# 色を指定する
pg.Color("color_name")
# 四角形を描く
pg.draw.rect(screen, color, (x, y, width, height))
# 線を引く
pg.draw.line(screen, color, (x1, y1), (x2, y2), bold)
# 円を描く
pd.draw.ellipse(screen, color, (x, y, width, height), bold)

# 画像を描写する

# 画像を読み込む
img = pg.image.load("img_path")
# 画像を描画する
screen.blit(img_val, (x, y))
# 画像を描画して、その範囲を取得する
img_range = screen.blit(img_val, (x, y))
# 画像のサイズを変更する
img_range = pg.transform.scale(img_val, (width, height))
# 画像を上下左右判定する
img_val = pg.transform.flip(img_val,flip_x(bool),flip_y(bool))

# 文字を描画する
# フォントを準備する
font = pg.font.Font(None,font_size)
# 文字列の画像を作る
img_val = font.render("str",True,color)

# Rectを作る
val = pg.Rect(x,y,width,height)

# 時間を調整する
pg.time.Clock().tick("1秒間にこの回数以下のスピードにする")

# キーボード・マウスの入力を調べる
key_val = pg.key.get_pressed()

# 今、マウスボタンが押されているか調べる
mouse_val = pg.mouse.get_pressed()

# マウスがどこを指しているか調べる
(mx,my) = pg.mouse.get_pos()

# 衝突を判定する

# ある点(x,y)がrectAの範囲内にあるかを調べる
val(bool) = rectA.collidepoint(x,y)

# rectAとrectBが衝突しているかを調べる
val(bool) = rectA.colliderect(rectB)

# rectAがリストの中のどれかのrectと衝突しているかを調べる
val(list[num]) = rectA.collidelist(list)

# 音を鳴らす
pg.mixer.Sound("sound_file_path").play()
