import pygame
import subprocess

pygame.init()

SCREENW, SCREENH = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((SCREENW, SCREENH), pygame.NOFRAME | pygame.FULLSCREEN)

running = True
while running:  
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
                pygame.quit()
                subprocess.run(["python", "main.py"])

pygame.quit()

