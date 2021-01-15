
# -*- acsection: general-init -*-

#uključujemo biblioteku pygame i pygamebg 
import pygame as pg
import pygamebg

#otvaramo prozor
sirina, visina = 410, 410
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
pg.draw.rect(prozor, crvena, (105, 0, 305, 300))
pg.draw.rect(prozor, bela, (0, 0, 97, 115))
pg.draw.rect(prozor, bela, (0, 130, 97, 170))
pg.draw.rect(prozor, plava, (0, 307, 97, 102))
pg.draw.rect(prozor, bela, (105, 307, 277, 102))
pg.draw.rect(prozor, bela, (390, 307, 20, 50))
pg.draw.rect(prozor, zuta, (390, 365, 20, 45))

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
