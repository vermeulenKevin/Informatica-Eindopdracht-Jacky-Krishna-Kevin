import pygame
import subprocess

pygame.init()

SCREENW, SCREENH = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((SCREENW, SCREENH), pygame.NOFRAME | pygame.FULLSCREEN)

BLAUW = (0,0,255)

running = True
while running:  
    screen.fill(BLAUW)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
                pygame.quit()
                subprocess.run(["python", "main.py"])
            if event.key == pygame.K_s:
                running = False
                pygame.quit()
                subprocess.run(["python", "spelregels.py"])

pygame.quit()

