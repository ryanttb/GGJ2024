import sys
import pygame

# Init pygame & display
pygame.init()

screen_rect = (1280, 720)
screen = pygame.display.set_mode(screen_rect)
pygame.display.set_caption("Make Me Laugh")

num_humans = 2

def load_humans():
    humans = []

    for i in range(1, num_humans + 1):
        filename = f"human-{i:03d}.jpg"
        print(filename)

        image = pygame.image.load(filename)
        humans.append(image)

    return humans

# Load humans
humans = load_humans()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Your game logic goes here

    screen.fill((255, 255, 255))

    screen.blit(humans[1], (screen_rect[0] - humans[1].get_rect().width, 0))


    # Update the display
    pygame.display.flip()

pygame.quit()

