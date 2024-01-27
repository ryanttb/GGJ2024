import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BROWN = (139, 69, 19)  # Brown color in RGB
WHITE = (255, 255, 255)  # White color in RGB
RECT_WIDTH = 220
RECT_HEIGHT = 140
RECT_MARGIN = 20  # Margin between rectangles

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Clickable Rectangles")

# Create a list to store the rectangles
rectangles = []

# Create eight white rectangles, arranging the second set below the first
for i in range(8):
    if i < 4:
        rect = pygame.Rect(
            (i * (RECT_WIDTH + RECT_MARGIN) + RECT_MARGIN, SCREEN_HEIGHT // 2 - RECT_HEIGHT),
            (RECT_WIDTH, RECT_HEIGHT)
        )
    else:
        rect = pygame.Rect(
            ((i - 4) * (RECT_WIDTH + RECT_MARGIN) + RECT_MARGIN, SCREEN_HEIGHT // 2),
            (RECT_WIDTH, RECT_HEIGHT)
        )
    rectangles.append(rect)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for mouse clicks on rectangles
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, rect in enumerate(rectangles):
                if rect.collidepoint(event.pos):
                    print(f"Rectangle {i + 1} clicked!")

    # Fill the background with brown
    screen.fill(BROWN)

    # Draw the white rectangles
    for rect in rectangles:
        pygame.draw.rect(screen, WHITE, rect)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

