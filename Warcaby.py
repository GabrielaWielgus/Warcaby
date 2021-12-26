import pygame
from warcaby.constants import WIDTH, HEIGHT
from warcaby.board import Board
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Warcaby')


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw_squares(WIN)
        pygame.display.update()

    pygame.quit()


main()
