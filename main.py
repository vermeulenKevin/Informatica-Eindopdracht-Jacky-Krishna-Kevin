import pygame
import time
import random

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
last_move_time = 0
selected_hero = None
eerste_beurt = True

SCREENW, SCREENH = pygame.display.Info().current_w, pygame.display.Info().current_h
print(f"Screen Width: {SCREENW}, Screen Height: {SCREENH}")

#SCREENW = 800
#SCREENH = 800
BOARDW = SCREENH
BOARDH = SCREENH
CELLW = BOARDW // 32
CELLH = BOARDH // 32

print(f"Cell breedte: {CELLW} Cell hoogte: {CELLH}")

pygame.display.set_caption (("Minotaurus")) 
screen = pygame.display.set_mode((SCREENW, SCREENH), pygame.NOFRAME | pygame.FULLSCREEN)

layout = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 1],
    [1, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1],
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
    [1, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1],
    [1, 11, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# alle images inladen en goed formaat geven
gras_image = pygame.image.load("images/grass2.png")
gras_image = pygame.transform.scale(gras_image, (CELLW, CELLH))

heg_image = pygame.image.load("images/hedge.png")
heg_image = pygame.transform.scale(heg_image, (CELLW, CELLH)) 

muur_image = pygame.image.load("images/muurtest3.png")
muur_image = pygame.transform.scale(muur_image, (CELLW, CELLH)) 

midden_image = pygame.image.load("images/middentest.png")
midden_image = pygame.transform.scale(midden_image, (CELLW, CELLH)) 

blauw_image = pygame.image.load("images/nieuwetegelblauw1.png")
blauw_image = pygame.transform.scale(blauw_image, (CELLW, CELLH)) 

wit_image = pygame.image.load("images/nieuwetegelwit.png")
wit_image = pygame.transform.scale(wit_image, (CELLW, CELLH)) 

geel_image = pygame.image.load("images/nieuwetegelgeel1.png")
geel_image = pygame.transform.scale(geel_image, (CELLW, CELLH)) 

rood_image = pygame.image.load("images/nieuwetegelrood.png")
rood_image = pygame.transform.scale(rood_image, (CELLW, CELLH)) 

heldblauw_image = pygame.image.load("images/blauwepion.png")
heldblauw_image = pygame.transform.scale(heldblauw_image, (CELLW, CELLH)) 

heldwit_image = pygame.image.load("images/wittepion.png")
heldwit_image = pygame.transform.scale(heldwit_image, (CELLW, CELLH)) 

heldgeel_image = pygame.image.load("images/gelepion.png")
heldgeel_image = pygame.transform.scale(heldgeel_image, (CELLW, CELLH)) 

heldrood_image = pygame.image.load("images/rodepion1.png")
heldrood_image = pygame.transform.scale(heldrood_image, (CELLW, CELLH)) 

def draw_board():
    for row in range(len(layout)):
        for col in range(len(layout[row])):
            # Bereken positie van de tegel
            x = (SCREENW - BOARDW) // 2 + col * CELLW
            y = (SCREENH - BOARDH) // 2 + row * CELLH

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
            elif layout[row][col] == 9:
                screen.blit (heldwit_image, (x, y))
            elif layout[row][col] == 10:
                screen.blit (heldgeel_image, (x, y))
            elif layout[row][col] == 11:
                screen.blit (heldrood_image, (x, y))

def find_blue_heroes(layout):
    blue_positions = []

    for y in range(len(layout)):
        for x in range(len(layout[y])):
            if layout[y][x] == 8:
                blue_positions.append((x, y))

    return blue_positions

def find_white_heroes(layout):
    white_positions = []

    for y in range(len(layout)):
        for x in range(len(layout[y])):
            if layout[y][x] == 9:
                white_positions.append((x, y))

    return white_positions

def find_red_heroes(layout):
    red_positions = []

    for y in range(len(layout)):
        for x in range(len(layout[y])):
            if layout[y][x] == 10:
                red_positions.append((x, y))

    return red_positions

def find_yellow_heroes(layout):
    yellow_positions = []

    for y in range(len(layout)):
        for x in range(len(layout[y])):
            if layout[y][x] == 11:
                yellow_positions.append((x, y))

    return yellow_positions

def move_hero_with_timer():
    global last_move_time
    current_time = time.time()
    if current_time - last_move_time >= 0.1:
        last_move_time = current_time
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            move_selected_hero(-1, 0)
        if keys[pygame.K_w]:
            move_selected_hero(0, -1)
        if keys[pygame.K_s]:
            move_selected_hero(0, 1)
        if keys[pygame.K_d]:
            move_selected_hero(1, 0)

def move_selected_hero(dx, dy):
    global selected_hero
    if selected_hero:
        x, y = selected_hero
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < BOARDW and 0 <= new_y < BOARDH:
            if layout[new_y][new_x] == 0:
                layout[y][x] = 0
                layout[new_y][new_x] = held_kleur
                selected_hero = (new_x, new_y)
                print(f"Held verplaatst naar: {new_x}, {new_y}")
            else:
                print("Ongelidge zet, de nieuwe tile is geen gras")
    else:
        print("Geen held geselecteerd")


def worp_muur(speler):
    print(f"{speler} gooide muur")

def worp_minotaurus(speler):
    print(f"{speler} gooide minotaurus")

def worp_groen(speler):
    print(f"{speler} gooide groen")

def worp_vier(speler):
    print(f"{speler} gooide vier")

def worp_vijf(speler):
    print(f"{speler} gooide vijf")

def worp_zes(speler):
    print(f"{speler} gooide zes")

def beurt_systeem(speler):
    global dobbelsteen, huidige_speler
    spelers = {
        1: "wit", 
        2: "blauw", 
        3: "geel", 
        4: "rood"
    }  
    print(f"Beurt van {spelers[speler]}")
    
    uitkomst = random.randint(1,6)
    if uitkomst == 1:
        worp_muur(speler)
    elif uitkomst == 2:
        worp_minotaurus(speler)
    elif uitkomst == 3:
        worp_groen(speler)
    elif uitkomst == 4:
        worp_vier(speler)
    elif uitkomst == 5:
        worp_vijf(speler)
    elif uitkomst == 6:
        worp_zes(speler)
    
    if speler < 4:
        huidige_speler = speler + 1
    else:
        huidige_speler = 1
    
    dobbelsteen = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    draw_board()

    if event.type == pygame.MOUSEBUTTONDOWN:

        mouse_pos = pygame.mouse.get_pos()
        cell_x = (mouse_pos[0] - ((SCREENW - BOARDW) // 2)) // CELLW
        cell_y = mouse_pos[1] // CELLH             

        blue_heroes = find_blue_heroes(layout)
        white_heroes = find_white_heroes(layout)
        red_heroes = find_red_heroes(layout)
        yellow_heroes = find_yellow_heroes(layout)

        if (cell_x, cell_y) in blue_heroes:
            held_kleur = 8
            selected_hero = (cell_x, cell_y)
        elif (cell_x, cell_y) in white_heroes:
            held_kleur = 9
            selected_hero = (cell_x, cell_y)
        elif (cell_x, cell_y) in red_heroes:
            held_kleur = 10
            selected_hero = (cell_x, cell_y)
        elif (cell_x, cell_y) in yellow_heroes:
            held_kleur = 11
            selected_hero = (cell_x, cell_y)
        else: 
            selected_hero = None
    
    pygame.display.update()
    
    while eerste_beurt:
        begin_speler = random.randint(1, 4)
        begin_speler = beurt_systeem(begin_speler)
        eerste_beurt = False

    while dobbelsteen:
        huidige_speler = beurt_systeem(huidige_speler)
        dobbelsteen = False

    move_hero_with_timer()
            
    pygame.display.update()
pygame.quit()
