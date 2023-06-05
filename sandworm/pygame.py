import pygame
import sys

# Initialize pygame and global variables
pygame.init()
window_width = 400
window_height = 500
framerate = 60
light_green = (175,215,70)

# Create pygame game window
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

while True:
    # Check if the user closed the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(light_green)
    screen.blit(background, (x_pos, y_pos))
    
    # Draw all our elements
    pygame.display.update()

    # Set framerate
    clock.tick(framerate)
    