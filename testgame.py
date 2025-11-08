import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Dodge Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Car settings
CAR_WIDTH, CAR_HEIGHT = 50, 100
car_x = WIDTH // 2 - CAR_WIDTH // 2
car_y = HEIGHT - CAR_HEIGHT - 10
car_speed = 7

# Obstacle settings
obstacle_width = 50
obstacle_height = 100
obstacle_speed = 5
obstacles = []

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Functions
def draw_car(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, CAR_WIDTH, CAR_HEIGHT))

def draw_obstacle(x, y):
    pygame.draw.rect(screen, RED, (x, y, obstacle_width, obstacle_height))

def show_score(score):
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

# Game Loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - CAR_WIDTH:
        car_x += car_speed

    # Add obstacles randomly
    if random.randint(1, 50) == 1:
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        obstacles.append([obstacle_x, -obstacle_height])

    # Move obstacles
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed

    # Check collisions
    for obstacle in obstacles:
        if (car_y < obstacle[1] + obstacle_height and
            car_y + CAR_HEIGHT > obstacle[1] and
            car_x < obstacle[0] + obstacle_width and
            car_x + CAR_WIDTH > obstacle[0]):
            running = False  # Collision detected

    # Remove off-screen obstacles and increase score
    obstacles = [obs for obs in obstacles if obs[1] < HEIGHT]
    score += 1

    # Draw car and obstacles
    draw_car(car_x, car_y)
    for obstacle in obstacles:
        draw_obstacle(obstacle[0], obstacle[1])

    show_score(score)

    pygame.display.update()
    clock.tick(FPS)

# Game Over
screen.fill(WHITE)
game_over_text = font.render(f"Game Over! Final Score: {score}", True, RED)
screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2))
pygame.display.update()
pygame.time.wait(3000)

pygame.quit()
sys.exit()
