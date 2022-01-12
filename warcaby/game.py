import pygame
from .constants import WIDTH, HEIGHT, YELLOW, WHITE, BLUE, SQUARE_SIZE, START, QUIT, RESTART, TURN_WHITE, TURN_YELLOW, \
    WHITE_WIN, \
    YELLOW_WIN
from warcaby.board import Board
from warcaby.button import Button


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):  # updating display
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        self.restart_button.draw(self.win)
        turn = lambda x: self.turn_yellow_button.draw(self.win) if (x == YELLOW) else self.turn_white_button.draw(
            self.win)
        turn(self.turn)
        if self.winner() is not None:
            winner = lambda x: self.win_yellow_button.draw(self.win) if (x == YELLOW) else self.win_white_button.draw(
                self.win)
            winner(self.winner())
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        # ----graphics----
        self.restart_button = Button(790, 300, RESTART, 0.8)
        self.turn_white_button = Button(825, 0, TURN_WHITE, 0.8)
        self.turn_yellow_button = Button(825, 0, TURN_YELLOW, 0.8)
        self.win_white_button = Button(500, 225, WHITE_WIN, 0.8)
        self.win_yellow_button = Button(500, 225, YELLOW_WIN, 0.8)
        # ----turn-----
        self.turn = YELLOW
        self.valid_moves = {}

    def reset(self):
        self._init()

    def select(self, row, col):  # select piece to move
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            # moving if piece selected, empty square, possible move
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def winner(self):
        return self.board.winner()

    def draw_buttons(self, win):
        self.turn_white_button.draw(self.win)
        self.turn_yellow_button.draw(self.win)

    def change_turn(self):
        self.valid_moves = {}  # reset dictionary to get another valid moves
        if self.turn == YELLOW:
            self.turn = WHITE
        else:
            self.turn = YELLOW
