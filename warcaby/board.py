import pygame
from warcaby.constants import BLACK, ROWS, SQUARE_SIZE, COLS, WHITE, YELLOW
from warcaby.piece import Piece


class Board:
    """
    Class Board is responsible for:
        Creating Board for a game, details:
        - draw squares on board
        - move pieces, and makes king if condition is met
        - getting pieces based on rows and columns of board
        - creating pieces on board
        - removing pieces if condition is met
        - determining the winner
        - getting valid moves for pieces (or king)

    """

    def __init__(self):
        self.board = []
        self.yellow_left = self.white_left = 12
        self.yellow_kings = self.white_kings = 0
        self.create_board()

    @property
    def board(self):
        return self.__board

    @property
    def yellow_left(self):
        return self.__yellow_left

    @property
    def yellow_kings(self):
        return self.__yellow_kings

    @property
    def create_board(self):
        return self.__create_board()

    @property
    def white_left(self):
        return self.__white_left

    @property
    def white_kings(self):
        return self.__white_kings

    @board.setter
    def board(self, board1):
        self.__board = board1

    @yellow_left.setter
    def yellow_left(self, yellow_l):
        self.__yellow_left = yellow_l

    @yellow_kings.setter
    def yellow_kings(self, yellow_k):
        self.__yellow_kings = yellow_k

    @white_left.setter
    def white_left(self, white_l):
        self.__white_left = white_l

    @white_kings.setter
    def white_kings(self, white_k):
        self.__white_kings = white_k

    # first method draw then draw_squares,
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1  # create king + 1
            else:
                self.yellow_kings += 1

    def get_piece(self, row, col):
        try:
            self.board[row][col]
        except:
            print("error don't click on side only on board")  # create to get error for try catch
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))  # adding piece to board list
                    elif row > 4:
                        self.board[row].append(Piece(row, col, YELLOW))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                piece_dr = lambda x: piece.draw(win) if (x != 0) else None
                piece_dr(piece)

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0  # remove piece
            if piece != 0:
                if piece.color == YELLOW:
                    self.yellow_left -= 1  # amount of pieces last - 1
                else:
                    self.white_left -= 1

    def winner(self):
        if self.yellow_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return YELLOW
        return None

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == YELLOW or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))  # yellow up move
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))  # yellow up move

        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))  # white down move
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))  # white down move

        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        # start -> row above where piece is
        # step -> up or down diagonally
        # stop -> piece end of sight
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left]
            if current == 0:  # no piece in square
                if skipped and not last:
                    break  # in loop if we skipped, found empty square, and if that's all -> no more moves
                elif skipped:
                    # increases the field of sight +1, across piece
                    moves[(r, left)] = last + skipped  # double jumping
                else:
                    # move add
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, -1)  # !!! CHANGE AFTER PRESENTATION 0 to -1 before max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    # now we are in new position, need to recalculate moves
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:  # piece with our color, blocked
                break
            else:  # opponent color, piece in move
                last = [current]
            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        #same like in _traverse_left but on right side
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped  # double jumping
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, -1)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            right += 1

        return moves
