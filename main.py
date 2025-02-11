import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)

SCREENW, SCREENH = pygame.display.Info().current_w, pygame.display.Info().current_h
print(f"Screen Width: {SCREENW}, Screen Height: {SCREENH}")


#SCREENW = 800
#SCREENH = 800
BOARDW = 320
BOARDH = 320
CELLW = BOARDW // 32
CELLH = BOARDH // 32
CENTER_CELLW = CELLW * 2
CENTER_CELLH = CELLH * 2

pygame.display.set_caption (("Minotaurus")) 
center_x = (SCREENW - CENTER_CELLW) // 2
center_y = (SCREENH - CENTER_CELLH) // 2
screen = pygame.display.set_mode((SCREENW, SCREENH), pygame.NOFRAME | pygame.FULLSCREEN)

def draw_board():
    pygame.draw.rect(screen, BLACK, (center_x,center_y, CENTER_CELLW, CENTER_CELLH))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    
    draw_board()

    pygame.display.update()


pygame.quit()