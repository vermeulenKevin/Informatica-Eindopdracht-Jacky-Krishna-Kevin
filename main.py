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
dobbelsteen = False
minotaurus_selected = None
minotaurus_moves_left = 0
stappen = 0

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
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 6, 0, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 4, 0, 7, 5, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
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
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 12]
]

# alle images inladen en goed formaat geven
gras_image = pygame.image.load("images/gras3.png")
gras_image = pygame.transform.scale(gras_image, (CELLW, CELLH))

heg_image = pygame.image.load("images/heg2.png")
heg_image = pygame.transform.scale(heg_image, (CELLW, CELLH)) 

muur_image = pygame.image.load("images/muurtest3.png")
muur_image = pygame.transform.scale(muur_image, (CELLW, CELLH)) 

midden_image = pygame.image.load("images/midden_leeg.png")
midden_image = pygame.transform.scale(midden_image, (2*CELLW, 2*CELLH)) 

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

minotaurus_image = pygame.image.load("images/midden_met_minotaurus.png")
minotaurus_image = pygame.transform.scale(minotaurus_image, (CELLW, CELLH)) 

minotaurusveld_image = pygame.image.load("images/minotaurusveld.png")
minotaurusveld_image = pygame.transform.scale(minotaurusveld_image, (CELLW, CELLH)) 


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
                screen.blit (midden_image, (x-24,y-24))
            elif layout[row][col] == 8:
                screen.blit (heldblauw_image, (x, y))
            elif layout[row][col] == 9:
                screen.blit (heldwit_image, (x, y))
            elif layout[row][col] == 10:
                screen.blit (heldgeel_image, (x, y))
            elif layout[row][col] == 11:
                screen.blit (heldrood_image, (x, y))
            elif layout[row][col] == 12:
                minotaurus_image = pygame.image.load("images/midden_met_minotaurus.png")
                minotaurus_image = pygame.transform.scale(minotaurus_image, ((2*CELLW), (2*CELLH))) 
                screen.blit (minotaurus_image, (x-408, y-384))
            elif layout[row][col] == 13:
                minotaurusveld_image = pygame.image.load("images/minotaurusveld.png")
                minotaurusveld_image = pygame.transform.scale(minotaurusveld_image, ((CELLW), (CELLH))) 
                screen.blit (minotaurusveld_image, (x, y))
            elif layout[row][col] == 14:
                middenleeg_image = pygame.image.load("images/midden_leeg.png")
                middenleeg_image = pygame.transform.scale(middenleeg_image, ((2*CELLW), (2*CELLH))) 
                screen.blit (middenleeg_image, (x-24, y-24))


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
            if layout[y][x] == 11:
                red_positions.append((x, y))

    return red_positions

def find_yellow_heroes(layout):
    yellow_positions = []

    for y in range(len(layout)):
        for x in range(len(layout[y])):
            if layout[y][x] == 10:
                yellow_positions.append((x, y))

    return yellow_positions

def move_hero_with_timer():
    global last_move_time
    current_time = time.time()
    if current_time - last_move_time >= 0.1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
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
    global selected_hero, stappen
    if selected_hero:
        x, y = selected_hero
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < BOARDW and 0 <= new_y < BOARDH:
            if layout[new_y][new_x] == 0:
                layout[y][x] = 0
                layout[new_y][new_x] = held_kleur
                selected_hero = (new_x, new_y)
                stappen += 1
                print(f"Held verplaatst naar: {new_x}, {new_y}. Aantal stappen: {stappen}")
            else:
                print("Ongelidge zet, de nieuwe tile is geen gras")
    else:
        print("Geen held geselecteerd")    

def worp_x(speler):
    print(f"{speler} gooide andere held verplaatsen")

def worp_minotaurus(speler):
    print(f"{speler} gooide minotaurus")
    minotaurus_plaatsen()
    print("minotaurus is geplaatst!")
    stappen_zetten = True
    while stappen_zetten:
        pygame.time.wait(300)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    minotaurus_bewegen(-1, 0)
                if keys[pygame.K_w]:
                    minotaurus_bewegen(0, -1)
                if keys[pygame.K_s]:
                    minotaurus_bewegen(0, 1)
                if keys[pygame.K_d]:
                    minotaurus_bewegen(1, 0)

