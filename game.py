import sys
import random
import pygame

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
    "ANGRY",        # 00
    "JOVIAL",       # 01
    "MYSTERIOUS",   # 02
    #"SAD",          # 03
    #"CURIOUS",      # 04
    #"DOMINATING",   # 05
    #"SPORTY",       # 06
    #"EXTROVERTED",  # 07
    #"INTROVERTED",  # 08
    #"DISAPPOINTED", # 09
    #"SOCIABLE",     # 10
    #"LOYAL",        # 11
    #"AGREEABLE",    # 12
    #"CONSCIENTIOUS",# 13
    #"NEUROTIC",     # 14
    #"PLAYFUL",      # 15
    #"LOVING",       # 16
    #"OPTIMISTIC",   # 17
    #"PESSIMISTIC",  # 18
    #"TECHNICAL",    # 19
    #"BOLD",         # 20
    #"LUDDITE",      # 21
    #"CLUMSY",       # 22
]

BG01S = [
    "CIRCUS PERFORMER", #00
    "ARTIST",           #01
    "DIPLOMAT",         #02
    "STEAMBOAT CAPTAIN",#03
    #"ASTRONAUT",        #04
    #"NOBLE",            #05
    #"ALCHEMIST",        #06
    #"ORPHAN",           #07
    #"GLADIATOR",        #08
    #"ASTRONOMER",       #09
]

BG02S = [
    "TURNED ADVENTURER",    #00
    "RAISED BY WOLVES",     #01 
    "TURNED REBEL LEADER",  #02
    "SEEKING VENGEANCE",    #03
    #"SEEKING REDEMPTION",   #05
    #"WITH PROPHECY POWERS", #06
]

