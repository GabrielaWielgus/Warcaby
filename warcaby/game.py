import pygame
from warcaby.constants import YELLOW, WHITE, BLUE, SQUARE_SIZE, RESTART, TURN_WHITE, TURN_YELLOW, WHITE_WIN, YELLOW_WIN
from warcaby.board import Board
from warcaby.button import Button


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    @property
    def win(self):
        return self.__win

    @property
    def _init(self):
        return self.__init()

    @win.setter
    def win(self, win1):
        self.__win = win1

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

    @property
    def selected(self):
        return self.__selected

    @property
    def board(self):
        return self.__board

    @property
    def restart_button(self):
        return self.__restart_button

    @property
    def turn_white_button(self):
        return self.__turn_white_button

    @property
    def turn_yellow_button(self):
        return self.__turn_yellow_button

    @property
    def win_white_button(self):
        return self.__win_white_button

    @property
    def win_yellow_button(self):
        return self.__win_yellow_button

    @property
    def turn(self):
        return self.__turn

    @property
    def valid_moves(self):
        return self.__valid_moves

    @selected.setter
    def selected(self, selected1):
        self.__selected = selected1

    @board.setter
    def board(self, board1):
        self.__board = board1

    @restart_button.setter
    def restart_button(self, restart):
        self.__restart_button = restart

    @turn_white_button.setter
    def turn_white_button(self, turn_white):
        self.__turn_white_button = turn_white

    @turn_yellow_button.setter
    def turn_yellow_button(self, turn_yellow):
        self.__turn_yellow_button = turn_yellow

    @win_white_button.setter
    def win_white_button(self, win_white):
        self.__win_white_button = win_white

    @win_yellow_button.setter
    def win_yellow_button(self, win_yellow):
        self.__win_yellow_button = win_yellow

    @turn.setter
    def turn(self, turn1):
        self.__turn = turn1

    @valid_moves.setter
    def valid_moves(self, valid_moves1):
        self.__valid_moves = valid_moves1

    def reset(self):
        self._init()

    def select(self, row, col):  # select piece to move
        if self.__selected:
            result = self._move(row, col)
            if not result:
                self.__selected = None
                self.select(row, col)

        piece = self.__board.get_piece(row, col)
        if piece != 0 and piece.color == self.__turn:
            self.__selected = piece
            self.__valid_moves = self.__board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        piece = self.__board.get_piece(row, col)
        if self.__selected and piece == 0 and (row, col) in self.__valid_moves:
            # moving if piece selected, empty square, possible move
            self.__board.move(self.selected, row, col)
            skipped = self.__valid_moves[(row, col)]
            if skipped:
                self.__board.remove(skipped)
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
        return self.__board.winner()

    def draw_buttons(self, win):
        self.__turn_white_button.draw(self.win)
        self.__turn_yellow_button.draw(self.win)

    def change_turn(self):
        self.__valid_moves = {}  # reset dictionary to get another valid moves
        if self.__turn == YELLOW:
            self.__turn = WHITE
        else:
            self.__turn = YELLOW
