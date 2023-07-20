# ゲームの準備をする
# import pygame as pg, sys

# pg.init()
# pg.font.init()
# screen = pg.display.set_mode((800, 600))
# # img1 = pg.image.load("images/car.png")
# # img1 = pg.transform.scale(img1,(50,50))
# font = pg.font.Font(None, 50)
# textimg = font.render("hello!", True, pg.Color("BLUE"))


def quitGame(pg,sys):
    # 閉じるボタンが押されたら、終了する
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()


# # この下をずっとループする
# while True:
#     # 画面を初期化する
#     screen.fill(pg.Color("BLACK"))
#     # 絵を描いたり判定する
#     screen.blit(textimg, (200, 100))
#     # 画面を表示する
#     pg.display.update()
#     # ゲームを終了する
#     quitGame(pg)
