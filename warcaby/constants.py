from os import path

import pygame
import pygame as pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

#rgb
RED = (255, 0, 0)
YELLOW = (252, 210, 79)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

#graphics
WHITE_WIN = pygame.transform.scale(pygame.image.load('warcaby/assets/white_win.png'), (400, 400))
CROWN = pygame.transform.scale(pygame.image.load('warcaby/assets/crown.png'), (50, 50))
YELLOW_WIN = pygame.transform.scale(pygame.image.load('warcaby/assets/yellow_win.png'), (400, 400))
START = pygame.transform.scale(pygame.image.load('warcaby/assets/start.png'),(200,200))
QUIT = pygame.transform.scale(pygame.image.load('warcaby/assets/exit.png'), (200, 200))
BACK = pygame.transform.scale(pygame.image.load('warcaby/assets/back.png'), (200, 200))
RESTART = pygame.transform.scale(pygame.image.load('warcaby/assets/restart.png'), (400, 400))
TURN_WHITE = pygame.transform.scale(pygame.image.load('warcaby/assets/white_turn.png'), (300, 300))
TURN_YELLOW = pygame.transform.scale(pygame.image.load('warcaby/assets/yellow_turn.png'), (300, 300))
BACKGROUND_RESET = pygame.transform.scale(pygame.image.load('warcaby/assets/background_restart.png'), (500,500))
BACKGROUND_GAME_OVER = pygame.transform.scale(pygame.image.load('warcaby/assets/background_game_over.png'), (500,500))
BACKGROUND_RECT = BACKGROUND_RESET.get_rect()
BACKGROUND_RECT_GO = BACKGROUND_GAME_OVER.get_rect()