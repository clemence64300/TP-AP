# ne pas oublier conda activate snake.py
import random
import sys
import pygame

white = [255, 255, 255]
black = [0, 0, 0]
red = [255, 0, 0]

snake = [[10, 15], [11, 15], [12, 15]]
direction = [0, 1]
fruit = [random.randint(0, 30) * 20, random.randint(0, 30) * 20, 20, 20]

pygame.init()
screen = pygame.display.set_mode([20 * 30, 20 * 30])
clock = pygame.time.Clock()

while True:

    #événement du clavier
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP and direction != [0, 1]:
                direction = [0, -1]
            if event.key == pygame.K_DOWN and direction != [0, -1]:
                direction = [0, 1]
            if event.key == pygame.K_RIGHT and direction != [-1, 0]:
                direction = [1, 0]
            if event.key == pygame.K_LEFT and direction != [1, 0]:
                direction = [-1, 0]
    
    #manger le fruit et grandir
    if snake[0][0] == fruit[0]//20 and snake[0][1] == fruit[1]//20 :
            fruit = [random.randint(0, 30) * 20, random.randint(0, 30) * 20, 20, 20]
            newqueue = snake[-1].copy()
            newqueue[0] += direction[0]
            newqueue[1] += direction[1]
            snake.append(newqueue)

    #déplacement du serpent
    snake.pop()
    a = snake[0].copy()
    a[0] += direction[0]
    a[1] += direction[1]
    snake.insert(0, a)
    screen.fill(white)

    #actualiser le dessin et l'écran
    pygame.draw.rect(screen, red, fruit)
    for x, y in snake:
        rect = [x * 20, y * 20, 20, 20]
        pygame.draw.rect(screen, black, rect)
        pygame.display.update()
    clock.tick(2)
