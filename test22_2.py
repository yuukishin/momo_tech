import pygame as pg, sys
import game_common

pg.init()
screen = pg.display.set_mode((800, 600))
imageR = pg.image.load("images/playerR.png")
myrect = pg.Rect(300, 200, 80, 100)

while True:
    screen.fill(pg.Color("WHITE"))
    vx = 0
    vy = 0
    key = pg.key.get_pressed()
    if key[pg.K_RIGHT]:
        vx = 5
    if key[pg.K_UP]:
        vy = -5
    if key[pg.K_DOWN]:
        vy = 5
    if key[pg.K_LEFT]:
        vx = -5
    myrect.x = myrect.x + vx
    myrect.y = myrect.y + vy
    screen.blit(imageR, myrect)
    game_common.showGame(pg, 100)
    game_common.quitGame(pg, sys)
