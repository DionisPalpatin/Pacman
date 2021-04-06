import pygame as pg
import Pacman_library


pg.init()
Pacman_library.main_game.start_the_game()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()