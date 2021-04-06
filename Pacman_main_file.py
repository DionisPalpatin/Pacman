import pygame as pg
import Pacman_library


pg.init()
Pacman_library.main_game.start_the_game()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()


    keys = pg.key.get_pressed()
    Pacman_library.main_game.player.move(keys)


    Pacman_library.main_game.drawing_the_figures()
    Pacman_library.main_game.clock.tick(Pacman_library.main_game.fps)