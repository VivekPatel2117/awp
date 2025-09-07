import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Infinite Scrolling Background")

# Load background image
bg = pygame.image.load("C:/Users/Heshita vaviya/Downloads/player.jpg").convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))  # Optional scaling
bg_width = bg.get_width()

# Set initial scroll positions
x1 = 0
x2 = bg_width
scroll_speed = 2

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move background
    x1 -= scroll_speed
    x2 -= scroll_speed

    # Reset positions if off screen
    if x1 <= -bg_width:
        x1 = bg_width
    if x2 <= -bg_width:
        x2 = bg_width

    # Draw backgrounds
    screen.blit(bg, (x1, 0))
    screen.blit(bg, (x2, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
