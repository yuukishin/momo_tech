import pygame as pg, sys
import game_common

pg.init()
screen = pg.display.set_mode((800, 600))

while True:
    screen.fill(pg.Color("WHITE"))
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()

    # if mdown[0]:
    #     print(mx, my)
    if mdown[0]:
        pg.draw.rect(screen, pg.Color("BLUE"), (mx - 50, my - 50, 100, 100))
    game_common.showGame(pg, 100)
    game_common.quitGame(pg, sys)
