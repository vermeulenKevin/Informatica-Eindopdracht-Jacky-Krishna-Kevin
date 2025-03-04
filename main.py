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
dobbelen = True

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
    [1, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 1],
    [1, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 11, 1],
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

blauw_image = pygame.image.load("images/blauwvlaktest.png")
blauw_image = pygame.transform.scale(blauw_image, (CELLW, CELLH)) 

wit_image = pygame.image.load("images/witvlaktest.png")
wit_image = pygame.transform.scale(wit_image, (CELLW, CELLH)) 

geel_image = pygame.image.load("images/geelvlaktest2.png")
geel_image = pygame.transform.scale(geel_image, (CELLW, CELLH)) 

rood_image = pygame.image.load("images/roodvlaktest.png")
rood_image = pygame.transform.scale(rood_image, (CELLW, CELLH)) 

heldblauw_image = pygame.image.load("images/testheldblauw2.png")
heldblauw_image = pygame.transform.scale(heldblauw_image, (CELLW, CELLH)) 

heldwit_image = pygame.image.load("images/testheldwit.png")
heldwit_image = pygame.transform.scale(heldwit_image, (CELLW, CELLH)) 

heldrood_image = pygame.image.load("images/testheldrood.png")
heldrood_image = pygame.transform.scale(heldrood_image, (CELLW, CELLH)) 

heldgeel_image = pygame.image.load("images/testheldgeel.png")
heldgeel_image = pygame.transform.scale(heldgeel_image, (CELLW, CELLH)) 


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
            elif layout[row][col] == 9:
                screen.blit (heldwit_image, (x, y))
            elif layout[row][col] == 10:
                screen.blit (heldrood_image, (x, y))
            elif layout[row][col] == 11:
                screen.blit (heldgeel_image, (x, y))

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
                print(f"Hero verplaatst naar: {new_x}, {new_y}")
            else:
                print("Ongelidge zet, de nieuwe tile is geen gras")
    else:
        print("Geen held geselecteerd")

def beurt_systeem(speler):  
    global dobbelen
    spelers = {1: "wit", 2: "blauw", 3: "geel", 4: "rood"}  
    print(f"Beurt van {spelers[speler]}")
    
    worp = input("Voer de dobbelsteenworp in (grijs, zwart, groen, 4, 5, 6): ")
    
    volgende_speler = speler + 1 if speler < 4 else 1 
    
    dobbelen = True
    return worp, volgende_speler

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    draw_board()

    if event.type == pygame.MOUSEBUTTONDOWN:
        current_time = time.time()
        if current_time - last_click_time > COOLDOWN:
            last_click_time = current_time

            mouse_pos = pygame.mouse.get_pos()
            cell_x = (mouse_pos[0] - ((SCREENW - BOARDW) // 2)) // CELLW
            cell_y = mouse_pos[1] // CELLH 
            print(f"Klik op tile positie: ({cell_x}, {cell_y})")

            blue_heroes = find_blue_heroes(layout)
            #print("Posities van de blauwe helden:", blue_heroes) 
            white_heroes = find_white_heroes(layout)
            #print("Posities van de witte helden:", white_heroes) 
            red_heroes = find_red_heroes(layout)
            #print("Posities van de rode helden:", red_heroes) 
            yellow_heroes = find_yellow_heroes(layout)
            #print("Posities van de gele helden:", yellow_heroes) 

            if (cell_x, cell_y) in blue_heroes:
                held_kleur = 8
                selected_hero = (cell_x, cell_y)
                print(f"Blauwe hero geselecteerd op positie: {selected_hero}")
            elif (cell_x, cell_y) in white_heroes:
                held_kleur = 9
                selected_hero = (cell_x, cell_y)
                print(f"Witte hero geselecteerd op positie: {selected_hero}")
            elif (cell_x, cell_y) in red_heroes:
                held_kleur = 10
                selected_hero = (cell_x, cell_y)
                print(f"Rode hero geselecteerd op positie: {selected_hero}")
            elif (cell_x, cell_y) in yellow_heroes:
                held_kleur = 11
                selected_hero = (cell_x, cell_y)
                print(f"Gele hero geselecteerd op positie: {selected_hero}")
            else: 
                selected_hero = None

    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_a]:
        #move_selected_hero(-1, 0)
    #if keys[pygame.K_w]:
        #move_selected_hero(0, -1)
    #if keys[pygame.K_s]:
        #move_selected_hero(0, 1)
    #if keys[pygame.K_d]:
        #move_selected_hero(1, 0)
    
    pygame.display.update()

    huidige_speler = random.randint(1, 4)
    
    while dobbelen:
        huidige_speler = random.randint(1, 4)
        worp, huidige_speler = beurt_systeem(huidige_speler)
        print(f"{huidige_speler} gooide: {worp}")
        dobbelen = False

    move_hero_with_timer()
            
    pygame.display.update()
pygame.quit()
