from warcaby.game import Game
from warcaby.piece import Piece
from warcaby.board import Board
import pygame
from warcaby.constants import WHITE, YELLOW, WIDTH, HEIGHT


def test_init1():
    WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    game = Game(WIN)
    assert game.win == pygame.display.set_mode((WIDTH + 300, HEIGHT))


def test_selected():
    WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    game = Game(WIN)
    game.selected = game.board.get_piece(5, 4)
    game.valid_moves = {(4, 3): [], (4, 5): []}
    game.turn = (252, 210, 79)
    assert game.select(5, 4) == True


def test_not_selected():
    WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    game = Game(WIN)
    game.selected = game.board.get_piece(4, 3)
    game.valid_moves = {(4, 3): [], (4, 5): []}
    game.turn = (252, 210, 79)
    assert game.select(4, 3) == False


def test_move_possible():
    WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    game = Game(WIN)
    game.selected = game.board.get_piece(5, 4)
    game.valid_moves = {(4, 3): [], (4, 5): []}
    game.turn = (252, 210, 79)
    assert game._move(4, 3) == True


def test_move_not_possible():
    WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    game = Game(WIN)
    game.selected = game.board.get_piece(5, 4)
    game.valid_moves = {(4, 3): [], (4, 5): []}
    game.turn = (252, 210, 79)
    assert game._move(5, 4) == False  # proba ustawienia pionka na tym miejscu, na którym już stoi


def test_is_remove_one():
    WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    piece = Piece(5, 2, YELLOW)
    board = Board()
    game = Game(WIN)
    # ---first move---#
    game.selected = game.board.get_piece(5, 4)
    game.valid_moves = {(4, 3): [], (4, 5): []}
    game.turn = (252, 210, 79)
    game._move(4, 3)
    # ---second move---#
    game.selected = game.board.get_piece(2, 5)
    game.valid_moves = {(3, 4): [], (3, 6): []}
    game.turn = (255, 255, 255)
    game._move(3, 4)
    # ---third move--#
    game.selected = game.board.get_piece(5, 2)
    game.valid_moves = {(4, 1): []}
    game.turn = (252, 210, 79)
    game._move(4, 1)
    # ---fourth move---#
    game.selected = game.board.get_piece(3, 4)
    game.valid_moves = {(5, 2): [piece], (4, 5): []}
    game.turn = (255, 255, 255)
    game._move(5, 2)
    assert game.board.yellow_left == 11


def test_is_remove_two():
    WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    piece1 = Piece(4, 3, YELLOW)
    piece2 = Piece(3, 2, YELLOW)

    game = Game(WIN)
    # ---first move---#
    game.selected = game.board.get_piece(5, 4)
    game.valid_moves = {(4, 3): [], (4, 5): []}
    game.turn = (252, 210, 79)
    game._move(4, 3)
    # ---second move---#
    game.selected = game.board.get_piece(2, 5)
    game.valid_moves = {(3, 4): [], (3, 6): []}
    game.turn = (255, 255, 255)
    game._move(3, 4)
    # ---third move--#
    game.selected = game.board.get_piece(5, 2)
    game.valid_moves = {(4, 1): []}
    game.turn = (252, 210, 79)
    game._move(4, 1)
    # ---fourth move---#
    game.selected = game.board.get_piece(3, 4)
    game.valid_moves = {(5, 2): [piece1], (4, 5): []}
    game.turn = (255, 255, 255)
    game._move(5, 2)
    # ---fifth move---#
    game.selected = game.board.get_piece(4, 1)
    game.valid_moves = {(3, 0): [], (3, 2): []}
    game.turn = (252, 210, 79)
    game._move(3, 2)
    # ---sixth move---#
    game.selected = game.board.get_piece(2, 3)
    game.valid_moves = {(4, 1): [piece2], (3, 4): []}
    game.turn = (255, 255, 255)
    game._move(4, 1)
    assert game.board.yellow_left == 10


