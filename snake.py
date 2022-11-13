# ne pas oublier conda activate snake.py
import random
import sys
import pygame

# Constants
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
COLORS = {"background": WHITE, "snake": BLACK, "fruit": RED}

WIDTH = 30  # number of cells
HEIGHT = 30  # number of cells
CELL_SIZE = 20  # number of pixels

FPS = 5  # frames per second

UP = [0, -1]
DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]


# Game state
snake = [[10, 15], [11, 15], [12, 15]]
direction = LEFT
fruit = [
    random.randint(0, WIDTH - 1) * CELL_SIZE,
    random.randint(0, HEIGHT - 1) * CELL_SIZE,
    CELL_SIZE,
    CELL_SIZE,
]


# Helper Function
def exit():
    pygame.quit()
    sys.exit()


# Score
score = 0
pygame.display.set_caption(f"🐍 Score: {score}")


##fonctions

# Event Management


def handle_events():
    global direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                exit()
            if event.key == pygame.K_UP and direction != DOWN:
                direction = UP
            if event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
            if event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT
            if event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT


# Game Logic


def move_snake():
    global fruit
    global direction
    global snake
    global score
    if snake[0][0] == fruit[0] // CELL_SIZE and snake[0][1] == fruit[1] // CELL_SIZE:
        fruit = [
            random.randint(0, WIDTH - 1) * CELL_SIZE,
            random.randint(0, HEIGHT - 1) * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE,
        ]
        newqueue = snake[-1].copy()
        newqueue[0] += direction[0]
        newqueue[1] += direction[1]
        snake.append(newqueue)
        score += 1
    if (
        snake[0][0] < 0
        or snake[0][0] >= WIDTH
        or snake[0][1] < 0
        or snake[0][1] >= HEIGHT
    ):
        exit()
    if snake[0][0] == snake[-1][0] and snake[0][1] == snake[-1][1]:
        exit()

    snake.pop()
    a = snake[0].copy()
    a[0] += direction[0]
    a[1] += direction[1]
    snake.insert(0, a)
    screen.fill(COLORS["background"])


# Setup


def setup():
    pygame.init()
    screen = pygame.display.set_mode([CELL_SIZE * WIDTH, CELL_SIZE * HEIGHT])
    clock = pygame.time.Clock()
    return screen, clock


# Frame Update


def draw_frame(screen):
    global score
    pygame.draw.rect(screen, COLORS["fruit"], fruit)
    for x, y in snake:
        rect = [x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE]
        pygame.draw.rect(screen, COLORS["snake"], rect)
    pygame.display.update()
    pygame.display.set_caption(f"🐍 Score: {score}")


# Wait for next frame


def wait_for_next_screen(clock):
    clock.tick(FPS)


# Main Loop

screen, clock = setup()
while True:
    handle_events()
    move_snake()
    draw_frame(screen)
    wait_for_next_screen(clock)
