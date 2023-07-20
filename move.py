import pygame as pg, sys
import test

pg.init()

screen = pg.display.set_mode((800, 600))
myrect = pg.Rect(100, 100, 100, 150)

while True:
    screen.fill(pg.Color("WHITE"))
    myrect.x = myrect.x + 1
    pg.draw.rect(screen, pg.Color("RED"), myrect)
    pg.display.update()
    pg.time.Clock().tick(60)
    test.quitGame(pg, sys)
