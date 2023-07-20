# ゲームの準備をする
import pygame as pg,sys
pg.init()
screen = pg.display.set_mode((800,600))
next_img = pg.image.load("images/nextbtn.png")

while True:
    pushFlag = False
    screen.fill(pg.Color("WHITE"))
    btn = screen.blit(next_img,(350,200))
    
    # ユーザーからの入力を調べる
    mdown = pg.mouse.get_pressed()
    (mx,my) = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint(mx,my) and pushFlag == False:
            print("押した!!")
            pushFlag = True
    else:
        print("押していない")
        pushFlag = False

    pg.display.update()
    pg.time.Clock().tick(60)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            