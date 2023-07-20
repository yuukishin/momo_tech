import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((800, 600))

img1 = pg.image.load("images/flower1.png")
img2 = pg.image.load("images/flower2.png")

def page1():
    screen.blit(img1, (0, 0))

def page2():
    screen.blit(img2, (0, 0))

page = 2

while True:
    if page == 1:
        page1()
    elif page == 2:
        page2()
    pg.display.update()
    pg.time.Clock().tick(60)    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
