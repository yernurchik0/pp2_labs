import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 25
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed = 20

while True:
    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y = max(ball_y - ball_speed, ball_radius)
            elif event.key == pygame.K_DOWN:
                ball_y = min(ball_y + ball_speed, screen_height - ball_radius)
            elif event.key == pygame.K_LEFT:
                ball_x = max(ball_x - ball_speed, ball_radius)
            elif event.key == pygame.K_RIGHT:
                ball_x = min(ball_x + ball_speed, screen_width - ball_radius)