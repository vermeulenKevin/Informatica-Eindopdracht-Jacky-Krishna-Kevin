import pygame

# Constanten
GRID_SIZE = 32  # Aantal cellen per rij en kolom
CELL_SIZE = 20  # Grootte van elke cel in pixels
SCREEN_SIZE = GRID_SIZE * CELL_SIZE

# Kleuren
LIGHT_GREEN = (144, 238, 144)
DARK_GREEN = (0, 100, 0)
BLACK = (0, 0, 0)

# Initialiseer Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("LEGO Minotaurus")

# Spelbord aanmaken (0 = leeg, 1 = buitenrand)
board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Buitenste rand maken
for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        if x == 0 or y == 0 or x == GRID_SIZE - 1 or y == GRID_SIZE - 1:
            board[y][x] = 1  # Buitenrand

def draw_board():
    screen.fill(LIGHT_GREEN)
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if board[y][x] == 1:
                pygame.draw.rect(screen, DARK_GREEN, rect)  # Buitenrand
            pygame.draw.rect(screen, BLACK, rect, 1)  # Rasterlijnen

# Hoofdloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw_board()
    pygame.display.flip()

pygame.quit()
