import pygame as pg


class Field():
    def __init__(self):
        self.matrix = list()
        with open(r"J:\Files\Homeworks\Pacman\New Text Document.txt") as file_map:
            for line in file_map:
                self.matrix.append(list(map(int, line.split())))
        self.sizes_main_game = (len(self.matrix), len(self.matrix[0]))
        self.width = 30
        self.screen = None


    def creating(self):
        self.screen = pg.display.set_mode((self.sizes_main_game[0] * self.width, self.sizes_main_game[1] * self.width))
        for y in range(self.sizes_main_game[0]):
            for x in range(self.sizes_main_game[1]):
                if self.matrix[y][x] == 1:
                    colour = (0, 0, 0)
                else:
                    colour = (255, 255, 0)
                pg.draw.rect(
                            self.screen, colour,
                            (x * self.width, y * self.width, self.width, self.width)
                            )
        pg.display.update()
    

class Enemy():
    def __init__(self):
        self.direction_x, self.direction_y = 0, 0
        self.x, self.y = 0, 0
        self.colour = (0, 0, 0)
    

class Game_process():
    def __init__(self, field, enemy, player):
        self.field = field
        self.enemy = enemy
        self.player = player


    def start_the_game(self):
        self.field.creating()


main_field = Field()
main_game = Game_process(main_field, None, None)
        