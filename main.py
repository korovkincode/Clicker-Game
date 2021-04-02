# set up the library
import pygame
pygame.init()

# set up the drawing screen window
screen_resolution = (1240, 720)
screen = pygame.display.set_mode(screen_resolution)

# fill screen background with white
screen.fill((255, 255, 255))

# set FPS limit
clock = pygame.time.Clock()
fps = 60

# All default colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)


# example of player
pygame.draw_circle(screen, YELLOW, (620, 360), 50)
direction = 5

# running the game until the user didn't quit
running = True
while running:

	# checking, whether the user quit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# flip the display
	pygame.display.flip()

	# set frames per second
	clock.tick(fps)

# Done!
pygame.quit()