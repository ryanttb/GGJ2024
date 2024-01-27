import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
FONT = pygame.font.Font(None, 36)

# Options
options = ["Option 1", "Option 2", "Option 3"]
current_option_index = 0

# Create a Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Options Screen")

left_arrow = pygame.Rect(50, 250, 50, 50)
right_arrow = pygame.Rect(700, 250, 50, 50)

def draw_buttons():
    # Draw left arrow button
    pygame.draw.polygon(screen, GRAY, [(60, 275), (80, 255), (80, 295)])
    
    # Draw right arrow button
    pygame.draw.polygon(screen, GRAY, [(710, 275), (690, 255), (690, 295)])

def draw_options():
    # Draw the currently selected option
    option_text = FONT.render(options[current_option_index], True, WHITE)
    screen.blit(option_text, (350, 275))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if left_arrow.collidepoint(event.pos):
                current_option_index = (current_option_index - 1) % len(options)
            elif right_arrow.collidepoint(event.pos):
                current_option_index = (current_option_index + 1) % len(options)

    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Draw buttons and options
    draw_buttons()
    draw_options()
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

