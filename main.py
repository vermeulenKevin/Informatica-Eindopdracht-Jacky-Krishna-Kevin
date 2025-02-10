import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)

SCREENW = 1400
SCREENH = 800
screen = pygame.display.set_mode ((SCREENW, SCREENH))
pygame.display.set_caption (("Minotaurus"))

BOARDW = 800
BOARDH = 800
CELLW = BOARDW // 32
CELLH = BOARDH // 32

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.display.flip()
            
pygame.quit()
