import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)

SCREENW, SCREENH = pygame.display.Info().current_w, pygame.display.Info().current_h

SCREENW = 800
SCREENH = 600

screen = pygame.display.set_mode ((SCREENW, SCREENH))
pygame.display.set_mode((SCREENW, SCREENH), pygame.NOFRAME)
pygame.display.set_caption (("Minotaurus")) 
center_x = (SCREENW - SCREENH) // 2
center_y = (SCREENW - SCREENH) // 2
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


BOARDW = 1200
BOARDH = 600
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

...