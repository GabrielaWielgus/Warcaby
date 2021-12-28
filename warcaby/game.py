import pygame
from .constants import YELLOW, WHITE, BLUE, SQUARE_SIZE, START, QUIT, RESTART, TURN_WHITE, TURN_YELLOW, WHITE_WIN, YELLOW_WIN
from warcaby.board import Board
from warcaby.button import Button

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        self.start_button.draw(self.win)
        self.quit_button.draw(self.win)
        self.restart_button.draw(self.win)
        if self.turn == YELLOW:
            self.turn_yellow_button.draw(self.win)
        else:
            self.turn_white_button.draw(self.win)
        if self.winner() == YELLOW:
            self.win_yellow_button.draw(self.win)
        elif self.winner() == WHITE:
            self.win_white_button.draw(self.win)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.start_button = Button(870, 500, START, 0.8)
        self.quit_button = Button(870, 600, QUIT, 0.8)
        self.restart_button = Button(870, 700, RESTART, 0.8)
        self.turn_white_button = Button(825, 0, TURN_WHITE, 0.8)
        self.turn_yellow_button = Button(825, 0, TURN_YELLOW, 0.8)
        self.win_white_button = Button(800, 225, WHITE_WIN, 0.8)
        self.win_yellow_button = Button(800, 225, YELLOW_WIN, 0.8)
        self.turn = YELLOW
        self.valid_moves = {}

    def reset(self):
        self._init()

    def select(self, row, col):
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
        winner = self.board.winner()
        return self.board.winner()

    def draw_buttons(self, win):
        self.turn_white_button.draw(self.win)
        self.turn_yellow_button.draw(self.win)


    def change_turn(self):
        self.valid_moves = {}
        if self.turn == YELLOW:
            self.turn = WHITE
        else:
            self.turn = YELLOW