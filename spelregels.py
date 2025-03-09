import pygame
import subprocess

pygame.init()

SCREENW, SCREENH = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((SCREENW, SCREENH), pygame.NOFRAME | pygame.FULLSCREEN)

GREEN = (0,255,0)

running = True
while running:  
    screen.fill(GREEN)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                subprocess.run(["python", "startscherm.py"])

pygame.quit()

