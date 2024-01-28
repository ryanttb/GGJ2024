import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_RECT = (SCREEN_WIDTH, SCREEN_HEIGHT)
FONT_SIZE = 36
FONT_COLOR = (255, 255, 255)  # White

# Create the Pygame screen
screen = pygame.display.set_mode(SCREEN_RECT)
pygame.display.set_caption("Centered Emoji Text Example")

# Create a font object using a font that includes emoji characters
font_path = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"  # Adjust the path as needed
font_size = 36
font = pygame.font.Font(font_path, font_size)


# Text to display (a smiley emoji)
text = "😊"

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Render the text
    text_surface = font.render(text, True, FONT_COLOR)

    # Calculate the position to center the text horizontally
    text_rect = text_surface.get_rect()
    text_rect.centerx = SCREEN_WIDTH // 2
    text_rect.y = 20  # You can adjust the Y-coordinate to control the vertical position

    # Blit the text onto the screen
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