def test_is_remove_double_jump():
    WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    piece1 = Piece(4, 3, YELLOW)
    piece2 = Piece(3, 2, YELLOW)
    piece3 = Piece(4, 1, WHITE)
    piece4 = Piece(2, 3, WHITE)

    game = Game(WIN)
    # ---first move---#
    game.selected = game.board.get_piece(5, 4)
    game.valid_moves = {(4, 3): [], (4, 5): []}
    game.turn = (252, 210, 79)
    game._move(4, 3)
    # ---second move---#
    game.selected = game.board.get_piece(2, 5)
    game.valid_moves = {(3, 4): [], (3, 6): []}
    game.turn = (255, 255, 255)
    game._move(3, 4)
    # ---third move--#
    game.selected = game.board.get_piece(5, 2)
    game.valid_moves = {(4, 1): []}
    game.turn = (252, 210, 79)
    game._move(4, 1)
    # ---fourth move---#
    game.selected = game.board.get_piece(3, 4)
    game.valid_moves = {(5, 2): [piece1], (4, 5): []}
    game.turn = (255, 255, 255)
    game._move(5, 2)
    # ---fifth move---#
    game.selected = game.board.get_piece(4, 1)
    game.valid_moves = {(3, 0): [], (3, 2): []}
    game.turn = (252, 210, 79)
    game._move(3, 2)
    # ---sixth move---#
    game.selected = game.board.get_piece(2, 3)
    game.valid_moves = {(4, 1): [piece2], (3, 4): []}
    game.turn = (255, 255, 255)
    game._move(4, 1)
    # ---seventh move---#
    game.selected = game.board.get_piece(5, 7)
    game.valid_moves = {(4, 5): [], (4, 7): []}
    game.turn = (252, 210, 79)
    game._move(4, 7)
    # ---eight move---#
    game.selected = game.board.get_piece(1, 4)
    game.valid_moves = {(2, 3): [], (2, 5): []}
    game.turn = (255, 255, 255)
    game._move(2, 5)
    # ---nineth move---#
    game.selected = game.board.get_piece(4, 7)
    game.valid_moves = {(3, 6): []}
    game.turn = (252, 210, 79)
    game._move(3, 6)
    # ---tenth move---#
    game.selected = game.board.get_piece(1, 2)
    game.valid_moves = {(2, 3): []}
    game.turn = (255, 255, 255)
    game._move(2, 3)
    # ---eleventh move---#
    game.selected = game.board.get_piece(5, 0)
    game.valid_moves = {(3, 2): [piece3], (1, 4): [piece3, piece4]}
    game.turn = (252, 210, 79)
    game._move(1, 4)
    assert game.board.yellow_left == 10
    assert game.board.white_left == 10


def test_is_yellow_king():
    WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    piece1 = Piece(4, 3, YELLOW)
    piece2 = Piece(3, 2, YELLOW)
    piece3 = Piece(4, 1, WHITE)
    piece4 = Piece(2, 3, WHITE)

    board = Board()
    game = Game(WIN)
    # ---first move---#
    game.selected = game.board.get_piece(5, 4)
    game.valid_moves = {(4, 3): [], (4, 5): []}
    game.turn = (252, 210, 79)
    game._move(4, 3)
    # ---second move---#
    game.selected = game.board.get_piece(2, 5)
    game.valid_moves = {(3, 4): [], (3, 6): []}
    game.turn = (255, 255, 255)
    game._move(3, 4)
    # ---third move--#
    game.selected = game.board.get_piece(5, 2)
    game.valid_moves = {(4, 1): []}
    game.turn = (252, 210, 79)
    game._move(4, 1)
    # ---fourth move---#
    game.selected = game.board.get_piece(3, 4)
    game.valid_moves = {(5, 2): [piece1], (4, 5): []}
    game.turn = (255, 255, 255)
    game._move(5, 2)
    # ---fifth move---#
    game.selected = game.board.get_piece(4, 1)
    game.valid_moves = {(3, 0): [], (3, 2): []}
    game.turn = (252, 210, 79)
    game._move(3, 2)
    # ---sixth move---#
    game.selected = game.board.get_piece(2, 3)
    game.valid_moves = {(4, 1): [piece2], (3, 4): []}
    game.turn = (255, 255, 255)
    game._move(4, 1)
    # ---seventh move---#
    game.selected = game.board.get_piece(5, 7)
    game.valid_moves = {(4, 5): [], (4, 7): []}
    game.turn = (252, 210, 79)
    game._move(4, 7)
    # ---eight move---#
    game.selected = game.board.get_piece(1, 4)
    game.valid_moves = {(2, 3): [], (2, 5): []}
    game.turn = (255, 255, 255)
    game._move(2, 5)
    # ---nineth move---#
    game.selected = game.board.get_piece(4, 7)
    game.valid_moves = {(3, 6): []}
    game.turn = (252, 210, 79)
    game._move(3, 6)
    # ---tenth move---#
    game.selected = game.board.get_piece(1, 2)
    game.valid_moves = {(2, 3): []}
    game.turn = (255, 255, 255)
    game._move(2, 3)
    # ---eleventh move---#
    game.selected = game.board.get_piece(5, 0)
    game.valid_moves = {(3, 2): [piece3], (1, 4): [piece3, piece4]}
    game.turn = (252, 210, 79)
    game._move(1, 4)
    # ---twelveth move---#
    game.selected = game.board.get_piece(0, 3)
    game.valid_moves = {(1, 2): []}
    game.turn = (255, 255, 255)
    game._move(1, 2)
    # ---therteen move---#
    game.selected = game.board.get_piece(1, 4)
    game.valid_moves = {(0, 3): []}
    game.turn = (252, 210, 79)
    game._move(0, 3)
    assert game.board.yellow_kings == 1


