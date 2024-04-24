import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont('Arial', size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_surface, text_rect)

def draw_apple(surface, apple):
    pygame.draw.rect(surface, RED, (apple[0]*GRID_SIZE, apple[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_banana(surface, apple):
    pygame.draw.rect(surface, 'yellow', (apple[0]*GRID_SIZE, apple[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_snake(surface, snake):
    for segment in snake:
        pygame.draw.rect(surface, WHITE, (segment[0]*GRID_SIZE, segment[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))

def main():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')

    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    snake_direction = RIGHT
    apple = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
    banana = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    running = True
    cnt_of_food = 0
    level = 1
    delay = 110
    food_collected = 0

    FOOD_TIMEOUT = 3000
    food_timer = 0

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != DOWN:
                    snake_direction = UP
                elif event.key == pygame.K_DOWN and snake_direction != UP:
                    snake_direction = DOWN
                elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
                    snake_direction = LEFT
                elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
                    snake_direction = RIGHT

        current_time = pygame.time.get_ticks()
        if current_time - food_timer > FOOD_TIMEOUT:
            apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            food_timer = current_time

        new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
        snake.insert(0, new_head)

        if not (0 <= new_head[0] < GRID_WIDTH) or not (0 <= new_head[1] < GRID_HEIGHT):
            running = False

        if len(snake) != len(set(snake)):
            running = False

        if new_head == apple:
            apple = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
            cnt_of_food += 1
            food_collected += 1
        elif new_head == banana:
            banana = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            cnt_of_food += 2
            food_collected += 2
            new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
            snake.insert(0, new_head)
        else:
            snake.pop()

        screen.fill(BLACK)
        draw_snake(screen, snake)
        draw_apple(screen, apple)
        draw_banana(screen, banana)
        draw_text(screen, f"Your level: {level}", 20, WIDTH - 60, 30)
        draw_text(screen, f"Foods collected: {food_collected}", 20, WIDTH - 80, 60)
        pygame.display.flip()

        if cnt_of_food >= 3:
            remainder = cnt_of_food - 3
            cnt_of_food = remainder
            level += 1
            delay = delay - 10

        pygame.time.delay(delay)

    screen.fill(BLACK)
    draw_text(screen, "Game Over", 50, WIDTH//2, HEIGHT//2)
    pygame.display.flip()
    pygame.time.delay(2000)

    # Закрыть окно
    pygame.quit()

main()