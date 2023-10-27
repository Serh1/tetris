from settings import *
import math
from tetromino import Tetromino
import pygame.freetype as ft


class Text:
    def __init__(self, app):
        self.app = app
        self.font = ft.SysFont(None, 24)

    def draw(self):
        self.font.render_to(self.app.screen, (WIN_W * 0.610, WIN_H * 0.02),
                            text='TETRIS', fgcolor='white',
                            size=TILE_SIZE*1.65)
        self.font.render_to(self.app.screen, (WIN_W * 0.610, WIN_H * 0.70),
                            text='SCORE:', fgcolor='white',
                            size=TILE_SIZE*1.30)
        self.font.render_to(self.app.screen, (WIN_W * 0.610, WIN_H * 0.80),
                            text=f'{self.app.tetris.score}', fgcolor='white',
                            size=TILE_SIZE*1.45)


class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetromino = Tetromino(self)
        self.speed_up = False
        self.next_tetromino = Tetromino(self, current=False)
        self.score = 0
        self.full_lines = 0
        self.points_per_lines = {0: 0, 1: 100, 2: 300, 3: 500, 4: 800}

    def get_score(self):
        self.score += self.points_per_lines[self.full_lines]
        self.full_lines = 0

    def check_full_lines(self):
        row = FIELD_HEIGHT - 1
        for y in range(FIELD_HEIGHT - 1, -1, -1):
            for x in range(FIELD_WIDTH):
                self.field_array[row][x] = self.field_array[y][x]

                if self.field_array[y][x]:
                    self.field_array[row][x].pos = vec(x, y)

            if sum(map(bool, self.field_array[y])) < FIELD_WIDTH:
                row -= 1
            else:
                for x in range(FIELD_WIDTH):
                    self.field_array[row][x].alive = False
                    self.field_array[row][x] = 0
                self.full_lines += 1

    def put_tetromino_blocks_in_array(self):
        for block in self.tetromino.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.field_array[y][x] = block

    def get_field_array(self):
        return [[0 for x in range(FIELD_WIDTH)] for y in range(FIELD_HEIGHT)]

    def is_game_over(self):
        if self.tetromino.blocks[0].pos.y == INIT_POS_OFFSET[1]:
            pg.time.wait(300)
            return True

    def has_tetromino_landed(self):
        if self.tetromino.landing:
            if self.is_game_over():
                self.__init__(self.app)
            else:
                self.speed_up = False
                self.put_tetromino_blocks_in_array()
                self.next_tetromino.current = True
                self.tetromino = self.next_tetromino
                self.next_tetromino = Tetromino(self, current=False)

    def control(self, pressed_key):
        if pressed_key == pg.K_LEFT:
            self.tetromino.move(direction='LEFT')
        elif pressed_key == pg.K_RIGHT:
            self.tetromino.move(direction='RIGHT')
        elif pressed_key == pg.K_UP:
            self.tetromino.rotate()
        elif pressed_key == pg.K_DOWN:
            self.speed_up = True

    def draw_grid(self):
        for x in range(FIELD_WIDTH):
            for y in range(FIELD_HEIGHT):
                pg.draw.rect(self.app.screen, 'black',
                             (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
        # self.pg.draw.rect(self.app.screen, 'yellow', (0, 0,
        #                   FIELD_WIDTH * TILE_SIZE, FIELD_HEIGHT * TILE_SIZE), 5)

    def update(self):
        trigger = [self.app.anim_trigger,
                   self.app.fast_anim_trigger][self.speed_up]
        if trigger:
            self.check_full_lines()
            self.tetromino.update()
            self.has_tetromino_landed()
            self.get_score()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)
