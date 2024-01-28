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
    "SAD",          # 01
    "DISAPPOINTED", # 02
    "JOVIAL",       # 03
    "MYSTERIOUS",   # 04
    "CURIOUS",      # 05
    "DOMINATING",   # 06
    "SPORTY",       # 07
    "EXTROVERTED",  # 08
    "INTROVERTED",  # 09
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
    "ALCHEMIST",        #01
    "ORPHAN",           #02
    "ASTRONAUT",        #03
    "NOBLE",            #04
    "ARTIST",           #05
    "DIPLOMAT",         #06
    "GLADIATOR",        #07
    "ASTRONOMER",       #08
    "STEAMBOAT CAPTAIN",#09
]

BG02S = [
    "TURNED ADVENTURER",    #00
    "SEEKING REDEMPTION",   #01
    "RAISED BY WOLVES",     #02 
    "TURNED REBEL LEADER",  #03
    "SEEKING VENGEANCE",    #04
    "WITH PROPHECY POWERS", #05
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
        "I swear, if I don't find redemption soon, I'll unleash my circus lion on you!"
    ],
    (0, 0, 2): [
    ],
    (0, 0, 3): [
    ],
    (0, 0, 4): [
    ],
    (0, 0, 5): [
        "My prophecy powers foretell a clown car full of angry clowns. Be afraid!"
    ],
    (0, 1, 0): [
    ],
    (0, 1, 1): [
    ],
    (0, 1, 2): [
    ],
    (0, 1, 3): [
    ],
    (0, 1, 4): [
    ],
    (0, 1, 5): [
    ],
    (0, 2, 0): [
    ],
    (0, 2, 1): [
    ],
    (0, 2, 2): [
    ],
    (0, 2, 3): [
    ],
    (0, 2, 4): [
    ],
    (0, 2, 5): [
    ],
    (0, 3, 0): [
    ],
    (0, 3, 1): [
    ],
    (0, 3, 2): [
    ],
    (0, 3, 3): [
    ],
    (0, 3, 4): [
    ],
    (0, 3, 5): [
    ],
    (0, 3, 0): [
    ],
    (0, 3, 1): [
    ],
    (0, 3, 2): [
    ],
    (0, 3, 3): [
    ],
    (0, 3, 4): [
    ],
    (0, 3, 5): [
    ],
    (0, 4, 0): [
    ],
    (0, 4, 1): [
    ],
    (0, 4, 2): [
    ],
    (0, 4, 3): [
    ],
    (0, 4, 4): [
    ],
    (0, 4, 5): [
    ],
    (0, 5, 0): [
    ],
    (0, 5, 1): [
    ],
    (0, 5, 2): [
    ],
    (0, 5, 3): [
    ],
    (0, 5, 4): [
    ],
    (0, 5, 5): [
    ],
    (0, 6, 0): [
    ],
    (0, 6, 1): [
    ],
    (0, 6, 2): [
    ],
    (0, 6, 3): [
    ],
    (0, 6, 4): [
    ],
    (0, 6, 5): [
    ],
    (0, 7, 0): [
    ],
    (0, 7, 1): [
    ],
    (0, 7, 2): [
    ],
    (0, 7, 3): [
    ],
    (0, 7, 4): [
    ],
    (0, 7, 5): [
    ],
    (0, 8, 0): [
    ],
    (0, 8, 1): [
    ],
    (0, 8, 2): [
    ],
    (0, 8, 3): [
    ],
    (0, 8, 4): [
    ],
    (0, 8, 5): [
    ],
    (0, 9, 0): [
    ],
    (0, 9, 1): [
    ],
    (0, 9, 2): [
    ],
    (0, 9, 3): [
    ],
    (0, 9, 4): [
    ],
    (0, 9, 5): [
    ],
    (1, 0, 0): [
    ],
    (1, 0, 1): [
    ],
    (1, 0, 2): [
    ],
    (1, 0, 3): [
    ],
    (1, 0, 4): [
    ],
    (1, 0, 5): [
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
    (1, 1, 4): [
    ],
    (1, 1, 5): [
    ],
    (1, 2, 0): [
    ],
    (1, 2, 1): [
    ],
    (1, 2, 2): [
    ],
    (1, 2, 3): [
    ],
    (1, 2, 4): [
    ],
    (1, 2, 5): [
    ],
    (1, 3, 0): [
    ],
    (1, 3, 1): [
    ],
    (1, 3, 2): [
    ],
    (1, 3, 3): [
    ],
    (1, 3, 4): [
    ],
    (1, 3, 5): [
    ],
    (1, 3, 0): [
    ],
    (1, 3, 1): [
    ],
    (1, 3, 2): [
    ],
    (1, 3, 3): [
    ],
    (1, 3, 4): [
    ],
    (1, 3, 5): [
    ],
    (1, 4, 0): [
    ],
    (1, 4, 1): [
    ],
    (1, 4, 2): [
    ],
    (1, 4, 3): [
    ],
    (1, 4, 4): [
    ],
    (1, 4, 5): [
    ],
    (1, 5, 0): [
    ],
    (1, 5, 1): [
    ],
    (1, 5, 2): [
    ],
    (1, 5, 3): [
    ],
    (1, 5, 4): [
    ],
    (1, 5, 5): [
    ],
    (1, 6, 0): [
    ],
    (1, 6, 1): [
    ],
    (1, 6, 2): [
    ],
    (1, 6, 3): [
    ],
    (1, 6, 4): [
    ],
    (1, 6, 5): [
    ],
    (1, 7, 0): [
    ],
    (1, 7, 1): [
    ],
    (1, 7, 2): [
    ],
    (1, 7, 3): [
    ],
    (1, 7, 4): [
    ],
    (1, 7, 5): [
    ],
    (1, 8, 0): [
    ],
    (1, 8, 1): [
    ],
    (1, 8, 2): [
    ],
    (1, 8, 3): [
    ],
    (1, 8, 4): [
    ],
    (1, 8, 5): [
    ],
    (1, 9, 0): [
    ],
    (1, 9, 1): [
    ],
    (1, 9, 2): [
    ],
    (1, 9, 3): [
    ],
    (1, 9, 4): [
    ],
    (1, 9, 5): [
    ],
    (2, 0, 0): [
    ],
    (2, 0, 1): [
    ],
    (2, 0, 2): [
    ],
    (2, 0, 3): [
    ],
    (2, 0, 4): [
    ],
    (2, 0, 5): [
    ],
    (2, 1, 0): [
    ],
    (2, 1, 1): [
    ],
    (2, 1, 2): [
    ],
    (2, 1, 3): [
    ],
    (2, 1, 4): [
    ],
    (2, 1, 5): [
    ],
    (2, 2, 0): [
    ],
    (2, 2, 1): [
    ],
    (2, 2, 2): [
    ],
    (2, 2, 3): [
    ],
    (2, 2, 4): [
    ],
    (2, 2, 5): [
    ],
    (2, 3, 0): [
    ],
    (2, 3, 1): [
    ],
    (2, 3, 2): [
    ],
    (2, 3, 3): [
    ],
    (2, 3, 4): [
    ],
    (2, 3, 5): [
    ],
    (2, 3, 0): [
    ],
    (2, 3, 1): [
    ],
    (2, 3, 2): [
    ],
    (2, 3, 3): [
    ],
    (2, 3, 4): [
    ],
    (2, 3, 5): [
    ],
    (2, 4, 0): [
    ],
    (2, 4, 1): [
    ],
    (2, 4, 2): [
    ],
    (2, 4, 3): [
    ],
    (2, 4, 4): [
    ],
    (2, 4, 5): [
    ],
    (2, 5, 0): [
    ],
    (2, 5, 1): [
    ],
    (2, 5, 2): [
    ],
    (2, 5, 3): [
    ],
    (2, 5, 4): [
    ],
    (2, 5, 5): [
    ],
    (2, 6, 0): [
    ],
    (2, 6, 1): [
    ],
    (2, 6, 2): [
    ],
    (2, 6, 3): [
    ],
    (2, 6, 4): [
    ],
    (2, 6, 5): [
    ],
    (2, 7, 0): [
    ],
    (2, 7, 1): [
    ],
    (2, 7, 2): [
    ],
    (2, 7, 3): [
    ],
    (2, 7, 4): [
    ],
    (2, 7, 5): [
    ],
    (2, 8, 0): [
    ],
    (2, 8, 1): [
    ],
    (2, 8, 2): [
    ],
    (2, 8, 3): [
    ],
    (2, 8, 4): [
    ],
    (2, 8, 5): [
    ],
    (2, 9, 0): [
    ],
    (2, 9, 1): [
    ],
    (2, 9, 2): [
    ],
    (2, 9, 3): [
    ],
    (2, 9, 4): [
    ],
    (2, 9, 5): [
    ],
    (3, 0, 0): [
    ],
    (3, 0, 1): [
    ],
    (3, 0, 2): [
    ],
    (3, 0, 3): [
    ],
    (3, 0, 4): [
    ],
    (3, 0, 5): [
    ],
    (3, 1, 0): [
    ],
    (3, 1, 1): [
    ],
    (3, 1, 2): [
    ],
    (3, 1, 3): [
    ],
    (3, 1, 4): [
    ],
    (3, 1, 5): [
    ],
    (3, 2, 0): [
    ],
    (3, 2, 1): [
    ],
    (3, 2, 2): [
    ],
    (3, 2, 3): [
    ],
    (3, 2, 4): [
    ],
    (3, 2, 5): [
    ],
    (3, 3, 0): [
    ],
    (3, 3, 1): [
    ],
    (3, 3, 2): [
    ],
    (3, 3, 3): [
        "From the stars to the bars! Leading a rebellion with a smile, one small step at a time!"
    ],
    (3, 3, 4): [
    ],
    (3, 3, 5): [
    ],
    (3, 3, 0): [
    ],
    (3, 3, 1): [
    ],
    (3, 3, 2): [
    ],
    (3, 3, 3): [
    ],
    (3, 3, 4): [
    ],
    (3, 3, 5): [
    ],
    (3, 4, 0): [
    ],
    (3, 4, 1): [
    ],
    (3, 4, 2): [
    ],
    (3, 4, 3): [
    ],
    (3, 4, 4): [
    ],
    (3, 4, 5): [
    ],
    (3, 5, 0): [
    ],
    (3, 5, 1): [
    ],
    (3, 5, 2): [
    ],
    (3, 5, 3): [
    ],
    (3, 5, 4): [
    ],
    (3, 5, 5): [
    ],
    (3, 6, 0): [
    ],
    (3, 6, 1): [
    ],
    (3, 6, 2): [
    ],
    (3, 6, 3): [
    ],
    (3, 6, 4): [
    ],
    (3, 6, 5): [
    ],
    (3, 7, 0): [
    ],
    (3, 7, 1): [
    ],
    (3, 7, 2): [
    ],
    (3, 7, 3): [
    ],
    (3, 7, 4): [
    ],
    (3, 7, 5): [
    ],
    (3, 8, 0): [
    ],
    (3, 8, 1): [
    ],
    (3, 8, 2): [
    ],
    (3, 8, 3): [
    ],
    (3, 8, 4): [
    ],
    (3, 8, 5): [
    ],
    (3, 9, 0): [
    ],
    (3, 9, 1): [
    ],
    (3, 9, 2): [
    ],
    (3, 9, 3): [
    ],
    (3, 9, 4): [
    ],
    (3, 9, 5): [
    ],
    (4, 0, 0): [
    ],
    (4, 0, 1): [
    ],
    (4, 0, 2): [
    ],
    (4, 0, 3): [
    ],
    (4, 0, 4): [
    ],
    (4, 0, 5): [
    ],
    (4, 1, 0): [
    ],
    (4, 1, 1): [
    ],
    (4, 1, 2): [
    ],
    (4, 1, 3): [
    ],
    (4, 1, 4): [
    ],
    (4, 1, 5): [
    ],
    (4, 2, 0): [
    ],
    (4, 2, 1): [
    ],
    (4, 2, 2): [
    ],
    (4, 2, 3): [
    ],
    (4, 2, 4): [
    ],
    (4, 2, 5): [
    ],
    (4, 3, 0): [
    ],
    (4, 3, 1): [
    ],
    (4, 3, 2): [
    ],
    (4, 3, 3): [
    ],
    (4, 3, 4): [
    ],
    (4, 3, 5): [
    ],
    (4, 3, 0): [
    ],
    (4, 3, 1): [
    ],
    (4, 3, 2): [
    ],
    (4, 3, 3): [
    ],
    (4, 3, 4): [
    ],
    (4, 3, 5): [
    ],
    (4, 4, 0): [
    ],
    (4, 4, 1): [
    ],
    (4, 4, 2): [
    ],
    (4, 4, 3): [
    ],
    (4, 4, 4): [
        "A noble by day, a vengeance seeker by night. My life’s more twisted than a royal family tree."
    ],
    (4, 4, 5): [
    ],
    (4, 5, 0): [
    ],
    (4, 5, 1): [
    ],
    (4, 5, 2): [
    ],
    (4, 5, 3): [
    ],
    (4, 5, 4): [
    ],
    (4, 5, 5): [
    ],
    (4, 6, 0): [
    ],
    (4, 6, 1): [
    ],
    (4, 6, 2): [
    ],
    (4, 6, 3): [
    ],
    (4, 6, 4): [
    ],
    (4, 6, 5): [
    ],
    (4, 7, 0): [
    ],
    (4, 7, 1): [
    ],
    (4, 7, 2): [
    ],
    (4, 7, 3): [
    ],
    (4, 7, 4): [
    ],
    (4, 7, 5): [
    ],
    (4, 8, 0): [
    ],
    (4, 8, 1): [
    ],
    (4, 8, 2): [
    ],
    (4, 8, 3): [
    ],
    (4, 8, 4): [
    ],
    (4, 8, 5): [
    ],
    (4, 9, 0): [
    ],
    (4, 9, 1): [
    ],
    (4, 9, 2): [
    ],
    (4, 9, 3): [
    ],
    (4, 9, 4): [
    ],
    (4, 9, 5): [
    ],
    (5, 0, 0): [
    ],
    (5, 0, 1): [
    ],
    (5, 0, 2): [
    ],
    (5, 0, 3): [
    ],
    (5, 0, 4): [
    ],
    (5, 0, 5): [
    ],
    (5, 1, 0): [
    ],
    (5, 1, 1): [
    ],
    (5, 1, 2): [
    ],
    (5, 1, 3): [
    ],
    (5, 1, 4): [
    ],
    (5, 1, 5): [
    ],
    (5, 2, 0): [
    ],
    (5, 2, 1): [
    ],
    (5, 2, 2): [
    ],
    (5, 2, 3): [
    ],
    (5, 2, 4): [
    ],
    (5, 2, 5): [
    ],
    (5, 3, 0): [
    ],
    (5, 3, 1): [
    ],
    (5, 3, 2): [
    ],
    (5, 3, 3): [
    ],
    (5, 3, 4): [
    ],
    (5, 3, 5): [
    ],
    (5, 3, 0): [
    ],
    (5, 3, 1): [
    ],
    (5, 3, 2): [
    ],
    (5, 3, 3): [
    ],
    (5, 3, 4): [
    ],
    (5, 3, 5): [
    ],
    (5, 4, 0): [
    ],
    (5, 4, 1): [
    ],
    (5, 4, 2): [
    ],
    (5, 4, 3): [
    ],
    (5, 4, 4): [
    ],
    (5, 4, 5): [
    ],
    (5, 5, 0): [
    ],
    (5, 5, 1): [
    ],
    (5, 5, 2): [
    ],
    (5, 5, 3): [
    ],
    (5, 5, 4): [
    ],
    (5, 5, 5): [
        "I see a future where my art is famous... or was that just another odd dream?"
    ],
    (5, 6, 0): [
    ],
    (5, 6, 1): [
    ],
    (5, 6, 2): [
    ],
    (5, 6, 3): [
    ],
    (5, 6, 4): [
    ],
    (5, 6, 5): [
    ],
    (5, 7, 0): [
    ],
    (5, 7, 1): [
    ],
    (5, 7, 2): [
    ],
    (5, 7, 3): [
    ],
    (5, 7, 4): [
    ],
    (5, 7, 5): [
    ],
    (5, 8, 0): [
    ],
    (5, 8, 1): [
    ],
    (5, 8, 2): [
    ],
    (5, 8, 3): [
    ],
    (5, 8, 4): [
    ],
    (5, 8, 5): [
    ],
    (5, 9, 0): [
    ],
    (5, 9, 1): [
    ],
    (5, 9, 2): [
    ],
    (5, 9, 3): [
    ],
    (5, 9, 4): [
        "I've sailed the seas, but now I'm on a quest for revenge. Ever fought a pirate captain with a steamboat?",
        "I'm curious to see how my vengeance quest ends. Maybe with a steam-powered cannonball to their ship!",
    ],
    (5, 9, 5): [
    ],
    (6, 0, 0): [
    ],
    (6, 0, 1): [
    ],
    (6, 0, 2): [
    ],
    (6, 0, 3): [
    ],
    (6, 0, 4): [
    ],
    (6, 0, 5): [
    ],
    (6, 1, 0): [
    ],
    (6, 1, 1): [
    ],
    (6, 1, 2): [
    ],
    (6, 1, 3): [
    ],
    (6, 1, 4): [
    ],
    (6, 1, 5): [
    ],
    (6, 2, 0): [
    ],
    (6, 2, 1): [
    ],
    (6, 2, 2): [
    ],
    (6, 2, 3): [
    ],
    (6, 2, 4): [
    ],
    (6, 2, 5): [
    ],
    (6, 3, 0): [
    ],
    (6, 3, 1): [
    ],
    (6, 3, 2): [
    ],
    (6, 3, 3): [
    ],
    (6, 3, 4): [
    ],
    (6, 3, 5): [
    ],
    (6, 3, 0): [
    ],
    (6, 3, 1): [
    ],
    (6, 3, 2): [
    ],
    (6, 3, 3): [
    ],
    (6, 3, 4): [
    ],
    (6, 3, 5): [
    ],
    (6, 4, 0): [
    ],
    (6, 4, 1): [
    ],
    (6, 4, 2): [
    ],
    (6, 4, 3): [
    ],
    (6, 4, 4): [
    ],
    (6, 4, 5): [
    ],
    (6, 5, 0): [
    ],
    (6, 5, 1): [
    ],
    (6, 5, 2): [
    ],
    (6, 5, 3): [
    ],
    (6, 5, 4): [
    ],
    (6, 5, 5): [
    ],
    (6, 6, 0): [
        "I went from debating in palaces to commanding in the wild. My word is still law, anywhere."
    ],
    (6, 6, 1): [
    ],
    (6, 6, 2): [
    ],
    (6, 6, 3): [
    ],
    (6, 6, 4): [
    ],
    (6, 6, 5): [
    ],
    (6, 7, 0): [
    ],
    (6, 7, 1): [
    ],
    (6, 7, 2): [
    ],
    (6, 7, 3): [
    ],
    (6, 7, 4): [
    ],
    (6, 7, 5): [
    ],
    (6, 8, 0): [
    ],
    (6, 8, 1): [
    ],
    (6, 8, 2): [
    ],
    (6, 8, 3): [
    ],
    (6, 8, 4): [
    ],
    (6, 8, 5): [
    ],
    (6, 9, 0): [
    ],
    (6, 9, 1): [
    ],
    (6, 9, 2): [
    ],
    (6, 9, 3): [
    ],
    (6, 9, 4): [
    ],
    (6, 9, 5): [
    ],
    (7, 0, 0): [
    ],
    (7, 0, 1): [
    ],
    (7, 0, 2): [
    ],
    (7, 0, 3): [
    ],
    (7, 0, 4): [
    ],
    (7, 0, 5): [
    ],
    (7, 1, 0): [
    ],
    (7, 1, 1): [
    ],
    (7, 1, 2): [
    ],
    (7, 1, 3): [
    ],
    (7, 1, 4): [
    ],
    (7, 1, 5): [
    ],
    (7, 2, 0): [
    ],
    (7, 2, 1): [
    ],
    (7, 2, 2): [
    ],
    (7, 2, 3): [
    ],
    (7, 2, 4): [
    ],
    (7, 2, 5): [
    ],
    (7, 3, 0): [
    ],
    (7, 3, 1): [
    ],
    (7, 3, 2): [
    ],
    (7, 3, 3): [
    ],
    (7, 3, 4): [
    ],
    (7, 3, 5): [
    ],
    (7, 3, 0): [
    ],
    (7, 3, 1): [
    ],
    (7, 3, 2): [
    ],
    (7, 3, 3): [
    ],
    (7, 3, 4): [
    ],
    (7, 3, 5): [
    ],
    (7, 4, 0): [
    ],
    (7, 4, 1): [
    ],
    (7, 4, 2): [
    ],
    (7, 4, 3): [
    ],
    (7, 4, 4): [
    ],
    (7, 4, 5): [
    ],
    (7, 5, 0): [
    ],
    (7, 5, 1): [
    ],
    (7, 5, 2): [
    ],
    (7, 5, 3): [
    ],
    (7, 5, 4): [
    ],
    (7, 5, 5): [
    ],
    (7, 6, 0): [
    ],
    (7, 6, 1): [
    ],
    (7, 6, 2): [
    ],
    (7, 6, 3): [
    ],
    (7, 6, 4): [
    ],
    (7, 6, 5): [
    ],
    (7, 7, 0): [
    ],
    (7, 7, 1): [
    ],
    (7, 7, 2): [
    ],
    (7, 7, 3): [
    ],
    (7, 7, 4): [
    ],
    (7, 7, 5): [
    ],
    (7, 8, 0): [
    ],
    (7, 8, 1): [
    ],
    (7, 8, 2): [
    ],
    (7, 8, 3): [
    ],
    (7, 8, 4): [
    ],
    (7, 8, 5): [
    ],
    (7, 9, 0): [
    ],
    (7, 9, 1): [
    ],
    (7, 9, 2): [
    ],
    (7, 9, 3): [
    ],
    (7, 9, 4): [
    ],
    (7, 9, 5): [
    ],
    (8, 0, 0): [
    ],
    (8, 0, 1): [
    ],
    (8, 0, 2): [
    ],
    (8, 0, 3): [
    ],
    (8, 0, 4): [
    ],
    (8, 0, 5): [
    ],
    (8, 1, 0): [
    ],
    (8, 1, 1): [
    ],
    (8, 1, 2): [
    ],
    (8, 1, 3): [
    ],
    (8, 1, 4): [
    ],
    (8, 1, 5): [
    ],
    (8, 2, 0): [
    ],
    (8, 2, 1): [
    ],
    (8, 2, 2): [
    ],
    (8, 2, 3): [
    ],
    (8, 2, 4): [
    ],
    (8, 2, 5): [
    ],
    (8, 3, 0): [
    ],
    (8, 3, 1): [
    ],
    (8, 3, 2): [
    ],
    (8, 3, 3): [
    ],
    (8, 3, 4): [
    ],
    (8, 3, 5): [
    ],
    (8, 3, 0): [
    ],
    (8, 3, 1): [
    ],
    (8, 3, 2): [
    ],
    (8, 3, 3): [
    ],
    (8, 3, 4): [
    ],
    (8, 3, 5): [
    ],
    (8, 4, 0): [
    ],
    (8, 4, 1): [
    ],
    (8, 4, 2): [
    ],
    (8, 4, 3): [
    ],
    (8, 4, 4): [
    ],
    (8, 4, 5): [
    ],
    (8, 5, 0): [
    ],
    (8, 5, 1): [
    ],
    (8, 5, 2): [
    ],
    (8, 5, 3): [
    ],
    (8, 5, 4): [
    ],
    (8, 5, 5): [
    ],
    (8, 6, 0): [
    ],
    (8, 6, 1): [
    ],
    (8, 6, 2): [
    ],
    (8, 6, 3): [
    ],
    (8, 6, 4): [
    ],
    (8, 6, 5): [
    ],
    (8, 7, 0): [
    ],
    (8, 7, 1): [
    ],
    (8, 7, 2): [
    ],
    (8, 7, 3): [
    ],
    (8, 7, 4): [
    ],
    (8, 7, 5): [
    ],
    (8, 8, 0): [
    ],
    (8, 8, 1): [
        "I used to watch stars, now I'm collecting good deeds. Brightening my own galaxy, one act at a time!"
    ],
    (8, 8, 2): [
    ],
    (8, 8, 3): [
    ],
    (8, 8, 4): [
    ],
    (8, 8, 5): [
    ],
    (8, 9, 0): [
    ],
    (8, 9, 1): [
    ],
    (8, 9, 2): [
    ],
    (8, 9, 3): [
    ],
    (8, 9, 4): [
    ],
    (8, 9, 5): [
    ],
    (9, 0, 0): [
    ],
    (9, 0, 1): [
    ],
    (9, 0, 2): [
    ],
    (9, 0, 3): [
    ],
    (9, 0, 4): [
    ],
    (9, 0, 5): [
    ],
    (9, 1, 0): [
    ],
    (9, 1, 1): [
    ],
    (9, 1, 2): [
    ],
    (9, 1, 3): [
    ],
    (9, 1, 4): [
    ],
    (9, 1, 5): [
    ],
    (9, 2, 0): [
    ],
    (9, 2, 1): [
    ],
    (9, 2, 2): [
    ],
    (9, 2, 3): [
    ],
    (9, 2, 4): [
    ],
    (9, 2, 5): [
    ],
    (9, 3, 0): [
    ],
    (9, 3, 1): [
    ],
    (9, 3, 2): [
    ],
    (9, 3, 3): [
    ],
    (9, 3, 4): [
    ],
    (9, 3, 5): [
    ],
    (9, 3, 0): [
    ],
    (9, 3, 1): [
    ],
    (9, 3, 2): [
    ],
    (9, 3, 3): [
    ],
    (9, 3, 4): [
    ],
    (9, 3, 5): [
    ],
    (9, 4, 0): [
    ],
    (9, 4, 1): [
    ],
    (9, 4, 2): [
    ],
    (9, 4, 3): [
    ],
    (9, 4, 4): [
    ],
    (9, 4, 5): [
    ],
    (9, 5, 0): [
    ],
    (9, 5, 1): [
    ],
    (9, 5, 2): [
    ],
    (9, 5, 3): [
    ],
    (9, 5, 4): [
    ],
    (9, 5, 5): [
    ],
    (9, 6, 0): [
    ],
    (9, 6, 1): [
    ],
    (9, 6, 2): [
    ],
    (9, 6, 3): [
    ],
    (9, 6, 4): [
    ],
    (9, 6, 5): [
    ],
    (9, 7, 0): [
    ],
    (9, 7, 1): [
    ],
    (9, 7, 2): [
    ],
    (9, 7, 3): [
    ],
    (9, 7, 4): [
    ],
    (9, 7, 5): [
    ],
    (9, 8, 0): [
    ],
    (9, 8, 1): [
    ],
    (9, 8, 2): [
    ],
    (9, 8, 3): [
    ],
    (9, 8, 4): [
    ],
    (9, 8, 5): [
    ],
    (9, 9, 0): [
    ],
    (9, 9, 1): [
    ],
    (9, 9, 2): [
    ],
    (9, 9, 3): [
    ],
    (9, 9, 4): [
    ],
    (9, 9, 5): [
        "I can predict the future, but I still can't find the courage to talk to my crew about it."
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
