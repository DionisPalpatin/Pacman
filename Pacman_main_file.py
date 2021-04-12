import pygame as pg
import Pacman_library


pg.init()
Pacman_library.main_game.drawing_the_figures()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()


    keys = pg.key.get_pressed()
    Pacman_library.main_game.move_player(keys)
    Pacman_library.main_game.drawing_the_figures()
    Pacman_library.main_game.clock.tick(Pacman_library.main_game.fps)