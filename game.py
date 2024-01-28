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

BIOME_GRID_ROWS = 4
BIOME_GRID_COLS = 2

BIOME_WIDTH = 608
BIOME_HEIGHT = 152
BIOME_MARGIN = 20  # Margin between biomes

PERSONALITIES = [
    "ANGRY",
    "SAD",
    "DISAPPOINTED",
    "JOVIAL",
    "MYSTERIOUS",
    "CURIOUS",
    "DOMINATING",
    "BOLD"
    "EXTROVERTED",
    "INTROVERTED",
    "SOCIABLE",
    "LOYAL",
    "AGREEABLE",
    "CONSCIENTIOUS",
    "NEUROTIC",
    "PLAYFUL",
    "LOVING",
    "OPTIMISTIC",
    "PESSIMISTIC",
    "TECHNICAL",
    "SPORTY",
    "LUDDITE",
]

TOGGLES_DOWN_LEFT = 600
TOGGLES_UP_LEFT = 1000
PERSONALITY_TOGGLE_TOP = 160
BG01_TOGGLE_TOP = 280
BG02_TOGGLE_TOP = 340

NUM_HUMANS = 1

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
BROWN = (139, 69, 19)

# Create the display surface
screen = pygame.display.set_mode(SCREEN_RECT)
pygame.display.set_caption("AI Laughs At You")

# Load the dirt texture
dirt_texture = pygame.image.load("dirt.png")
texture_rect = dirt_texture.get_rect()

# Create eight biomes, arranging the second set below the first
def create_biomes():
    biomes = []

    for row in range(BIOME_GRID_ROWS):
        for col in range(BIOME_GRID_COLS):
            x = (BIOME_MARGIN * (col + 1)) + col * BIOME_WIDTH
            y = (BIOME_MARGIN * (row + 1)) + row * BIOME_HEIGHT
            rect = pygame.Rect(
                (x, y),
                (BIOME_WIDTH, BIOME_HEIGHT)
            )
            biomes.append(rect)
    return biomes

def load_humans(num_humans):
    humans = []

    for i in range(1, num_humans + 1):
        filename = f"human-{i:03d}.png"
        print(filename)

        image = pygame.image.load(filename)
        #image.set_colorkey((255, 255, 255))
        humans.append(image)

    return humans


# Game state
grid_view = True
cur_human = 0

biomes = create_biomes()

humans = load_humans(NUM_HUMANS)

laugh_box = pygame.image.load("laugh-box-scaled.png")

current_personality_idx = 1
current_background01_idx = 0
current_background02_idx = 0

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
    text = font.render("DONE", True, BLACK)
    screen.blit(text, (SCREEN_WIDTH - BUTTON_WIDTH + 20, SCREEN_HEIGHT - BUTTON_HEIGHT + 10))

def draw_option_buttons(top):
    # Draw left arrow button
    pygame.draw.polygon(screen, GRAY, [(TOGGLES_DOWN_LEFT, top + 20), (TOGGLES_DOWN_LEFT + 20, top), (TOGGLES_DOWN_LEFT + 20, top + 40)])
    
    # Draw right arrow button
    pygame.draw.polygon(screen, GRAY, [(TOGGLES_UP_LEFT + 20, top + 20), (TOGGLES_UP_LEFT, top), (TOGGLES_UP_LEFT, top + 40)])
    
def draw_options():
    font = pygame.font.Font(None, 36)

    screen.blit(font.render("PERSONALITY", True, BLACK), (640, 128))
    personality_text = font.render(PERSONALITIES[current_personality_idx], True, GRAY)
    screen.blit(personality_text, (640, 168))

    screen.blit(font.render("BACKGROUND", True, BLACK), (640, 256))

    draw_option_buttons(PERSONALITY_TOGGLE_TOP)
    draw_option_buttons(BG01_TOGGLE_TOP)
    draw_option_buttons(BG02_TOGGLE_TOP)

def draw_human_edit_screen():
    screen.fill(WHITE)

    screen.blit(humans[cur_human], (48, 128))
    screen.blit(laugh_box, (0, 0))

    draw_options()

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

