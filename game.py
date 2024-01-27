import pygame
import sys

# don't ruin my project, it's not worth it
# export GITHUB_TOKEN=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

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_RECT = (SCREEN_WIDTH, SCREEN_HEIGHT)
GRID_ROWS = 4
GRID_COLS = 2
CELL_WIDTH = SCREEN_WIDTH // GRID_COLS
CELL_HEIGHT = SCREEN_HEIGHT // GRID_ROWS
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50
BORDER_SIZE = 16

NUM_HUMANS = 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
BROWN = (139, 69, 19)  # Brown color for the path

# Create the display surface
screen = pygame.display.set_mode(SCREEN_RECT)
pygame.display.set_caption("AI Laughs At You")

# Load the dirt texture
dirt_texture = pygame.image.load("dirt.png")
texture_rect = dirt_texture.get_rect()

# Game state
grid_view = True
cur_human = 1
humans = []

def load_humans(num_humans):
    humans = []

    for i in range(1, num_humans + 1):
        filename = f"human-{i:03d}.jpg"
        print(filename)

        image = pygame.image.load(filename)
        humans.append(image)

    return humans

# Load humans
humans = load_humans(NUM_HUMANS)

def draw_path():
    for x in range(SCREEN_WIDTH // BORDER_SIZE):
        for y in range(SCREEN_HEIGHT // BORDER_SIZE):
            texture_rect.topleft = (x * BORDER_SIZE, y * BORDER_SIZE)
            screen.blit(dirt_texture, texture_rect)

def draw_grid():
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            pygame.draw.rect(screen, WHITE, (col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))
            pygame.draw.rect(screen, BROWN, (col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), BORDER_SIZE)

            for i in range(0, CELL_WIDTH // BORDER_SIZE):
                texture_rect.topleft = (col * CELL_WIDTH + (BORDER_SIZE * i), row * CELL_HEIGHT)
                screen.blit(dirt_texture, texture_rect)

                texture_rect.top = texture_rect.top + (CELL_HEIGHT * BORDER_SIZE)
                screen.blit(dirt_texture, texture_rect)

            for i in range(0, CELL_HEIGHT // BORDER_SIZE):
                texture_rect.topleft = (col * CELL_WIDTH, row * CELL_HEIGHT + (BORDER_SIZE * i))
                screen.blit(dirt_texture, texture_rect)

def draw_back_button():
    pygame.draw.rect(screen, GRAY, (SCREEN_WIDTH - BUTTON_WIDTH, SCREEN_HEIGHT - BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT))
    font = pygame.font.Font(None, 36)
    text = font.render("Back", True, BLACK)
    screen.blit(text, (SCREEN_WIDTH - BUTTON_WIDTH + 20, SCREEN_HEIGHT - BUTTON_HEIGHT + 10))

def draw_human_edit_screen():
    screen.fill(WHITE)
    # Add elements for the new screen as needed

    screen.blit(humans[cur_human], (SCREEN_RECT[0] - humans[cur_human].get_rect().width, 0))

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
                    if SCREEN_WIDTH - BUTTON_WIDTH <= mouse_x <= SCREEN_WIDTH and SCREEN_HEIGHT - BUTTON_HEIGHT <= mouse_y <= SCREEN_HEIGHT:
                        grid_view = True

        if grid_view:
            screen.fill(WHITE)
            #draw_path()
            draw_grid()
        else:
            draw_human_edit_screen()

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

