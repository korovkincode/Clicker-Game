# set up the library
import pygame
pygame.init()

# set up the drawing screen window
screen_resolution = (1240, 720)
screen = pygame.display.set_mode(screen_resolution)

# running the game until the user didn't quit
running = True
while running:

    # did the user quit?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill screen background with purple
    screen.fill((255, 255, 255))

    # flip the display
    pygame.display.flip()

# Done!
pygame.quit()
