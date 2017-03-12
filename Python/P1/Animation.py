#Testing out the drawing tool and Animation
#Simple Animation of a Computer Monitor that changes the output Animation in the screen by keyboard input
import pygame
import random

pygame.init()

# ----------Constants and Variables-------------------# 
BLACK = (0,0,0)
WHITE = (255,255,255)
BACKGROUND = (120,0,21)
BROWN = (179,75,34)
LIGHTW = (212,101,57)
GRAY = (94,94,94)
GREEN = (0,255,0)

Color = [0,255,0]

size = [700,500]
screen = pygame.display.set_mode(size)

current = 0
done = False
clock = pygame.time.Clock()

pygame.display.set_caption("Computer Animation")

#Starting position of the rectangle and circle
rect_x = 325
rect_y = 135

#Speed and direction of the rectangle
rect_change_x = 5
rect_change_y = 5

def random1():
  return random.randrange(0,256)

#For the white particle down
star_list = []

for i in range(50):
	x = random.randrange(257,444)
	y = random.randrange(125,225)
	star_list.append([x,y])

#Text Font 
font = pygame.font.Font("C:/Windows/Fonts/ITCEDSCR.TTF", 50)
font1 = pygame.font.Font("C:/Windows/Fonts/ITCEDSCR.TTF", 80)
#-----------While Loop discreption--------------------#
while done == False:
	#-----------Event Processing----------------------#
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("User asked to quit.")
			done = True
		elif event.type == pygame.KEYDOWN:
			print("User pressed a key.")
			if current == 0:
				current = 1
			elif current == 1:
				current = 2
			elif current == 2:
				current = 0


	#-------------------------------------------------#

	#------------------Game Logic---------------------#
	if current == 0:
		rect_x += rect_change_x
		rect_y += rect_change_y

	#-------------------------------------------------#

	#------------------Drawing Code-------------------#
	screen.fill(BACKGROUND)

	#Drawing the Wood Panel on the Background
	for i in range(8):
		pygame.draw.line(screen,BROWN,[0,62.5*i],[700,62.5*i],2)
		pygame.draw.line(screen,LIGHTW,[0,2+62.5*i],[700,2+62.5*i],2)

	pygame.draw.rect(screen,BLACK,[250,120,200,120],10)
	pygame.draw.rect(screen,BLACK,[340,240,20,30])
	pygame.draw.ellipse(screen,BLACK,[320,265,60,20],10)

	#screen.fill(BLACK)

	if current == 0:
		pygame.draw.rect(screen,GRAY,[255,125,190,110])
		if rect_y > 221 or rect_y < 126:
			Color = [random1(),random1(),random1()]
			rect_change_y = rect_change_y * -1
		elif rect_x > 431 or rect_x < 251:
			rect_change_x = rect_change_x * -1
			Color = [random1(),random1(),random1()]
		else:
			pygame.draw.rect(screen,Color, [rect_x,rect_y,15,15])
	
	elif current == 1:
		pygame.draw.rect(screen,BLACK,[255,125,190,110])
		for item in star_list:
			item[1] += 2
			pygame.draw.circle(screen,WHITE,item,2)
			if item[1] > 230:
				item[1] = 125
				item[0] = random.randrange(255,444)

	elif current == 2:
		Color = [random1(),random1(),random1()]
		pygame.draw.rect(screen,Color,[255,125,190,110])
		for row in range(125,235,4):
			for column in range(255,445,9):
				pygame.draw.rect(screen,GREEN,[column,row,2,2])

	
	text = font.render("Press Any Key to Switch Screen.",True, BLACK) #(Text, anti-aliasing, color)
	text1 = font.render("Press Any Key to Switch Screen.", True, (255,200,0))
	screen.blit(text, [100,320])
	screen.blit(text1, [105,320])

	#text2 = font1.render("Good Night",True, BLACK) #(Text, anti-aliasing, color)
	#text3 = font1.render("Good Night", True, GRAY)
	#screen.blit(text2, [115,350])
	#screen.blit(text3, [120,350])
	
	#-------------------------------------------------#

	#------------Screen Update------------------------#
	pygame.display.flip()

	#-------Clock tick, 40 frames per second----------#
	clock.tick(40)

pygame.quit()