ALL_COMMENTS = {
    (0, 0, 0): [
        "You think this is tough? Try walking a tightrope over a pit of lions while angry! Now THAT was an adventure!",
		"I used to juggle flaming torches for a living, and now I'm dealing with these ridiculous monsters? What a circus my life has become!",
		"These dungeons are like a never-ending clown car of surprises. Just when you think you've seen it all, out pops another ridiculous creature!",
		"I'll show those monsters what a real 'big top' is all about! Prepare to be amazed, you overgrown carnival rejects!",
		"I've tamed lions, tigers, and bears in the circus, but these dungeons are a whole different kind of animal!",
		"Step right up, folks! Watch me turn these foes into confetti with my trusty sword! It's all in a day's work for a circus performer turned adventurer!",
    ],
    (0, 0, 1): [
        "I may have been raised by wolves, but I'll be damned if I let anyone treat me like an animal!",

        "My circus skills might seem wild, but they're nothing compared to the instincts I learned in the wilderness!",

        "Being raised by wolves toughened me up for anything life throws at me, whether it's performing under the big top or battling monsters in the forest.",

        "I howled at the moon with my wolf family, and now I'll howl with fury at anyone who stands in my way!",

        "I may have the heart of a circus performer, but I've got the ferocity of a wolf. Together, I'm a force to be reckoned with!",
    ],
    (0, 0, 2): [
        "I once commanded the spotlight in the circus ring, but now I lead a different kind of show – a rebellion against the tyrants!",

        "I've swapped my juggling balls for battle tactics, and these rebels are about to witness the greatest performance of their lives!",

        "In the circus, I entertained the masses. Now, I inspire them to rise up and fight for their freedom!",

        "Circus tricks may have been my past, but leading this rebellion is my destiny!",

        "I used to tame lions, but now I'm taming a nation's hunger for justice. Watch out, oppressors, this circus performer is leading the charge!",
    ],
    (0, 0, 3): [
        "They thought they could ruin my circus and get away with it? Well, they're about to witness the most spectacular revenge act of all time!",

        "The circus was my life, and they took it away from me. Now, it's time to make them pay for every laugh they stole.",

        "I used to bring joy to crowds, but now I'll bring vengeance to those who wronged me!",

        "They clowned around with my dreams, but now it's their turn to face the consequences!",

        "I've traded in my circus costume for a cloak of vengeance, and I won't stop until I've settled the score!",
    ],
    (0, 1, 0): [
        "My anger fuels my creativity, and now I'm channeling it into the most epic adventures the world has ever seen!",

        "I used to paint with a brush, but now I'm sketching my adventures with a sword in hand!",

        "The canvas couldn't contain my passion anymore, so I decided to paint my own destiny as an adventurer.",

        "They called me a temperamental artist, but they've yet to see the true masterpiece of my life – my adventures!",

        "I may have left my art studio behind, but the world itself has become my canvas, and my adventures are my greatest works of art!",
    ],
    (0, 1, 1): [
        "Raised by wolves, I bring the raw, untamed fury of the wilderness into my art and my adventures.",

        "The howling of wolves echoes in my heart, guiding me as I create and conquer in this wild world.",

        "In the solitude of the wolf pack, I found a connection to nature that now shapes my artistic expression and my daring adventures.",

        "They called my art 'savage,' but I'll show them what true savagery looks like when I'm on a quest!",

        "The wilderness and artistry run deep in my veins, and now I'm using both to leave my mark on the world as an adventurer."
    ],
    (0, 1, 2): [
        "I once painted my emotions, but now I lead a rebellion, and every stroke of my rebellion is a brushstroke against oppression.",

        "Art used to be my sanctuary, but now I've turned my canvas into a battle standard, and my rebellion will be a masterpiece of justice.",

        "They thought I was just an artist, but little did they know, my artistry would inspire a revolution.",

        "I've traded my easel for a sword, and my passion for justice now drives my rebellion forward!",

        "My art was a whisper, but my rebellion is a roar that will echo through the annals of history!",
    ],
    (0, 1, 3): [
        "My brush once painted serenity, but now it will craft a portrait of vengeance so vivid it will haunt those who wronged me.",

        "My art used to be a reflection of my soul, but now it's a mirror that shows my enemies the face of their own destruction.",

        "They thought they could destroy my creations and get away with it? Well, they're about to witness the wrath of a scorned artist!",

        "Every stroke of my revenge is a stroke of retribution, and I won't rest until my masterpiece of vengeance is complete.",

        "The art of revenge is a canvas I'm eager to paint upon, and the colors I'll use will be shades of despair and regret!",
    ],
    (0, 2, 0): [
        "Diplomacy failed to resolve the issues, so now I'm taking matters into my own hands as an adventurer!",

        "I once negotiated peace, but now I'm prepared to fight for it, one battle at a time.",

        "They said I was too soft-spoken for the political arena, but they've yet to witness the determination of an angry diplomat turned adventurer.",

        "The world of diplomacy may be filled with empty promises, but in the world of adventure, I'll create my destiny.",

        "I've left the conference room behind for the thrill of the unknown. As an adventurer, I'll find the answers diplomacy couldn't provide.",
    ],
    (0, 2, 1): [
        "Raised by wolves, I bring the wisdom of the pack into the world of diplomacy. Now, my negotiations have the strength of the wild!",

        "The howls of my wolf family echo in my heart as I navigate the political wilderness, seeking to bring balance and justice.",

        "The diplomatic world may be a jungle, but the lessons I learned from my wolf pack have made me a fearless negotiator.",

        "They thought I was just a soft-spoken diplomat, but little did they know that the wilderness taught me the true art of diplomacy.",

        "The diplomatic game may be a cunning one, but my upbringing with wolves has taught me to be a cunning diplomat, ready to pounce when necessary!",
    ],
    (0, 2, 2): [
        "I once brokered peace, but now I lead a rebellion against tyranny. My negotiations have turned into battles for justice!",

        "Diplomacy couldn't bring the change we needed, so I'm using my skills to lead a rebellion that will shake the foundations of power.",

        "They underestimated the passion of a diplomat pushed too far. Now, I'm leading a rebellion that will rewrite the rules.",

        "My diplomacy may have been refined, but my resolve as a rebel leader is unyielding. It's time to overthrow the oppressors.",

        "I used to negotiate behind closed doors, but now I negotiate with fists and swords, leading this rebellion to a brighter future!",
    ],
    (0, 2, 3): [
        "They thought diplomacy was my only weapon, but now they'll see the ferocity of a diplomat seeking vengeance!",

        "My diplomatic skills were once used to foster peace, but now they're directed towards a different goal – revenge!",

        "They crossed the wrong diplomat, and now I'll use every resource at my disposal to exact my vengeance.",

        "I once negotiated treaties, but now I'll negotiate the terms of their downfall!",

        "I'll use the art of diplomacy to weave a web of vengeance so intricate, they won't even see it coming!",
    ],
    (0, 3, 0): [
        "I once navigated the rivers with my steamboat, but now I'm charting new courses as a fearless adventurer!",

        "The river used to be my domain, but now I seek uncharted waters and untamed lands in my quest for adventure.",

        "They called me the captain of the steamboat, but I've set sail on the grandest adventure of my life!",

        "From the steam to the wild, I've traded in my captain's hat for an adventurer's heart.",

        "My steamboat used to be my home, but now the world itself is my domain, and adventure is my calling!",
    ],
    (0, 3, 1): [
        "Raised by wolves and captain of the steamboat – a unique blend of wilderness instincts and river mastery!",

        "My life was divided between the untamed wilderness and the mighty river, and now I combine both as an adventurer.",

        "I may have been raised by wolves, but I ruled the river with my steamboat, and now I rule the wilderness with my anger.",

        "The river currents couldn't wash away the wildness in my blood. Now, my adventures are as unpredictable as the wolves that raised me.",

        "The wolves taught me survival, and the steamboat taught me mastery. Together, they make me a force to be reckoned with in the world of adventure!",
    ],
    (0, 3, 2): [
        "I once commanded the mighty steamboat, but now I'm steering the ship of rebellion against those who oppress us!",

        "I've traded my steamboat's helm for a rebellion's banner, and I'll lead our cause with the same determination I had navigating treacherous waters.",

        "The river was my kingdom, but now I'm on a mission to reclaim our land from the tyrants who seized it.",

        "From the helm of a steamboat to the helm of a revolution – they never saw this transformation coming!",

        "I used to transport cargo, but now I transport the hopes and dreams of those who fight alongside me in this rebellion!",
    ],
    (0, 3, 3): [
        "They thought they could sink my steamboat and get away with it? Well, they're about to face the wrath of a steamboat captain seeking vengeance!",

        "I navigated the waters with finesse, but now I'll navigate the treacherous path of vengeance to make them pay for what they did!",

        "The river may have been calm under my command, but now I'm unleashing a storm of vengeance upon those who wronged me.",

        "I'll steamroll my way through obstacles to exact my revenge, just like I steered my steamboat through rough currents!",

        "The steam that once powered my boat now fuels the fires of vengeance burning within me. They won't escape the reckoning!",
    ],
    (1, 0, 0): [
        "The circus was all laughter and smiles, and now I'm bringing that same joy to the world as an adventurer!",

        "I might not have a trapeze anymore, but my acrobatic skills sure come in handy during our daring quests!",

        "Life under the big top was a blast, but life on the open road as an adventurer? That's a whole new level of excitement!",

        "I used to make people laugh with my clown act, and now I'm making them laugh with my daring escapades!",

        "They say life is a circus, and I'm just taking that circus on the road, one adventure at a time!",
    ],
    (1, 0, 1): [
    ],
    (1, 0, 2): [
    ],
    (1, 0, 3): [
    ],
    (1, 1, 0): [
    ],
    (1, 1, 1): [
        "I used to mix potions to find happiness. Now, I'm just mixing them to find a way to say sorry."
    ],
    (1, 1, 2): [
    ],
    (1, 1, 3): [
    ],
    (1, 2, 0): [
    ],
    (1, 2, 1): [
    ],
    (1, 2, 2): [
    ],
    (1, 2, 3): [
    ],
    (1, 3, 0): [
    ],
    (1, 3, 1): [
    ],
    (1, 3, 2): [
    ],
    (1, 3, 3): [
    ],
    (1, 3, 0): [
    ],
    (1, 3, 1): [
    ],
    (1, 3, 2): [
    ],
    (1, 3, 3): [
    ],
    (1, 4, 0): [
    ],
    (1, 4, 1): [
    ],
    (1, 4, 2): [
    ],
    (1, 4, 3): [
    ],
    (1, 5, 0): [
    ],
    (1, 5, 1): [
    ],
    (1, 5, 2): [
    ],
    (1, 5, 3): [
    ],
    (1, 6, 0): [
    ],
    (1, 6, 1): [
    ],
    (1, 6, 2): [
    ],
    (1, 6, 3): [
    ],
    (1, 7, 0): [
    ],
    (1, 7, 1): [
    ],
    (1, 7, 2): [
    ],
    (1, 7, 3): [
    ],
    (1, 8, 0): [
    ],
    (1, 8, 1): [
    ],
    (1, 8, 2): [
    ],
    (1, 8, 3): [
    ],
    (2, 0, 0): [
    ],
    (2, 0, 1): [
    ],
    (2, 0, 2): [
    ],
    (2, 0, 3): [
    ],
    (2, 1, 0): [
    ],
    (2, 1, 1): [
    ],
    (2, 1, 2): [
    ],
    (2, 1, 3): [
    ],
    (2, 2, 0): [
    ],
    (2, 2, 1): [
    ],
    (2, 2, 2): [
    ],
    (2, 2, 3): [
    ],
    (2, 3, 0): [
    ],
    (2, 3, 1): [
    ],
    (2, 3, 2): [
    ],
    (2, 3, 3): [
    ],
    (2, 3, 0): [
    ],
    (2, 3, 1): [
    ],
    (2, 3, 2): [
    ],
    (2, 3, 3): [
    ],
    (2, 4, 0): [
    ],
    (2, 4, 1): [
    ],
    (2, 4, 2): [
    ],
    (2, 4, 3): [
    ],
    (2, 5, 0): [
    ],
    (2, 5, 1): [
    ],
    (2, 5, 2): [
    ],
    (2, 5, 3): [
    ],
    (2, 6, 0): [
    ],
    (2, 6, 1): [
    ],
    (2, 6, 2): [
    ],
    (2, 6, 3): [
    ],
    (2, 7, 0): [
    ],
    (2, 7, 1): [
    ],
    (2, 7, 2): [
    ],
    (2, 7, 3): [
    ],
    (2, 8, 0): [
    ],
    (2, 8, 1): [
    ],
    (2, 8, 2): [
    ],
    (2, 8, 3): [
    ],
}

