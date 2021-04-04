# set up the library
import pygame
pygame.init()

# set up the drawing screen window
screen_resolution = [626, 375]
player_size = [37, 57]
screen = pygame.display.set_mode(screen_resolution)
clock = pygame.time.Clock()

class Ground:
	def __init__(self, x, y, width):
		self.xstart = x
		self.xend = x + width
		self.y = y

	def isTouch(self, obj):
		if obj.x >= self.xstart and obj.x <= self.xend and obj.y == self.y:
			return True
		return False

class Player:
	def __init__(self, x, y, hp = 100, speed = 3.5):
		self.x = x # X position
		self.y = y # Y position
		self.hp = hp # Health Points
		self.speed = speed # Speed
		self.direction = 0 # Direction(0 -> east, 1 -> west)
		self.jumpH = 90 # player max jump height
		self.jumptime = 0 # air time
		self.isFalling = False
		self.isJumping = False

ground = [Ground(0, 230, 626)]

# set up the background and the player
player_img = [pygame.image.load("static/player.png"), pygame.image.load("static/mirrored_player.png")]
background_img = pygame.image.load("static/background.jpg")

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
	elif keys[pygame.K_RIGHT] and player.x < screen_resolution[0] - player_size[0]:
		player.x += player.speed
		player.direction = 0
	if keys[pygame.K_UP] and player.y + player.jumpH < screen_resolution[1]:
		if not player.isJumping and not player.isFalling:
			player.isJumping = True

	# if player in jump
	if player.isJumping:
		if player.jumptime + 5 <= player.jumpH:
			player.y -= 5
			player.jumptime += 5
		else:
			player.jumptime = 0
			player.isJumping = False
			player.isFalling = True

	# if player is falling
	if player.isFalling:
		touched = False
		for gr in ground: # if player touches ground -> he stops falling
			if gr.isTouch(player):
				touched = True
		if not touched:
			player.y += 5
		else:
			player.isFalling = False

	# drawing the background and the player
	screen.blit(background_img, (0, 0))
	screen.blit(player_img[player.direction], (player.x, player.y))

	# flip the display
	pygame.display.flip()

	# set up fps
	clock.tick(60)

# Done!
pygame.quit()
