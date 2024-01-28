import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame Timer Example")

# Initialize variables
start_time = pygame.time.get_ticks()  # Get the current time in milliseconds
timer_interval = 5 * 1000  # 90 seconds in milliseconds
timer_event = pygame.USEREVENT + 1  # Custom event ID for the timer

# Create a custom event to be triggered every 90 seconds
pygame.time.set_timer(timer_event, timer_interval)

# Font and font size
font = pygame.font.Font(None, 36)

# List to store random numbers as strings and their positions
random_numbers = []

# Function to generate and store a random number as a string
def generate_random_number():
    number = str(random.randint(1, 100))  # Generate a random number between 1 and 100
    x = random.randint(0, WINDOW_WIDTH - 50)  # Random x-coordinate
    y = random.randint(0, WINDOW_HEIGHT - 50)  # Random y-coordinate
    random_numbers.append((number, x, y))  # Store the number and its position

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == timer_event:
            # This code will execute every 90 seconds
            print("Timer event triggered. Do something here.")
            generate_random_number()  # Generate a random number and store it

    # Clear the screen
    screen.fill(WHITE)

    # Draw random numbers on the screen
    for number, x, y in random_numbers:
        text_surface = font.render(number, True, BLACK)
        screen.blit(text_surface, (x, y))

    # Update the game logic and draw game objects here

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

