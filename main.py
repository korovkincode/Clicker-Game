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
fps = 30

# All default colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)


# example of player
coord_x, coord_y = 620, 360
pygame.draw.circle(screen, YELLOW, (coord_x, coord_y), 50)
direction = 0

# running the game until the user didn't quit
running = True
while running:
	# handle every event
	for event in pygame.event.get():

		# checking, whether the user quit
		if event.type == pygame.QUIT:
			running = False

	keys_pressed = pygame.key.get_pressed()
	# move	
	if keys_pressed[pygame.K_d]:
		print('Key D pressed')
		if direction == -3:
			direction = 0
		else:
			direction = 3
	if keys_pressed[pygame.K_a]:
		print('Key A pressed')
		if direction == 3:
			direction = 0
		else:
			direction = -3
	pygame.draw.circle(screen, WHITE, (coord_x, coord_y), 50)
	coord_x += direction
	pygame.draw.circle(screen, YELLOW, (coord_x, coord_y), 50)
	# flip the display
	pygame.display.flip()

	# set frames per second
	clock.tick(fps)

# Done!
pygame.quit()