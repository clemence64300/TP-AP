import random
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                print("↑")
            if event.key == pygame.K_DOWN:
                print("↓")
            if event.key == pygame.K_RIGHT:
                print("→")
            if event.key == pygame.K_LEFT:
                print("←")
    k=0
    for i in range (20) :
        k+=1
        for j in range (20) :
            k+=1
            x = 30*i
            y = 30*j
            width = 30
            height = 30
            rect = [x, y, width, height]
            if k%2 == 0 :
                red, blue, green = 255,255,255
                color = [red, green, blue]
                pygame.draw.rect(screen, color, rect)
    pygame.display.update()
    clock.tick(1)