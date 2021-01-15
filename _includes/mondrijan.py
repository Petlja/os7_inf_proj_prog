
# -*- acsection: general-init -*-

#uključujemo biblioteku pygame i pygamebg 
import pygame as pg
import pygamebg

#otvaramo prozor
sirina, visina = 820, 820
prozor = pygamebg.open_window(sirina,visina,'Mondrijan')

# -*- acsection: main -*-

#bojimo pozadinu
prozor.fill(pg.Color('black'))

#definišemo boje koje ćemo koristiti
crvena = (173,12,4)
bela = (230,221,214)
plava = (0,17,107)
zuta = (234, 170,0)

#crtamo pravougaonike
pg.draw.rect(prozor, crvena, (210, 0, 610, 600))
pg.draw.rect(prozor, bela, (0, 0, 195, 230))
pg.draw.rect(prozor, bela, (0, 260, 195, 340))
pg.draw.rect(prozor, plava, (0, 615, 195, 205))
pg.draw.rect(prozor, bela, (210, 615, 560, 205))
pg.draw.rect(prozor, bela, (790, 615, 30, 100))
pg.draw.rect(prozor, zuta, (790, 740, 30, 90))

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
