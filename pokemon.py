# ゲームの準備をする
import pygame as pg, sys
import random

pg.init()
screen = pg.display.set_mode((800, 600))

# 紙芝居
pokemon_images_links = []
for pokemon_images_link in range(20):
    pokemon_images_links.append(f"images/pokemon2/pokemon{pokemon_images_link}_R.png")
    # pokemon_images_links.append(f"images/pokemon/pokemon{pokemon_images_link}.jpg")

print(pokemon_images_links)

pokemon_images = []
for pokemon_image_link in pokemon_images_links:
    pokemon_image = pg.image.load(pokemon_image_link)
    pokemon_images.append(pokemon_image)

# ボタン
button_img = pg.image.load("images/nextbtn.png")
pushFlag = False
def button_to_jump(btn):
    global page, pushFlag
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint(mx, my) and pushFlag == False:
            page = random.randint(0, len(pokemon_images) - 1)
            pushFlag = True
    else:
        pushFlag = False


page = random.randint(0, len(pokemon_images) - 1)

while True:
    screen.fill(pg.Color("BLACK"))
    screen.blit(pokemon_images[page], (0, 0))
    button = screen.blit(button_img, (600, 540))
    button_to_jump(button)
    # 画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