TOGGLES_WIDTH = 50
TOGGLES_HEIGHT = 50
TOGGLES_DOWN_LEFT = 600
TOGGLES_UP_LEFT = 1000
PERSONALITY_TOGGLE_TOP = 160
BG01_TOGGLE_TOP = 280
BG02_TOGGLE_TOP = 340

HUMAN_IN_BOX_OFFSET = (92, 128)
HUMAN_WIDTH = 256
NUM_HUMANS = 8

TIMER_INTERVAL = 1 * 1000 # new comment every 10s
COMMENT_TIMER_EVENT = pygame.USEREVENT + 1

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
BROWN = (139, 69, 19)

# Create the display surface
screen = pygame.display.set_mode(SCREEN_RECT)
pygame.display.set_caption("AI Laughs At You")

# Comments and timer stuff
start_tiem = pygame.time.get_ticks()
pygame.time.set_timer(COMMENT_TIMER_EVENT, TIMER_INTERVAL)

# Load the dirt texture
dirt_texture = pygame.image.load("dirt.png")
texture_rect = dirt_texture.get_rect()

# General font for the options
options_font = pygame.font.Font(None, 36)

# Comment font
comment_font = pygame.font.Font(None, 24)

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
            biomes.append({
                "rect": rect, 
                "human": -1,
                "personality": (-1, -1, -1),
                "comment": "",
                "comment_ttl": -1,
                "comment_idx": 0
            })
    return biomes

