import pygame as pg

vec = pg.math.Vector2

FPS = 60
FIELD_COLOR = (40, 40, 40)
BG_COLOR = (80, 80, 80)

ANIM_TIME_INTERVAL = 150
FAST_ANIM_TIME_INTERVAL = 50

TILE_SIZE = 30
FIELD_SIZE = FIELD_WIDTH, FIELD_HEIGHT = 10, 20
FIELD_RES = FIELD_WIDTH * TILE_SIZE, FIELD_HEIGHT * TILE_SIZE

FIELD_SCALE_W, FIELD_SCALE_H = 1.7, 1.0
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * \
    FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H

FONT_PATH = '/assets/font/open-sans.regular.ttf'


INIT_POS_OFFSET = vec(FIELD_WIDTH // 2 - 1, 0)
NEXT_POS_OFFSET = vec(FIELD_WIDTH * 1.4, FIELD_HEIGHT * 0.2)
MOVE_DIRECTIONS = {'LEFT': vec(-1, 0), 'RIGHT': vec(1, 0), 'DOWN': vec(0, 1)}

TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'I': [(0, 0), (0, -1), (0, -2), (0, -3)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}

COLORS = {
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'ORANGE': (255, 165, 0),
    'BLUE': (0, 0, 255),
    'YELLOW': (255, 255, 0),
    'PURPLE': (128, 0, 128),
    'CYAN': (0, 255, 255)
}
