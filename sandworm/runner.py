"""Simple Endless Runner created in Pygame."""

import pygame
from sys import exit


# Global variables
game_title = "Runewood: Sprite Fright"
screen_width = 800
screen_height = 400
frame_rate = 60

# Must be called before any other pygame functions
pygame.init()

# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the window title
pygame.display.set_caption(game_title)

# Set the frame rate
clock = pygame.time.Clock()

test_surface = pygame.image.load("assets/images/test.png").convert_alpha()

# Game loop
while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface, (200, 100))

    # Update everything
    pygame.display.update()
    clock.tick(frame_rate)  # Frames per second