def minotaurus_plaatsen():
    global minotaurus_selected, minotaurus_moves_left
    toegestane_plek = pygame.Rect(648, 312, 144, 144)
    print("Klik op de tile waar je de minotaurus wilt plaatsen, dit moet grenzen aan een gekleurd hokje in het midden van het speelveld.")
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                mino_x = CELLW * ((mouse_pos[0]) // CELLW)
                mino_y = CELLH * ((mouse_pos[1]) // CELLH)
                mino_x_layout = (mino_x - ((SCREENW - BOARDW) // 2)) // CELLW
                mino_y_layout = mino_y // CELLH
                if toegestane_plek.collidepoint(mouse_pos) and layout[mino_x_layout][mino_y_layout] == 0:
                    print("mouse_pos[0]:", mouse_pos[0])
                    print("mouse_pos[1]:", mouse_pos[1])
                    mino_x = CELLW * ((mouse_pos[0]) // CELLW)
                    mino_y = CELLH * ((mouse_pos[1]) // CELLH)
                    mino_x_layout = (mino_x - ((SCREENW - BOARDW) // 2)) // CELLW
                    mino_y_layout = mino_y // CELLH
                    print(f"mino x{mino_x_layout}, mino y{mino_y_layout}")
                    minotaurus_selected = (mino_x_layout, mino_y_layout)
                    minotaurus_moves_left = 8
                    layout[mino_y_layout][mino_x_layout] = 13
                    for row in range(len(layout)):  # Loop through rows
                        for col in range(len(layout[row])):  # Loop through columns
                            if layout[row][col] == 12:
                                layout[row][col] = 100
                    layout[16][16] = 14
                    draw_board()
                    pygame.display.update()
                    print(f"Minotaurus geplaatst op: {mino_x}, {mino_y} met {minotaurus_moves_left} stappen beschikbaar.")
                    waiting = False

def minotaurus_bewegen(dx, dy):
    global minotaurus_selected, stappen, stappen_zetten
    mag_bewegen = True
    while mag_bewegen:
        x, y = minotaurus_selected
        new_x, new_y = x + dx, y + dy
        if layout[new_y][new_x] == 0:
            layout[y][x] = 0
            layout[new_y][new_x] = 13
            minotaurus_selected = (new_x, new_y)
            print(f"Minotaurus verplaatst naar: {new_x}, {new_y}")
            stappen = stappen + 1
            if stappen > 7:
                mag_bewegen = False
                stappen_zetten = False
        else:
            print("Ongelidge zet, de nieuwe tile is geen gras")   

def worp_groen(speler):
    print(f"{speler} gooide groen")

def worp_vier(speler):
    spelers = {
        1: "wit", 
        2: "blauw", 
        3: "geel", 
        4: "rood"
    }  
    print(f"{spelers[speler]} gooide vier")
    global held_kleur, selected_hero
    print("Klik op een held van jouw kleur")
    wachten_op_klik = True
    while wachten_op_klik:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("er is geklikt")
                mouse_pos = pygame.mouse.get_pos()
                cell_x = (mouse_pos[0] - ((SCREENW - BOARDW) // 2)) // CELLW
                cell_y = mouse_pos[1] // CELLH             

                blue_heroes = find_blue_heroes(layout)
                white_heroes = find_white_heroes(layout)
                red_heroes = find_red_heroes(layout)
                yellow_heroes = find_yellow_heroes(layout)

                if (cell_x, cell_y) in blue_heroes and speler == 2:
                    held_kleur = 8
                    selected_hero = (cell_x, cell_y)
                    wachten_op_klik = False
                elif (cell_x, cell_y) in white_heroes and speler == 1:
                    held_kleur = 9
                    selected_hero = (cell_x, cell_y)
                    wachten_op_klik = False
                elif (cell_x, cell_y) in red_heroes and speler == 4:
                    held_kleur = 10
                    selected_hero = (cell_x, cell_y)
                    wachten_op_klik = False
                elif (cell_x, cell_y) in yellow_heroes and speler == 3:
                    held_kleur = 11
                    selected_hero = (cell_x, cell_y)
                    wachten_op_klik = False
                else: 
                    selected_hero = None
                    print("Dit is niet jouw held")
        draw_board()
        pygame.display.update()
 
    
    stappen = 0  
    while stappen < 4:
        move_hero_with_timer()
        draw_board()
        pygame.display.update()

    
    print("4 stappen gezet")


def worp_vijf(speler):
    spelers = {
        1: "wit", 
        2: "blauw", 
        3: "geel", 
        4: "rood"
    }  
    print(f"{spelers[speler]} gooide vijf")
    global held_kleur, selected_hero
    print("Klik op een held van jouw kleur")
    wachten_op_klik = True
    while wachten_op_klik:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("er is geklikt")
                mouse_pos = pygame.mouse.get_pos()
                cell_x = (mouse_pos[0] - ((SCREENW - BOARDW) // 2)) // CELLW
                cell_y = mouse_pos[1] // CELLH             

                blue_heroes = find_blue_heroes(layout)
                white_heroes = find_white_heroes(layout)
                red_heroes = find_red_heroes(layout)
                yellow_heroes = find_yellow_heroes(layout)

                if (cell_x, cell_y) in blue_heroes and speler == 2:
                    held_kleur = 8
                    selected_hero = (cell_x, cell_y)
                    wachten_op_klik = False
                elif (cell_x, cell_y) in white_heroes and speler == 1:
                    held_kleur = 9
                    selected_hero = (cell_x, cell_y)
                    wachten_op_klik = False
                elif (cell_x, cell_y) in red_heroes and speler == 4:
                    held_kleur = 10
                    selected_hero = (cell_x, cell_y)
                    wachten_op_klik = False
                elif (cell_x, cell_y) in yellow_heroes and speler == 3:
                    held_kleur = 11
                    selected_hero = (cell_x, cell_y)
                    wachten_op_klik = False
                else: 
                    selected_hero = None
                    print("Dit is niet jouw held")
        draw_board()
        pygame.display.update()
 
    
    stappen = 0  
    while stappen < 5:
        move_hero_with_timer()
        draw_board()
        pygame.display.update()

    
    print("5 stappen gezet")

def worp_zes(speler):
    spelers = {
        1: "wit", 
        2: "blauw", 
        3: "geel", 
        4: "rood"
    }  
    print(f"{spelers[speler]} gooide zes")
    global held_kleur, selected_hero
    print("Klik op een held van jouw kleur")
    wachten_op_klik = True
    while wachten_op_klik:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("er is geklikt")
                mouse_pos = pygame.mouse.get_pos()
                cell_x = (mouse_pos[0] - ((SCREENW - BOARDW) // 2)) // CELLW
                cell_y = mouse_pos[1] // CELLH             

                blue_heroes = find_blue_heroes(layout)
                white_heroes = find_white_heroes(layout)
                red_heroes = find_red_heroes(layout)
                yellow_heroes = find_yellow_heroes(layout)

                if (cell_x, cell_y) in blue_heroes and speler == 2:
                    held_kleur = 8
                    selected_hero = (cell_x, cell_y)
                    wachten_op_klik = False
                elif (cell_x, cell_y) in white_heroes and speler == 1:
                    held_kleur = 9
                    selected_hero = (cell_x, cell_y)
                    wachten_op_klik = False
                elif (cell_x, cell_y) in red_heroes and speler == 4:
                    held_kleur = 10
                    selected_hero = (cell_x, cell_y)
                    wachten_op_klik = False
                elif (cell_x, cell_y) in yellow_heroes and speler == 3:
                    held_kleur = 11
                    selected_hero = (cell_x, cell_y)
                    wachten_op_klik = False
                else: 
                    selected_hero = None
                    print("Dit is niet jouw held")
        draw_board()
        pygame.display.update()
 
    
    stappen = 0  
    while stappen < 6:
        move_hero_with_timer()
        draw_board()
        pygame.display.update()

    
    print("6 stappen gezet")

def beurt_systeem(speler):
    global dobbelsteen, huidige_speler
    spelers = {
        1: "wit", 
        2: "blauw", 
        3: "geel", 
        4: "rood"
    }  
    print(f"Beurt van {spelers[speler]}")
    
    uitkomst = random.randint(3,6)
    if uitkomst == 1:
        worp_x(speler)
    elif uitkomst == 2:
        worp_groen(speler)
    elif uitkomst == 3:
        worp_minotaurus(speler)
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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    draw_board()
    pygame.display.update()
    
    while eerste_beurt:
        begin_speler = random.randint(1, 4)
        begin_speler = beurt_systeem(begin_speler)
        eerste_beurt = False

    while dobbelsteen:
        huidige_speler = beurt_systeem(huidige_speler)
        dobbelsteen = False

    pygame.display.update()
pygame.quit()
