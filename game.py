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

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50

PATH_SPRITE_SIZE = 16

BIOME_WIDTH = 280
BIOME_HEIGHT = 160
BIOME_MARGIN = 20  # Margin between biomes

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

# Create eight biomes, arranging the second set below the first
def create_biomes():
    biomes = []
    for i in range(8):
        if i < 4:
            rect = pygame.Rect(
                (i * (BIOME_WIDTH + BIOME_MARGIN) + BIOME_MARGIN, SCREEN_HEIGHT // 4 - BIOME_HEIGHT),
                (BIOME_WIDTH, BIOME_HEIGHT)
            )
        else:
            rect = pygame.Rect(
                ((i - 4) * (BIOME_WIDTH + BIOME_MARGIN) + BIOME_MARGIN, (SCREEN_HEIGHT // 2) + BIOME_MARGIN),
                (BIOME_WIDTH, BIOME_HEIGHT)
            )
        biomes.append(rect)
    return biomes

def load_humans(num_humans):
    humans = []

    for i in range(1, num_humans + 1):
        filename = f"human-{i:03d}.jpg"
        print(filename)

        image = pygame.image.load(filename)
        humans.append(image)

    return humans


# Game state
grid_view = True
cur_human = 1

biomes = create_biomes()

humans = load_humans(NUM_HUMANS)

def draw_path():
    for x in range(SCREEN_WIDTH // PATH_SPRITE_SIZE):
        for y in range(SCREEN_HEIGHT // PATH_SPRITE_SIZE):
            texture_rect.topleft = (x * PATH_SPRITE_SIZE, y * PATH_SPRITE_SIZE)
            screen.blit(dirt_texture, texture_rect)

def draw_biomes():
    for rect in biomes:
        pygame.draw.rect(screen, WHITE, rect)

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

            # Check for mouse clicks on biomes
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if grid_view:
                    for i, rect in enumerate(biomes):
                        if rect.collidepoint(event.pos):
                            print(f"Biome {i} clicked!")
                            grid_view = False
                else:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if SCREEN_WIDTH - BUTTON_WIDTH <= mouse_x <= SCREEN_WIDTH and SCREEN_HEIGHT - BUTTON_HEIGHT <= mouse_y <= SCREEN_HEIGHT:
                        grid_view = True

        if grid_view:
            screen.fill(WHITE)
            draw_path()
            draw_biomes()
        else:
            draw_human_edit_screen()

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

