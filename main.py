# set up the library
import pygame
pygame.init()

# set up the drawing screen window
screen_resolution = (626, 375)
screen = pygame.display.set_mode(screen_resolution)
clock = pygame.time.Clock()

# set up the background and the player
player = [pygame.image.load("player.png"), pygame.image.load("mirrored_player.png")]
background = pygame.image.load("background.jpg")
direction = 0  # 0 -- right, 1 -- left

# set up the player movement
x = 0
y = 230
speed = 3.5

# running the game until the user didn't quit
running = True
while running:
	# set up fps
	clock.tick(60)

	# checking, whether the user quit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# player movement
	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x > 0:
		x -= speed
		direction = 1
	elif keys[pygame.K_RIGHT] and x < 589:
		x += speed
		direction = 0

	# drawing the background and the player
	screen.blit(background, (0, 0))
	screen.blit(player[direction], (x, y))

	# flip the display
	pygame.display.flip()

# Done!
pygame.quit()