def test_is_yellow_king_attack_double_jump_backwards():
    WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    piece1 = Piece(4, 3, YELLOW)
    piece2 = Piece(3, 2, YELLOW)
    piece3 = Piece(4, 1, WHITE)
    piece4 = Piece(2, 3, WHITE)
    piece6 = Piece(1, 2, WHITE)
    piece7 = Piece(3, 2, WHITE)

    game = Game(WIN)
    # ---first move---#
    game.selected = game.board.get_piece(5, 4)
    game.valid_moves = {(4, 3): [], (4, 5): []}
    game.turn = (252, 210, 79)
    game._move(4, 3)
    # ---second move---#
    game.selected = game.board.get_piece(2, 5)
    game.valid_moves = {(3, 4): [], (3, 6): []}
    game.turn = (255, 255, 255)
    game._move(3, 4)
    # ---third move--#
    game.selected = game.board.get_piece(5, 2)
    game.valid_moves = {(4, 1): []}
    game.turn = (252, 210, 79)
    game._move(4, 1)
    # ---fourth move---#
    game.selected = game.board.get_piece(3, 4)
    game.valid_moves = {(5, 2): [piece1], (4, 5): []}
    game.turn = (255, 255, 255)
    game._move(5, 2)
    # ---fifth move---#
    game.selected = game.board.get_piece(4, 1)
    game.valid_moves = {(3, 0): [], (3, 2): []}
    game.turn = (252, 210, 79)
    game._move(3, 2)
    # ---sixth move---#
    game.selected = game.board.get_piece(2, 3)
    game.valid_moves = {(4, 1): [piece2], (3, 4): []}
    game.turn = (255, 255, 255)
    game._move(4, 1)
    # ---seventh move---#
    game.selected = game.board.get_piece(5, 7)
    game.valid_moves = {(4, 5): [], (4, 7): []}
    game.turn = (252, 210, 79)
    game._move(4, 7)
    # ---eight move---#
    game.selected = game.board.get_piece(1, 4)
    game.valid_moves = {(2, 3): [], (2, 5): []}
    game.turn = (255, 255, 255)
    game._move(2, 5)
    # ---nineth move---#
    game.selected = game.board.get_piece(4, 7)
    game.valid_moves = {(3, 6): []}
    game.turn = (252, 210, 79)
    game._move(3, 6)
    # ---tenth move---#
    game.selected = game.board.get_piece(1, 2)
    game.valid_moves = {(2, 3): []}
    game.turn = (255, 255, 255)
    game._move(2, 3)
    # ---eleventh move---#
    game.selected = game.board.get_piece(5, 0)
    game.valid_moves = {(3, 2): [piece3], (1, 4): [piece3, piece4]}
    game.turn = (252, 210, 79)
    game._move(1, 4)
    # ---twelveth move---#
    game.selected = game.board.get_piece(0, 3)
    game.valid_moves = {(1, 2): []}
    game.turn = (255, 255, 255)
    game._move(1, 2)
    # ---therteen move---#
    game.selected = game.board.get_piece(1, 4)
    game.valid_moves = {(0, 3): []}
    game.turn = (252, 210, 79)
    game._move(0, 3)
    # ---fourtheenth move---#
    game.selected = game.board.get_piece(2, 1)
    game.valid_moves = {(3, 0): [], (3, 2): []}
    game.turn = (255, 255, 255)
    game._move(3, 2)
    # ---fifetheenth move---#
    game.selected = game.board.get_piece(0, 3)
    game.valid_moves = {(2, 1): [piece6], (4, 3): [piece6, piece7], (1, 4): []}
    game.turn = (252, 210, 79)
    game.board.board[4][3] = 0
    game._move(4, 3)
    assert game.board.white_left == 8


def test_winner1():
    WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    game = Game(WIN)
    assert game.winner() == None


def test_winning_yellow():
    WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    game = Game(WIN)
    game.board.white_left = 0
    game.board.yellow_left = 1
    assert game.board.winner() == YELLOW


def test_winning_white():
    WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    game = Game(WIN)
    game.board.white_left = 8
    game.board.yellow_left = 0
    assert game.board.winner() == WHITE


def test_change_turn_yellow_to_white():
    WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    game = Game(WIN)
    game.change_turn()
    assert game.turn == WHITE


def test_change_turn_white_to_yellow():
    WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    game = Game(WIN)
    game.turn = WHITE
    game.change_turn()
    assert game.turn == YELLOW
