from warcaby.constants import SQUARE_SIZE, GREY, CROWN
import pygame


class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    @property
    def row(self):
        return self.__row

    @property
    def col(self):
        return self.__col

    @property
    def color(self):
        return self.__color

    @property
    def king(self):
        return self.__king

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @row.setter
    def row(self, row1):
        self.__row = row1

    @col.setter
    def col(self, col1):
        self.__col = col1

    @color.setter
    def color(self, color1):
        self.__color = color1

    @king.setter
    def king(self, king1):
        self.__king = king1

    @x.setter
    def x(self, x1):
        self.__x = x1

    @y.setter
    def y(self, y1):
        self.__y = y1

    def calc_pos(self):
        self.__x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.__y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.__king = True

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.__x, self.__y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.__color, (self.__x, self.__y), radius)
        if self.king:
            win.blit(CROWN, (self.__x - CROWN.get_width()//2, self.__y - CROWN.get_height()//2))

    def move(self, row, col):
        self.__row = row
        self.__col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)