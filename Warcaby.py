import pygame
from warcaby.constants import WIDTH, HEIGHT, SQUARE_SIZE, BACKGROUND_GAME_OVER, BACKGROUND_RESET, \
    BACKGROUND_RECT, BACKGROUND_RECT_GO
from warcaby.game import Game
from warcaby.ErrorsHandle import *

clock = pygame.time.Clock()
FPS = 60

WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT))
pygame.display.set_caption('Warcaby')


def get_row_col_from_mouse(pos):
    x, y = pos
    if x > WIDTH + 300 or y > HEIGHT:
        raise OwnErrorMessage("Error with coursor position")
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


# for restart showing screen
def show_restart_screen():
    WIN.blit(BACKGROUND_RESET, BACKGROUND_RECT)
    pygame.display.flip()
    waiting = True

    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:  # if key pressed
                waiting = False


# for game showing screen
def show_game_over_screen():
    WIN.blit(BACKGROUND_GAME_OVER, BACKGROUND_RECT_GO)
    pygame.display.flip()
    waiting = True

    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:  # if key pressed
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
            game = Game(WIN)  # after showing new window want to restart whole game
            pos = pygame.mouse.get_pos()
            row, col = get_row_col_from_mouse(pos)
            game.select(row, col)
            game.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                show_restart_screen()
                game = Game(WIN)  # after showing new window want to restart whole game
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
                game.update()

            if event.type == pygame.MOUSEBUTTONDOWN:  # mouse use to control pieces
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                if col > 7 or row > 7:
                    print("You have clicked side of board, DON'T do it anymore\n" + "Row clicked: \n" + str(
                        row) + "\nColumn clicked: \n" + str(col))
                    break
                elif row <= 7 and col <= 7:
                    game.select(row, col)
                    game.update()
                game.select(row, col)

        game.update()

    pygame.quit()


main()
