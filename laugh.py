import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display dimensions
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Laugh-O-Meter")

# Load the PNG image
image = pygame.image.load("laugh-o-meter2.png")

# Get the image's rect and center it on the screen
image_rect = image.get_rect()
image_rect.center = (screen_width // 2, 120)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the image on the screen
    screen.blit(image, image_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