def load_humans(num_humans):
    humans = []

    for i in range(1, num_humans + 1):
        file_i = i % 2
        filename = f"human-{file_i:03d}.png"
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

cur_personality_idx = 0
cur_bg01_idx = 0
cur_bg02_idx = 0

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

def wrap_text(text, font, max_width):
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = current_line + [word]
        test_size = font.size(' '.join(test_line))

        if test_size[0] <= max_width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))

    return lines

# side is 0 = left, 1 = right
def render_and_display_wrapped_text(side, text, font, max_width, starting_pos):
    wrapped_lines = wrap_text(text, font, max_width)
    rendered_lines = [font.render(line, True, BLACK) for line in wrapped_lines]

    y = 0 # starting y position

    for rendered_line in rendered_lines:
        if side == 0:
            screen.blit(rendered_line, (starting_pos[0], y + starting_pos[1]))
        else:
            screen.blit(rendered_line, (starting_pos[0] + (HUMAN_WIDTH // 4), y + starting_pos[1]))

        y += font.get_linesize()

def draw_biomes():
    for i, obj in enumerate(biomes):
        pygame.draw.rect(screen, WHITE, obj["rect"])
        if obj["human"] != -1:
            image = humans[obj["human"]]
            desired_height = obj["rect"].height // 2
            original_width, original_height = image.get_size()
            aspect_ratio = original_width / original_height
            new_width = int(desired_height * aspect_ratio)
            scaled_image = pygame.transform.scale(image, (new_width, desired_height))

            if (i % 2) == 0:
                screen.blit(scaled_image, (obj["rect"].left + BIOME_WIDTH - new_width - BIOME_MARGIN, obj["rect"].top + BIOME_HEIGHT // 4))
            else:
                flipped_image = pygame.transform.flip(scaled_image, True, False)
                screen.blit(flipped_image, (obj["rect"].left + BIOME_MARGIN, obj["rect"].top + BIOME_HEIGHT // 4))

            if obj["comment"] != "":
                render_and_display_wrapped_text(i % 2, obj["comment"], comment_font, BIOME_WIDTH - HUMAN_WIDTH, (obj["rect"].left + BIOME_MARGIN, obj["rect"].top + BIOME_MARGIN))
                #comment = comment_font.render(obj["comment"], True, BLACK)
                #screen.blit(comment, (obj["rect"].left + BIOME_MARGIN, obj["rect"].top + BIOME_MARGIN))

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
    screen.blit(options_font.render("PERSONALITY", True, BLACK), (640, 128))
    personality_text = options_font.render(PERSONALITIES[cur_personality_idx], True, GRAY)
    screen.blit(personality_text, (640, 168))

    screen.blit(options_font.render("BACKGROUND", True, BLACK), (640, 256))
    bg01_text = options_font.render(BG01S[cur_bg01_idx], True, GRAY)
    screen.blit(bg01_text, (640, 290))
    bg02_text = options_font.render(BG02S[cur_bg02_idx], True, GRAY)
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

# Add a random comment to a zooman
def add_comment():
    for i, obj in enumerate(biomes):
        if obj["human"] != -1:
            if obj["comment_ttl"] <= 0:
                comments = ALL_COMMENTS.get(obj["personality"])
                if comments is not None:
                    print(obj["comment_idx"])
                    if len(comments) > obj["comment_idx"]:
                        print(comments[obj["comment_idx"]])
                        obj["comment"] = comments[obj["comment_idx"]]
                        obj["comment_ttl"] = random.randint(0, 8)
                        obj["comment_idx"] = (obj["comment_idx"] + 1) % len(comments)
                break
            else:
                obj["comment_ttl"] = obj["comment_ttl"] - 1
                if obj["comment_ttl"] <= 1:
                    obj["comment"] = ""


    return

def main():
    global grid_view
    global cur_human
    global cur_personality_idx
    global cur_bg01_idx
    global cur_bg02_idx

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == COMMENT_TIMER_EVENT and grid_view:
                add_comment()

            # Check for mouse clicks on biomes
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if grid_view:
                    if cur_human != NUM_HUMANS:
                        for i, obj in enumerate(biomes):
                            if obj["rect"].collidepoint(event.pos):
                                print(f"Biome {i} clicked!")
                                if obj["human"] == -1:
                                    cur_biome = i
                                    grid_view = False
                                else:
                                    print(obj["personality"])
                                    comment = ALL_COMMENTS.get(obj["personality"])
                                    if comment is not None:
                                        print(comment[0])

                else: # Laugh Box
                    cur_personality_idx = check_option(event, personality_down_arrow, personality_up_arrow, cur_personality_idx , PERSONALITIES)
                    cur_bg01_idx = check_option(event, bg01_down_arrow, bg01_up_arrow, cur_bg01_idx , BG01S)
                    cur_bg02_idx = check_option(event, bg02_down_arrow, bg02_up_arrow, cur_bg02_idx , BG02S)

                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if SCREEN_WIDTH - BUTTON_WIDTH <= mouse_x <= SCREEN_WIDTH and SCREEN_HEIGHT - BUTTON_HEIGHT <= mouse_y <= SCREEN_HEIGHT:
                        biomes[cur_biome]["human"] = cur_human
                        biomes[cur_biome]["personality"] = (cur_personality_idx, cur_bg01_idx, cur_bg02_idx)
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
