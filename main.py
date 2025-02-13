import pygame
import time

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
GRAS = (2, 212, 12)
MUUR = (128, 128, 128)
HEG = (4, 135, 4)
BLUE = (0, 0, 200)
RED = (210, 0, 0)
YELLOW = (230, 230, 0)

COOLDOWN = 0.5
last_click_time = 0

SCREENW, SCREENH = pygame.display.Info().current_w, pygame.display.Info().current_h
print(f"Screen Width: {SCREENW}, Screen Height: {SCREENH}")

#SCREENW = 800
#SCREENH = 800
BOARDW = 768
BOARDH = 768
CELLW = BOARDW // 32
CELLH = BOARDH // 32

print(f"Cell breedte: {CELLW} Cell hoogte: {CELLH}")

pygame.display.set_caption (("Minotaurus")) 
screen = pygame.display.set_mode((SCREENW, SCREENH), pygame.NOFRAME | pygame.FULLSCREEN)

layout = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 1],
    [1, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 2, 2, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [2, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 2],
    [2, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 6, 6, 3, 3, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 6, 7, 7, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 4, 7, 7, 5, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [2, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 4, 4, 5, 5, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 2],
    [2, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 2],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 2, 2, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1],
    [1, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# alle images inladen en goed formaat geven
gras_image = pygame.image.load("images/grastest.png")
gras_image = pygame.transform.scale(gras_image, (CELLW, CELLH))

heg_image = pygame.image.load("images/hegtest.png")
heg_image = pygame.transform.scale(heg_image, (CELLW, CELLH)) 

muur_image = pygame.image.load("images/muurtest.png")
muur_image = pygame.transform.scale(muur_image, (CELLW, CELLH)) 

midden_image = pygame.image.load("images/middentest.png")
midden_image = pygame.transform.scale(midden_image, (CELLW, CELLH)) 

blauw_image = pygame.image.load("images/blauwtest.png")
blauw_image = pygame.transform.scale(blauw_image, (CELLW, CELLH)) 

wit_image = pygame.image.load("images/wittest.png")
wit_image = pygame.transform.scale(wit_image, (CELLW, CELLH)) 

geel_image = pygame.image.load("images/geeltest.png")
geel_image = pygame.transform.scale(geel_image, (CELLW, CELLH)) 

rood_image = pygame.image.load("images/roodtest.png")
rood_image = pygame.transform.scale(rood_image, (CELLW, CELLH)) 

heldblauw_image = pygame.image.load("images/testheldblauw.png")
heldblauw_image = pygame.transform.scale(heldblauw_image, (CELLW, CELLH)) 


def draw_board():
    for row in range(len(layout)):
        for col in range(len(layout[row])):
            # Bereken positie van de tegel
            x = (SCREENW - BOARDW) // 2 + col * CELLW
            y = (SCREENH - BOARDH) // 2 + row * CELLH

            # Bepaal kleur op basis van de waarde in de matrix
            
            # Teken de tegel
            #pygame.draw.rect(screen, color, (x, y, CELLW, CELLH))

            # border om elke tile
            # pygame.draw.rect(screen, GRAY, (x, y, CELLW, CELLH), 1)

            if layout[row][col] == 0:
                screen.blit (gras_image, (x,y))
            elif layout[row][col] == 1:
                screen.blit (heg_image, (x,y))
            elif layout[row][col] == 2:
                screen.blit (muur_image, (x,y))
            elif layout[row][col] == 3:
                screen.blit (blauw_image, (x,y))
            elif layout[row][col] == 4:
                screen.blit (rood_image, (x,y))
            elif layout[row][col] == 5:
                screen.blit (geel_image, (x,y))
            elif layout[row][col] == 6:
                screen.blit (wit_image, (x,y))
            elif layout[row][col] == 7:
                screen.blit (midden_image, (x,y))
            elif layout[row][col] == 8:
                screen.blit (heldblauw_image, (x, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    draw_board()

    pygame.display.update()

    if event.type == pygame.MOUSEBUTTONDOWN:
        current_time = time.time()
        if current_time - last_click_time > COOLDOWN:
            last_click_time = current_time

            mouse_pos = pygame.mouse.get_pos()
            cell_x = (mouse_pos[0] - 336) // CELLW  # Bereken de x-coördinaat in de grid
            cell_y = mouse_pos[1] // CELLH  # Bereken de y-coördinaat in de grid  # Haal de muispositie op
            print(f"Klik op tile positie: ({cell_x}, {cell_y})")  # Print de tile-coördinaten


pygame.quit()