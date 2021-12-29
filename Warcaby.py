import pygame
from pygame import K_ESCAPE, K_SPACE

from warcaby.constants import RED, WHITE, WIDTH, HEIGHT, SQUARE_SIZE, BACKGROUND_GAME_OVER, BACKGROUND_RESET, \
    BACKGROUND_RECT, BACKGROUND_RECT_GO
from warcaby.game import Game
from warcaby.button import Button

clock = pygame.time.Clock()
FPS = 60

WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT + 300))
pygame.display.set_caption('Warcaby')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def show_restart_screen():
    WIN.blit(BACKGROUND_RESET, BACKGROUND_RECT)
    pygame.display.flip()
    waiting = True

    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                waiting = False


def show_game_over_screen():
    WIN.blit(BACKGROUND_RESET, BACKGROUND_RECT)
    pygame.display.flip()
    waiting = True

    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                waiting = False


def show_game_over_screen():
    WIN.blit(BACKGROUND_GAME_OVER, BACKGROUND_RECT_GO)
    pygame.display.flip()
    waiting = True

    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                waiting = False


def main():
    run = True
    game_over = True
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() is not None:
            print(game.winner())
            show_game_over_screen()
            game = Game(WIN)
            pos = pygame.mouse.get_pos()
            row, col = get_row_col_from_mouse(pos)
            game.select(row, col)
            game.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                show_restart_screen()
                game = Game(WIN)
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
                game.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()


main()
