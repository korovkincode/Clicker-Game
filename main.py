# set up the library
import pygame
pygame.init()

# set up the drawing screen window
screen_resolution = (1240, 720)
screen = pygame.display.set_mode(screen_resolution)
clock = pygame.time.Clock()
fps = 60

# running the game until the user didn't quit
running = True
while running:

	# checking, whether the user quit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# fill screen background with white
	screen.fill((255, 255, 255))

	# flip the display
	pygame.display.flip()

	# set frames per second
	clock.tick(fps)
	
# Done!
pygame.quit()