import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
GRID_ROWS = 4
GRID_COLS = 2
CELL_WIDTH = SCREEN_WIDTH // GRID_COLS
CELL_HEIGHT = SCREEN_HEIGHT // GRID_ROWS
BORDER_SIZE = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)  # Brown color for the path

# Create the display surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Clickable Grid")

# Game state
grid_view = True

def draw_grid():
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            pygame.draw.rect(screen, BROWN, (col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))
            pygame.draw.rect(screen, WHITE, (col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), BORDER_SIZE)

def draw_back_button():
    pygame.draw.rect(screen, BROWN, (SCREEN_WIDTH - CELL_WIDTH, SCREEN_HEIGHT - CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))
    pygame.draw.rect(screen, GRAY, (SCREEN_WIDTH - CELL_WIDTH + BORDER_SIZE, SCREEN_HEIGHT - CELL_HEIGHT + BORDER_SIZE,
                                    CELL_WIDTH - 2 * BORDER_SIZE, CELL_HEIGHT - 2 * BORDER_SIZE))
    font = pygame.font.Font(None, 36)
    text = font.render("Back", True, BLACK)
    screen.blit(text, (SCREEN_WIDTH - CELL_WIDTH + 20, SCREEN_HEIGHT - CELL_HEIGHT + 10))

def draw_new_screen():
    screen.fill(BLACK)
    # Add elements for the new screen as needed
    draw_back_button()

def main():
    global grid_view

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                clicked_col = mouse_x // CELL_WIDTH
                clicked_row = mouse_y // CELL_HEIGHT

                if grid_view:
                    print(f"Clicked on cell ({clicked_col}, {clicked_row})")
                    grid_view = False
                else:
                    if SCREEN_WIDTH - CELL_WIDTH <= mouse_x <= SCREEN_WIDTH and SCREEN_HEIGHT - CELL_HEIGHT <= mouse_y <= SCREEN_HEIGHT:
                        grid_view = True

        if grid_view:
            screen.fill(BLACK)
            draw_grid()
        else:
            draw_new_screen()

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

