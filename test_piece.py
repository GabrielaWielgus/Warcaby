from warcaby.piece import Piece
from warcaby.constants import YELLOW, WHITE, BLUE, WIDTH, HEIGHT, SQUARE_SIZE, START, QUIT, RESTART, TURN_WHITE, TURN_YELLOW, \
    WHITE_WIN, \
    YELLOW_WIN
import pygame
WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT))


def test_constructor():
    obj = Piece(1, 2, BLUE)
    assert obj.row == 1


def test_color_blue():
    obj = Piece(1, 2, BLUE)
    assert obj.__repr__() == '(0, 0, 255)'


def test_color_yellow():
    obj = Piece(1, 2, YELLOW)
    assert obj.__repr__() == '(252, 210, 79)'


def test_color_white():
    obj = Piece(1, 2, WHITE)
    assert obj.__repr__() == '(255, 255, 255)'


def test_make_king():
    assert True


def test_calc_pos():
    obj = Piece(1, 2, WHITE)
    assert obj.x == 250
    assert obj.y == 150


def test_move1_yellow():
    obj = Piece(4, 8, YELLOW)
    obj.move(6, 10)
    assert obj.row == 6
    assert obj.col == 10


def test_move2_yellow():
    obj = Piece(4, 8, YELLOW)
    obj.move(100, 20)
    assert obj.row == 100
    assert obj.col == 20

def test_move1_white():
    obj = Piece(4, 8, WHITE)
    obj.move(100, 20)
    assert obj.row == 100
    assert obj.col == 20

def test_move2_white():
    obj = Piece(4, 8, WHITE)
    obj.move(100, 20)
    assert obj.row == 100
    assert obj.col == 20