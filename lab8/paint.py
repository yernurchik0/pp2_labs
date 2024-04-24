import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Shapes
RECTANGLE = 'rectangle'
CIRCLE = 'circle'
ERASER = 'eraser'

class PaintApp:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Paint App")
        self.clock = pygame.time.Clock()

        self.drawing_color = BLACK
        self.shape = None
        self.drawing = False
        self.start_pos = (0, 0)
        self.end_pos = (0, 0)

        self.create_buttons()

    def create_buttons(self):
        # Color selection buttons
        self.black_button = pygame.Rect(10, 10, 50, 50)
        self.white_button = pygame.Rect(70, 10, 50, 50)
        self.red_button = pygame.Rect(130, 10, 50, 50)
        self.green_button = pygame.Rect(190, 10, 50, 50)
        self.blue_button = pygame.Rect(250, 10, 50, 50)

        # Shape selection buttons
        self.rectangle_button = pygame.Rect(10, 70, 100, 30)
        self.circle_button = pygame.Rect(120, 70, 100, 30)

    def draw_buttons(self):
        # Draw color selection buttons
        pygame.draw.rect(self.screen, BLACK, self.black_button)
        pygame.draw.rect(self.screen, WHITE, self.white_button)
        pygame.draw.rect(self.screen, RED, self.red_button)
        pygame.draw.rect(self.screen, GREEN, self.green_button)
        pygame.draw.rect(self.screen, BLUE, self.blue_button)

        # Draw text on color selection buttons
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Black', True, WHITE)
        self.screen.blit(text_surface, (15, 25))
        text_surface = font.render('White', True, BLACK)
        self.screen.blit(text_surface, (75, 25))
        text_surface = font.render('Red', True, WHITE)
        self.screen.blit(text_surface, (135, 25))
        text_surface = font.render('Green', True, WHITE)
        self.screen.blit(text_surface, (195, 25))
        text_surface = font.render('Blue', True, WHITE)
        self.screen.blit(text_surface, (255, 25))

        # Draw shape selection buttons
        pygame.draw.rect(self.screen, BLACK, self.rectangle_button)
        pygame.draw.rect(self.screen, BLACK, self.circle_button)
        text_surface = font.render('Rectangle', True, WHITE)
        self.screen.blit(text_surface, (15, 75))
        text_surface = font.render('Circle', True, WHITE)
        self.screen.blit(text_surface, (125, 75))

    def draw_shape(self):
        if self.shape == RECTANGLE:
            pygame.draw.rect(self.screen, self.drawing_color, (self.start_pos[0], self.start_pos[1],
                                                               self.end_pos[0] - self.start_pos[0],
                                                               self.end_pos[1] - self.start_pos[1]), 0)
        elif self.shape == CIRCLE:
            radius = max(abs(self.end_pos[0] - self.start_pos[0]), abs(self.end_pos[1] - self.start_pos[1]))
            pygame.draw.circle(self.screen, self.drawing_color, self.start_pos, radius, 0)
        elif self.shape == ERASER:
            pygame.draw.circle(self.screen, BG_COLOR, pygame.mouse.get_pos(), 20)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.black_button.collidepoint(mouse_pos):
                    self.drawing_color = BLACK
                elif self.white_button.collidepoint(mouse_pos):
                    self.drawing_color = WHITE
                elif self.red_button.collidepoint(mouse_pos):
                    self.drawing_color = RED
                elif self.green_button.collidepoint(mouse_pos):
                    self.drawing_color = GREEN
                elif self.blue_button.collidepoint(mouse_pos):
                    self.drawing_color = BLUE
                elif self.rectangle_button.collidepoint(mouse_pos):
                    self.shape = RECTANGLE
                elif self.circle_button.collidepoint(mouse_pos):
                    self.shape = CIRCLE
                else:
                    self.drawing = True
                    self.start_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.drawing = False
                self.end_pos = pygame.mouse.get_pos()
                self.draw_shape()
        return True

    def main_loop(self):
        running = True
        while running:
            self.screen.fill(BG_COLOR)

            running = self.handle_events()
            self.draw_buttons()

            if self.drawing:
                self.end_pos = pygame.mouse.get_pos()
                self.draw_shape()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    app = PaintApp()
    app.main_loop()