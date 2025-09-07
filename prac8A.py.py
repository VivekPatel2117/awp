import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
freeze = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("9110 Samruddhi Surve")

# Fill background color
color = (255, 0, 0)  # Red
freeze.fill(color)

# Load and display image
try:
    img = pygame.image.load("C:/Users/Heshita vaviya/Downloads/glower-removebg-preview.png")
    freeze.blit(img, (600, 400))
except pygame.error:
    print("Image not found or path is incorrect.")

# Drawing shapes
pygame.draw.line(freeze, (255, 255, 255), (50, 50), (200, 50), 1)
pygame.draw.circle(freeze, (0, 255, 100), (200, 400), 100, 1)
pygame.draw.rect(freeze, (255, 255, 255), (200, 200, 400, 400), 2, border_radius=5)
pygame.draw.polygon(freeze, (255, 0, 255), [(300, 50), (150, 200), (450, 200)], 4)
pygame.draw.ellipse(freeze, (0, 255, 255), (350, 350, 400, 100), 5)
pygame.draw.polygon(freeze, (240, 100, 150), [(200, 150), (350, 50), (500, 150), (450, 300), (250, 300)], 10)

# Text rendering
font1 = pygame.font.SysFont("freesansbold.ttf", 50)
font2 = pygame.font.SysFont("chalkduster.ttf", 40)  # This font may not exist; you can change it.

text1 = font1.render("Hello", True, (0, 255, 0))
text2 = font2.render("World", True, (0, 255, 240))

textRect1 = text1.get_rect()
textRect2 = text2.get_rect()

textRect1.center = (100, 100)
textRect2.center = (100, 155)

freeze.blit(text1, textRect1)
freeze.blit(text2, textRect2)

# Update the display
pygame.display.update()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
