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
BOARDW = 768
BOARDH = 768
CELLW = BOARDW // 32
CELLH = BOARDH // 32
CENTER_CELLW = CELLW * 2
CENTER_CELLH = CELLH * 2

pygame.display.set_caption (("Minotaurus")) 
center_x = (SCREENW - CENTER_CELLW) // 2
center_y = (SCREENH - CENTER_CELLH) // 2
screen = pygame.display.set_mode((SCREENW, SCREENH), pygame.NOFRAME | pygame.FULLSCREEN)
print(f"Center_x: {center_x}, Center_y: {center_y}")

#def draw_board():
    #pygame.draw.rect(screen, BLACK, (center_x,center_y, CENTER_CELLW, CENTER_CELLH))

def draw_grid():
    for row in range(32):
        for col in range(32):
            # Bereken positie van de tegel
            x = (SCREENW - BOARDW) // 2 + col * CELLW
            y = (SCREENH - BOARDH) // 2 + row * CELLH
            
            # Check of het een rand is (buitenste rij of kolom)
            if row == 0 or row == 31 or col == 0 or col == 31:
                # Buitenste rand = muur (zwart)
                pygame.draw.rect(screen, BLACK, (x, y, CELLW, CELLH))
            else:
                # Binnenste tegels = leeg (grijs)
                pygame.draw.rect(screen, GRAY, (x, y, CELLW, CELLH), 1)  # Dunne grijze lijn voor het raster



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    
    #draw_board()
    draw_grid()

    pygame.display.update()


pygame.quit()