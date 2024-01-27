import pygame

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Dirt Path Example')

# Load the dirt texture
dirt_texture = pygame.image.load("dirt.png")

# Resize the texture to 32x16 pixels
#dirt_texture = pygame.transform.scale(dirt_texture, (32, 16))

# Create a green surface
background = pygame.Surface((width, height))
background.fill((0, 255, 0))

# Define the coordinates for the dirt path
path_width = 16
path_start = (width // 2 - path_width // 2, 0)

# Repeat the dirt texture in the path
for x in range(path_start[0], width, path_width):
    background.blit(dirt_texture, (x, 0))

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

