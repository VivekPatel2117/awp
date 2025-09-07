import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Target Shooting Game")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)

# Target properties
target_radius = 30
target_x = random.randint(target_radius, screen_width - target_radius)
target_y = random.randint(target_radius, screen_height - target_radius)

# Crosshair properties
crosshair_radius = 10
crosshair_x = screen_width // 2
crosshair_y = screen_height // 2

# Score and Timer
score = 0
game_duration = 60  # seconds
start_time = time.time()

# Font
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse click to shoot
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance = ((mouse_x - target_x) ** 2 + (mouse_y - target_y) ** 2) ** 0.5
            if distance <= target_radius:
                score += 1
                target_x = random.randint(target_radius, screen_width - target_radius)
                target_y = random.randint(target_radius, screen_height - target_radius)

    # Update crosshair position
    crosshair_x, crosshair_y = pygame.mouse.get_pos()

    # Draw everything
    screen.fill(white)
    pygame.draw.circle(screen, red, (target_x, target_y), target_radius)
    pygame.draw.circle(screen, black, (crosshair_x, crosshair_y), crosshair_radius, 2)

    # Calculate remaining time
    elapsed_time = time.time() - start_time
    remaining_time = max(0, game_duration - int(elapsed_time))

    # Display score and timer
    score_text = font.render(f"Score: {score}", True, black)
    time_text = font.render(f"Time: {remaining_time}", True, black)
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (screen_width - 150, 10))

    # Check for game over
    if remaining_time == 0:
        game_over_text = font.render("Game Over", True, black)
        screen.blit(game_over_text, (screen_width // 2 - 80, screen_height // 2))
        pygame.display.flip()
        time.sleep(3)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
