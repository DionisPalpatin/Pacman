import pygame as pg


class Field():
    def __init__(self):
        self.matrix = list()
        with open(r"J:\Files\Homeworks\Pacman\New Text Document.txt") as file_map:
            for line in file_map:
                self.matrix.append(list(map(int, line.split())))
        self.sizes_main_game = (len(self.matrix), len(self.matrix[0]))
        self.width = 50
        self.screen = None


    def creating(self):
        self.screen = pg.display.set_mode((self.sizes_main_game[0] * self.width, self.sizes_main_game[1] * self.width))
        for y in range(self.sizes_main_game[0]):
            for x in range(self.sizes_main_game[1]):
                if self.matrix[y][x] != 0:
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
        self.speed = 3
        self.x, self.y = 0, 0
        self.rad = 0
        self.has_moved = False
        self.cell_x, self.cell_y = 0, 0
        

class Game_process():
    def __init__(self, field, enemy, player):
        self.field = field
        self.enemy = enemy
        self.player = player
        self.fps = 60
        self.clock = pg.time.Clock()


    def drawing_the_figures(self):
        self.field.creating()
        pg.draw.circle(
                    self.field.screen, (100, 100, 100),
                    (self.player.x, self.player.y), self.player.rad
                    )
        # pg.draw.circle(
        #             self.field.screen, (0, 0, 0),
        #             (self.enemy.x, self.enemy.y), self.field.width // 2
        #             )
        self.player.has_moved = False
        pg.display.update()


    def move_player(self, keys):
        self.player.cell_x = self.player.x // self.field.width
        self.player.cell_y = self.player.y // self.field.width
        distans_up = self.player.y - self.player.cell_y * self.field.width
        distans_down = (self.player.cell_y + 1) * self.field.width - self.player.y
        distans_right = (self.player.cell_x + 1) * self.field.width - self.player.x
        distans_left = self.player.x - self.player.cell_x * self.field.width


        if keys[pg.K_w]:
            if self.field.matrix[self.player.cell_y - 1][self.player.cell_x] == 1:
                if distans_up - self.player.rad > self.player.speed:
                    self.player.y -= self.player.speed
                else:
                    self.player.y -= distans_up - self.player.rad
            elif self.player.rad < distans_up or distans_right >= self.player.rad <= distans_left:
                self.player.y -= self.player.speed
            else:
                self.player.y -= self.player.rad - distans_up
            self.player.has_moved = True
        if keys[pg.K_s]:
            if self.field.matrix[self.player.cell_y + 1][self.player.cell_x] == 1:
                if distans_down - self.player.rad > self.player.speed:
                    self.player.y += self.player.speed
                else:
                    self.player.y += distans_down - self.player.rad
            elif self.player.rad < distans_down or distans_right >= self.player.rad <= distans_left:
                self.player.y += self.player.speed
            else:
                self.player.y += self.player.rad - distans_down
            self.player.has_moved = True
        if keys[pg.K_a]:
            if self.field.matrix[self.player.cell_y][self.player.cell_x - 1] == 1:
                if distans_left - self.player.rad > self.player.speed:
                    self.player.x -= self.player.speed
                else:
                    self.player.x -= distans_left - self.player.rad
            elif self.player.rad < distans_left or distans_down >= self.player.rad <= distans_up:
                self.player.x -= self.player.speed
            else:
                self.player.x -= self.player.rad - distans_left
            self.player.has_moved = True
        if keys[pg.K_d]:
            if self.field.matrix[self.player.cell_y][self.player.cell_x + 1] == 1:
                if distans_right - self.player.rad > self.player.speed:
                    self.player.x += self.player.speed
                else:
                    self.player.x += distans_right - self.player.rad
            elif self.player.rad < distans_right or distans_down >= self.player.rad <= distans_up:
                self.player.x += self.player.speed
            else:
                self.player.x += self.player.rad - distans_right
            self.player.has_moved = True
                


main_field = Field()
player = Player()
player.x = main_field.sizes_main_game[0] * main_field.width // 2
player.y = main_field.sizes_main_game[1] * main_field.width // 2
player.cell_x = player.x // main_field.width
player.cell_y = player.y // main_field.width
player.rad = 10 
main_field.matrix[player.y // main_field.width][player.x // main_field.width]
main_game = Game_process(main_field, None, player)
        