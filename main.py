# set up the library
import pygame
pygame.init()

# set up the drawing screen window
screen_resolution = (626, 375)
screen = pygame.display.set_mode(screen_resolution)
clock = pygame.time.Clock()

class Player:
	def __init__(self, x, y, hp = 100, speed = 3.5):
		self.x = x
		self.y = y
		self.hp = hp
		self.speed = speed
		self.direction = 0

# set up the background and the player
player_img = [pygame.image.load("player.png"), pygame.image.load("mirrored_player.png")]
background_img = pygame.image.load("background.jpg")

# set up the player movement
player = Player(x = 0, y = 230)

# running the game until the user didn't quit
running = True
while running:
	
	# checking, whether the user quit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# player movement
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and player.x > 0:
		player.x -= player.speed
		player.direction = 1
	elif keys[pygame.K_RIGHT] and player.x < 589:
		player.x += player.speed
		player.direction = 0

	# drawing the background and the player
	screen.blit(background_img, (0, 0))
	screen.blit(player_img[player.direction], (player.x, player.y))

	# flip the display
	pygame.display.flip()

	# set up fps
	clock.tick(60)

# Done!
pygame.quit()
