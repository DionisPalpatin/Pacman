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


class Player():
    def __init__(self):
        self.speed = 1
        self.x, self.y = 0, 0
        

class Game_process():
    def __init__(self, field, enemy, player):
        self.field = field
        self.enemy = enemy
        self.player = player
        self.fps = 60
        self.clock = pg.time.Clock()


    def start_the_game(self):
        self.field.creating()


    def drawing_the_figures(self):
        self.start_the_game()
        pg.draw.circle(
                    self.field.screen, (100, 100, 100),
                    (self.player.x, self.player.y), self.field.width // 2
                    )
        # pg.draw.circle(
        #             self.field.screen, (0, 0, 0),
        #             (self.enemy.x, self.enemy.y), self.field.width // 2
        #             )
        pg.display.update()


    def check_move(self):
        cell_player_x = self.player.x // self.field.width + 1
        cell_player_y = self.player.y // self.field.width + 1
        self.field.matrix[cell_player_y][cell_player_x] = "p"
        if  


    def move_player(self, keys):
        if keys[pg.K_w]:
            self.y -= self.speed
        if keys[pg.K_s]:
            self.y += self.speed
        if keys[pg.K_d]:
            self.x += self.speed
        if keys[pg.K_a]:
            self.x -= self.speed


main_field = Field()
player = Player()
player.x = main_field.sizes_main_game[0] * main_field.width // 2
player.y = main_field.sizes_main_game[1] * main_field.width // 2
main_game = Game_process(main_field, None, player)
        