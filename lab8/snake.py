import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set screen dimensions
WIDTH, HEIGHT = 800, 600

# Define cell size and grid dimensions
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Set game speeds for different levels
SPEEDS = [10, 15, 20]

class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

        # Initialize game variables
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = pygame.K_RIGHT
        self.food = self.generate_food()
        self.score = 0
        self.level = 1
        self.speed = SPEEDS[self.level - 1]
        
        # Snake movement variables
        self.move_timer = 0
        self.move_interval = 1000 / self.speed  # Time in milliseconds between each move
        self.velocity = [1, 0]  # Initial velocity: moving right

    def generate_food(self):
        while True:
            food_pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if food_pos not in self.snake:
                return food_pos

    def draw_snake(self):
        for segment in self.snake:
            pygame.draw.rect(self.screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE,
                                                  CELL_SIZE, CELL_SIZE))

    def draw_food(self):
        pygame.draw.rect(self.screen, RED, (self.food[0] * CELL_SIZE, self.food[1] * CELL_SIZE,
                                            CELL_SIZE, CELL_SIZE))

    def check_collision(self):
        head = self.snake[0]
        # Check if snake hits the wall
        if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
            return True
        # Check if snake hits itself
        if head in self.snake[1:]:
            return True
        return False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != pygame.K_DOWN:
                    self.direction = pygame.K_UP
                    self.velocity = [0, -1]  # Change velocity to move up
                elif event.key == pygame.K_DOWN and self.direction != pygame.K_UP:
                    self.direction = pygame.K_DOWN
                    self.velocity = [0, 1]  # Change velocity to move down
                elif event.key == pygame.K_LEFT and self.direction != pygame.K_RIGHT:
                    self.direction = pygame.K_LEFT
                    self.velocity = [-1, 0]  # Change velocity to move left
                elif event.key == pygame.K_RIGHT and self.direction != pygame.K_LEFT:
                    self.direction = pygame.K_RIGHT
                    self.velocity = [1, 0]  # Change velocity to move right
        return True

    def update_snake(self):
        # Move the snake based on velocity
        self.move_timer += self.clock.get_rawtime()
        if self.move_timer >= self.move_interval:
            self.move_timer = 0
            new_head = (self.snake[0][0] + self.velocity[0], self.snake[0][1] + self.velocity[1])
            # Insert new head at the beginning of the snake list
            self.snake.insert(0, new_head)
            # Check if snake eats food
            if self.snake[0] == self.food:
                self.score += 1
                self.food = self.generate_food()
                # Increase speed and level if score meets criteria
                if self.score % 3 == 0:  # Adjust this to change level up criteria
                    self.level += 1

            else:
                # Remove the tail segment
                self.snake.pop()

    def main_loop(self):
        running = True
        while running:
            # Handle events
            running = self.handle_events()

            # Clear the screen
            self.screen.fill(BLACK)

            # Draw snake and food
            self.draw_snake()
            self.draw_food()

            # Update snake position
            self.update_snake()

            # Check for collision
            if self.check_collision():
                running = False

            # Draw score and level
            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            level_text = self.font.render(f"Level: {self.level}", True, WHITE)
            self.screen.blit(score_text, (10, 10))
            self.screen.blit(level_text, (10, 40))

            # Update display
            pygame.display.flip()

            # Cap the frame rate
            self.clock.tick()

        pygame.quit()

if __name__ == "__main__":
    game = SnakeGame()
    game.main_loop()