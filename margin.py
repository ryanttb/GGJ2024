import pygame

# Constants
WIDTH, HEIGHT = 800, 600
GRID_WIDTH, GRID_HEIGHT = 2, 4
CELL_SIZE = 100  # Adjust as needed
MARGIN = 16

# Colors
BROWN = (139, 69, 19)  # Brown color in RGB

def draw_background(screen):
    screen.fill(BROWN)

def draw_grid(screen):
    cell_width = (WIDTH - 2 * MARGIN) // GRID_WIDTH
    cell_height = (HEIGHT - 2 * MARGIN) // GRID_HEIGHT

    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            x = MARGIN + col * cell_width
            y = MARGIN + row * cell_height
            pygame.draw.rect(screen, (0, 0, 0), (x, y, cell_width, cell_height), 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Grid with Brown Background")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_background(screen)
        draw_grid(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

