
from warcaby.game import Game
from warcaby.piece import Piece
from warcaby.board import Board
import pygame
from warcaby.constants import RED, WHITE, YELLOW, BLUE, WIDTH, HEIGHT, ROWS, COLS


def test_move_to_yellow_king():
    board = Board()
    piece = Piece(6, 6, YELLOW)
    board.move(piece, 7, 6)
    assert board.yellow_kings == 1


def test_move_to_white_king():
    board = Board()
    piece = Piece(1, 1, WHITE)
    board.move(piece, 0, 1)
    assert board.white_kings == 1


def test_get_piece_yellow():
    board = Board()
    assert board.get_piece(5, 4) == board.board[5][4]


def test_get_piece_white():
    board = Board()
    assert board.get_piece(7, 4) == board.board[7][4]


def test_get_valid_moves():
    board = Board()
    piece = Piece(5, 4, YELLOW)
    moves = board.get_valid_moves(piece)
    assert moves == {(4, 3): [], (4, 5): []}


def test_traverse_left():
    board = Board()
    traverse_left = board._traverse_left(4, 2, -1, YELLOW, 3, skipped=[])
    assert traverse_left == {(4, 3): []}


def test_traverse_right():
    board = Board()
    traverse_left = board._traverse_left(4, 2, -1, YELLOW, 5, skipped=[])
    assert traverse_left == {(4, 5): []}