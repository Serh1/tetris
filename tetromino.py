import random
from settings import *


class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos, color):
        self.tetromino = tetromino
        self.pos = vec(pos) + INIT_POS_OFFSET
        self.next_pos = vec(pos) + NEXT_POS_OFFSET
        self.alive = True

        super().__init__(self.tetromino.tetris.sprite_group)
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        pg.draw.rect(self.image, color,
                     (1, 1, TILE_SIZE-2, TILE_SIZE-2), border_radius=3)
        self.rect = self.image.get_rect()

    def is_alive(self):
        if not self.alive:
            self.kill()

    def rotate(self, pivot_pos):
        translated = self.pos - pivot_pos
        rotated = translated.rotate(90)
        return pivot_pos + rotated

    def set_rect_pos(self):
        pos = [self.next_pos, self.pos][self.tetromino.current]
        self.rect.topleft = pos * TILE_SIZE

    def update(self):
        self.is_alive()
        self.set_rect_pos()

    def is_collide(self, pos):
        x, y = int(pos.x), int(pos.y)
        if 0 <= x < FIELD_WIDTH and y < FIELD_HEIGHT and (y < 0 or not self.tetromino.tetris.field_array[y][x]):
            return False
        return True


class Tetromino:
    def __init__(self, tetris, current=True):
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOES.keys()))
        self.color = random.choice(list(COLORS.values()))
        self.blocks = [Block(self, pos, self.color)
                       for pos in TETROMINOES[self.shape]]
        self.landing = False
        self.current = current

    def rotate(self):
        pivot_pos = self.blocks[0].pos
        new_block_positions = [block.rotate(
            pivot_pos) for block in self.blocks]

        if not self.is_collide(new_block_positions):
            for j, block in enumerate(self.blocks):
                block.pos = new_block_positions[j]

    def is_collide(self, block_direction):
        return any(map(Block.is_collide, self.blocks, block_direction))

    def move(self, direction):
        move_direction = MOVE_DIRECTIONS[direction]
        new_block_positions = [block.pos +
                               move_direction for block in self.blocks]
        is_collide = self.is_collide(new_block_positions)

        if not is_collide:
            for block in self.blocks:
                block.pos += move_direction
        elif direction == 'DOWN':
            self.landing = True

    def update(self):
        self.move(direction='DOWN')
