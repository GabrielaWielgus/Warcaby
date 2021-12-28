import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# rgb
RED = (255, 0, 0)
YELLOW = (252, 210, 79)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('warcaby/assets/crown.png'), (50, 50))
WHITE_WIN = pygame.transform.scale(pygame.image.load('warcaby/assets/white_win.png'), (400, 400))
YELLOW_WIN = pygame.transform.scale(pygame.image.load('warcaby/assets/yellow_win.png'), (400, 400))
START = pygame.transform.scale(pygame.image.load('warcaby/assets/start.png'),(200,200))
QUIT = pygame.transform.scale(pygame.image.load('warcaby/assets/exit.png'), (200, 200))
RESTART = pygame.transform.scale(pygame.image.load('warcaby/assets/back.png'), (200, 200))
TURN_WHITE = pygame.transform.scale(pygame.image.load('warcaby/assets/white_turn.png'), (300, 300))
TURN_YELLOW = pygame.transform.scale(pygame.image.load('warcaby/assets/yellow_turn.png'), (300, 300))