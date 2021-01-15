# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (800, 600)
prozor = pygamebg.open_window(sirina,visina,'Kutije')

# -*- acsection: main -*-

#fiksne vrednosti koje ćemo koristiti za pomeraj tačaka u crtanju pomoću petlje
ort_i = (30, 15) 
ort_j = (-50, 20)
ort_k = (0, -40)
#ove dve vrednosti nam pomažu prilikom dohvatanja elemenata torki 
X, Y = 0, 1

def crtaj_kutiju(A, h):
    #crtamo jednu kutiju vodeći računa da su nam sve definisane u odnosu na koordinate tačke A i veličinu h
    B = (A[X] - ort_j[X], A[Y] - ort_j[Y])
    C = (B[X] - ort_i[X], B[Y] - ort_i[Y])
    D = (A[X] - ort_i[X], A[Y] - ort_i[Y])
    A1 = (A[X] + h * ort_k[X], A[Y] + h * ort_k[Y])
    B1 = (B[X] + h * ort_k[X], B[Y] + h * ort_k[Y])
    C1 = (C[X] + h * ort_k[X], C[Y] + h * ort_k[Y])
    D1 = (D[X] + h * ort_k[X], D[Y] + h * ort_k[Y])
    pg.draw.polygon(prozor, pg.Color("Brown"), [A, D, D1, A1])
    pg.draw.polygon(prozor, pg.Color("Yellow"), [A, B, B1, A1])
    pg.draw.polygon(prozor, pg.Color("Khaki"), [A1, B1, C1, D1])

#broj kutija u spoljnem sloju 
broj_kutija=5

#glavna petlja programa u kojoj ponavljamo jednu kutiju broj puta definišemo pomoću broj_kutija
for red in range(broj_kutija):
    for kol in range(broj_kutija - red):
        x = sirina // 2 + red * ort_j[X] + kol * ort_i[X] #određujemo x koordinatu tačke A
        y = 2*visina // 3 + red * ort_j[Y] + kol * ort_i[Y] #određujemo y koordinatu tačke A
        h = max(broj_kutija - red - kol, 0) 
        crtaj_kutiju((x, y), h)


# -*- acsection: after-main -*-

pygamebg.wait_loop()
