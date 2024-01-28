import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame Timer Example")

# Initialize variables
start_time = pygame.time.get_ticks()  # Get the current time in milliseconds
timer_interval = 5 * 1000  # 90 seconds in milliseconds
timer_event = pygame.USEREVENT + 1  # Custom event ID for the timer

# Create a custom event to be triggered every 90 seconds
pygame.time.set_timer(timer_event, timer_interval)

# List to store rectangles
rectangles = []

# Function to draw a rectangle at a random location
def draw_random_rectangle():
    x = random.randint(0, WINDOW_WIDTH - 50)  # Random x-coordinate
    y = random.randint(0, WINDOW_HEIGHT - 50)  # Random y-coordinate
    rectangles.append(pygame.Rect(x, y, 50, 50))  # Add a rectangle to the list

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == timer_event:
            # This code will execute every 90 seconds
            print("Timer event triggered. Do something here.")
            draw_random_rectangle()  # Draw a random rectangle

    # Clear the screen
    screen.fill(WHITE)

    # Draw all rectangles
    for rect in rectangles:
        pygame.draw.rect(screen, RED, rect)

    # Update the game logic and draw game objects here

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

