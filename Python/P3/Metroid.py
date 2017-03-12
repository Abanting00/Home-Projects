import pygame	
import random


#Global Variables -- Colors (set as a tuple) and Screen Size
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

#Classes --- Player, Metroid, Spaceship, Effects, Bullets

class Spaceship(pygame.sprite.Sprite):
	"""This class represent the spaceships that the player attacks"""
	
	def __init__(self): #Constructor, creates the spaceships
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load("block.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.x_speed = random.randrange(-5,5)
		self.y_speed = random.randrange(-5,5)

	def update(self):

		if self.rect.x > 700 or self.rect.x < 10:
			self.x_speed *= -1
		if self.rect.y > 400 or self.rect.y < 0:
			self.y_speed *= -1

		
		
		self.rect.x += self.x_speed
		self.rect.y += self.y_speed

class Metroid(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load("circle.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.x_speed = random.randrange(-50,50,25)
		self.y_speed = random.randrange(-50,50,25)

	def update(self):

		if self.rect.x > 700 or self.rect.x < 10:
			self.x_speed *= -1
		if self.rect.y > 400 or self.rect.y < 0:
			self.y_speed *= -1
				
		self.rect.x += self.x_speed
		self.rect.y += self.y_speed

class Player(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load("Player.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.x_speed = 0

	def update(self):
		"""Updates Player Position based on keyboard"""
		if self.rect.x > 650:
			self.x_speed = 0
			self.rect.x -= 3
		else:
			self.rect.x += self.x_speed

class Bullet(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load("player_bullet.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()

	def update(self):

		self.rect.y -= 30    #speed of the bullet going up

class Game(object):
	"""Creates an instance of the game. Every new game we just need to create a new
		intance of this class."""

	def __init__(self):  #Constructor with attributes and game initialization
		
		self.score = 0
		self.game_over = False
		self.x_speed = 0

		#Create sprite Lists
		self.ship_list = pygame.sprite.Group()
		self.bullet_list = pygame.sprite.Group()
		self.all_sprites_list = pygame.sprite.Group()

		#Addition of the metroid
		#self.metroid_list = pygame.sprite.Group()

		for i in range(10):
			metroid = Metroid()

			metroid.rect.x = random.randrange(SCREEN_WIDTH)
			metroid.rect.y = random.randrange(400)

			self.ship_list.add(metroid)
			self.all_sprites_list.add(metroid)

		for i in range(10):
			ship = Spaceship()

			ship.rect.x = random.randrange(SCREEN_WIDTH)
			ship.rect.y = random.randrange(400)

			self.ship_list.add(ship)
			self.all_sprites_list.add(ship)

		#Creates the player
		self.player = Player()
		self.all_sprites_list.add(self.player)
		self.player.rect.y = 450

	def process_events(self):

		click_sound = pygame.mixer.Sound("laser5.ogg")
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True

			if event.type == pygame.MOUSEBUTTONDOWN:
				if self.game_over:
					self.__init__()

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_SPACE:
					bullet = Bullet()
					bullet.rect.x = self.player.rect.x + 46
					bullet.rect.y = self.player.rect.y

					self.all_sprites_list.add(bullet)
					self.bullet_list.add(bullet)

					click_sound.play()
				if event.key == pygame.K_LEFT:
					self.player.x_speed = -10
				if event.key == pygame.K_RIGHT:
					self.player.x_speed = 10

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					self.player.x_speed = 0
				if event.key == pygame.K_RIGHT:
					self.player.x_speed = 0

	def run_logic(self):

		if not self.game_over:
			self.all_sprites_list.update()

		self.player.update()

		for bullet in self.bullet_list:
			bullet_hit_list = pygame.sprite.spritecollide(bullet,self.ship_list,True)

			for hit in bullet_hit_list:
				self.bullet_list.remove(bullet)
				self.all_sprites_list.remove(bullet)
				self.score += 1
				print(self.score)

			if bullet.rect.y < -10:
				self.bullet_list.remove(bullet)

			if len(self.ship_list) == 0:
				self.game_over = True
		

	def display_frame(self,screen):
		background_image = pygame.image.load("space.jpg").convert()
		screen.blit(background_image,[0,0])

		if self.game_over:
			font = pygame.font.Font("C:/Windows/Fonts/ITCEDSCR.TTF", 25)
			text = font.render("Game Over, click to restart", True,BLACK)
			center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
			center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
			screen.fill(WHITE)
			screen.blit(text, [center_x, center_y])
		else:
			self.all_sprites_list.draw(screen)

        

def main():
	pygame.init()

	size = [SCREEN_WIDTH,SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)

	pygame.display.set_caption("Space Invader")
	pygame.mouse.set_visible(False)

	done = False
	clock = pygame.time.Clock()

	game = Game()

	while not done:

		done = game.process_events()

		game.run_logic()
		game.display_frame(screen)
		pygame.display.flip()
		clock.tick(60)
		pygame.display.Info()


	pygame.quit()

main()



		

