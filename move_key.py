import pygame as pg, sys
import test


pg.init()
screen = pg.display.set_mode((800, 600))
while True:
    screen.fill(pg.Color("WHITE"))
key = pg.key.get_pressed()
if key[pg.K_RIGHT]:
    print("RIGHT")
if key[pg.K_LEFT]:
    print("LEFT")
pg.display.update()
pg.time.Clock().tick(60)
test.quitGame(pg, sys)
