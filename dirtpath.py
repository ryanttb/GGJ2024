import random
import pygame

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Dirt Path Example')

# Define colors
green = (0, 255, 0)
brown = (139, 69, 19)
dark_brown = (101, 51, 12)

# Create a green surface
background = pygame.Surface((width, height))
background.fill(green)

# Define the coordinates for the dirt path
path_width = 200
path_start = (width // 2 - path_width // 2, 0)
path_end = (width // 2 + path_width // 2, height)

# Draw a solid brown path
pygame.draw.rect(background, brown, (path_start, (path_width, height)))

# Add some darker brown accents to the path
for i in range(50):
    x = pygame.Rect(path_start, (path_width, height)).centerx + pygame.Rect(path_start, (path_width, height)).width // 4
    y = random.randint(0, height)
    pygame.draw.circle(background, dark_brown, (x, y), 2)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background onto the screen
    screen.blit(background, (0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

