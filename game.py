import pygame
import sys

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
    "BOLD",
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

BG01S = [
    "CIRCUS PERFORMER",
    "ALCHEMIST",
    "ORPHAN",
    "ASTRONAUT",
    "NOBLE",
    "ARTIST",
    "DIPLOMAT",
    "GLADIATOR",
    "ASTRONOMER",
    "STEAMBOAT CAPTAIN",
]

BG02S = [
    "TURNED ADVENTURER",
    "SEEKING REDEMPTION",
    "RAISED BY THIEVES",
    "TURNED REBEL LEADER",
    "SEEKING VENGEANCE",
    "WITH PROPHECY POWERS",
]

TOGGLES_WIDTH = 50
TOGGLES_HEIGHT = 50
TOGGLES_DOWN_LEFT = 600
TOGGLES_UP_LEFT = 1000
PERSONALITY_TOGGLE_TOP = 160
BG01_TOGGLE_TOP = 280
BG02_TOGGLE_TOP = 340

HUMAN_IN_BOX_OFFSET = (92, 128)
NUM_HUMANS = 2

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

# Laugh box image
laugh_box = pygame.image.load("laugh-box-scaled.png")

# Arrow rects
personality_down_arrow = pygame.Rect(TOGGLES_DOWN_LEFT, PERSONALITY_TOGGLE_TOP, TOGGLES_WIDTH, TOGGLES_HEIGHT)
personality_up_arrow = pygame.Rect(TOGGLES_UP_LEFT, PERSONALITY_TOGGLE_TOP, TOGGLES_WIDTH, TOGGLES_HEIGHT)

bg01_down_arrow = pygame.Rect(TOGGLES_DOWN_LEFT, BG01_TOGGLE_TOP, TOGGLES_WIDTH, TOGGLES_HEIGHT)
bg01_up_arrow = pygame.Rect(TOGGLES_UP_LEFT, BG01_TOGGLE_TOP, TOGGLES_WIDTH, TOGGLES_HEIGHT)

bg02_down_arrow = pygame.Rect(TOGGLES_DOWN_LEFT, BG02_TOGGLE_TOP, TOGGLES_WIDTH, TOGGLES_HEIGHT)
bg02_up_arrow = pygame.Rect(TOGGLES_UP_LEFT, BG02_TOGGLE_TOP, TOGGLES_WIDTH, TOGGLES_HEIGHT)

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
            biomes.append({"idx": (row * BIOME_GRID_COLS + col), "rect": rect, "human": -1})
    return biomes

def load_humans(num_humans):
    humans = []

    for i in range(1, num_humans + 1):
        filename = f"human-{i:03d}.png"
        print(filename)

        image = pygame.image.load(filename)
        humans.append(image)

    return humans


# Game state
grid_view = True
cur_human = 0
cur_biome = -1

biomes = create_biomes()

humans = load_humans(NUM_HUMANS)

current_personality_idx = 0
current_bg01_idx = 0
current_bg02_idx = 0

def check_option(event, down, up, idx, values):
    if down.collidepoint(event.pos):
        if (idx == 0):
            idx = len(values) - 1
        else:
            idx = (idx - 1) % len(values)
    elif up.collidepoint(event.pos):
        idx = (idx + 1) % len(values)

    return idx

def draw_path():
    for x in range(SCREEN_WIDTH // PATH_SPRITE_SIZE):
        for y in range(SCREEN_HEIGHT // PATH_SPRITE_SIZE):
            texture_rect.topleft = (x * PATH_SPRITE_SIZE, y * PATH_SPRITE_SIZE)
            screen.blit(dirt_texture, texture_rect)

def draw_biomes():
    for obj in biomes:
        pygame.draw.rect(screen, WHITE, obj["rect"])
        if obj["human"] != -1:
            image = humans[obj["human"]]
            desired_height = obj["rect"].height // 2
            original_width, original_height = image.get_size()
            aspect_ratio = original_width / original_height
            new_width = int(desired_height * aspect_ratio)
            scaled_image = pygame.transform.scale(image, (new_width, desired_height))

            if (obj["idx"] % 2) == 0:
                screen.blit(scaled_image, (obj["rect"].left + BIOME_WIDTH - new_width, obj["rect"].top + BIOME_HEIGHT // 4))
            else:
                screen.blit(scaled_image, (obj["rect"].left, obj["rect"].top + BIOME_HEIGHT // 4))

def draw_back_button():
    pygame.draw.rect(screen, GRAY, (SCREEN_WIDTH - BUTTON_WIDTH, SCREEN_HEIGHT - BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT))
    font = pygame.font.Font(None, 36)
    text = font.render("DONE", True, BLACK)
    screen.blit(text, (SCREEN_WIDTH - BUTTON_WIDTH + 20, SCREEN_HEIGHT - BUTTON_HEIGHT + 10))

def draw_option_buttons(down, up):
    # Draw toggle down button
    pygame.draw.polygon(screen, GRAY, [(down.left, down.top + 20), (down.left + 20, down.top), (down.left + 20, down.top + 40)])
    
    # Draw toggle up button
    pygame.draw.polygon(screen, GRAY, [(up.left + 20, up.top + 20), (up.left, up.top), (up.left, up.top + 40)])
    
def draw_options():
    font = pygame.font.Font(None, 36)

    screen.blit(font.render("PERSONALITY", True, BLACK), (640, 128))
    personality_text = font.render(PERSONALITIES[current_personality_idx], True, GRAY)
    screen.blit(personality_text, (640, 168))

    screen.blit(font.render("BACKGROUND", True, BLACK), (640, 256))
    bg01_text = font.render(BG01S[current_bg01_idx], True, GRAY)
    screen.blit(bg01_text, (640, 290))
    bg02_text = font.render(BG02S[current_bg02_idx], True, GRAY)
    screen.blit(bg02_text, (640, 350))

    draw_option_buttons(personality_down_arrow, personality_up_arrow)
    draw_option_buttons(bg01_down_arrow, bg01_up_arrow)
    draw_option_buttons(bg02_down_arrow, bg02_up_arrow)

def draw_human_edit_screen():
    screen.fill(WHITE)

    screen.blit(humans[cur_human], HUMAN_IN_BOX_OFFSET)
    screen.blit(laugh_box, (0, 0))

    draw_options()

    draw_back_button()

def main():
    global grid_view
    global cur_human
    global current_personality_idx
    global current_bg01_idx
    global current_bg02_idx

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check for mouse clicks on biomes
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if grid_view:
                    if cur_human != NUM_HUMANS:
                        for i, obj in enumerate(biomes):
                            if obj["rect"].collidepoint(event.pos):
                                print(f"Biome {i} clicked!")
                                cur_biome = i
                                grid_view = False
                else: # Laugh Box
                    current_personality_idx = check_option(event, personality_down_arrow, personality_up_arrow, current_personality_idx , PERSONALITIES)
                    current_bg01_idx = check_option(event, bg01_down_arrow, bg01_up_arrow, current_bg01_idx , BG01S)
                    current_bg02_idx = check_option(event, bg02_down_arrow, bg02_up_arrow, current_bg02_idx , BG02S)

                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if SCREEN_WIDTH - BUTTON_WIDTH <= mouse_x <= SCREEN_WIDTH and SCREEN_HEIGHT - BUTTON_HEIGHT <= mouse_y <= SCREEN_HEIGHT:
                        biomes[cur_biome]["human"] = cur_human
                        cur_human += 1
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

