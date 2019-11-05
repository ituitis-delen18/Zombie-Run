"""
	Emirhan Delen
	Platform Game Character Movements: Fire / Jump / Run etc.
	Made with python/pygame
	Made for only improving myself on python
"""

import pygame,sys,time

pygame.init()

pygame.time.delay(3000)
	
pygame.display.set_caption("Zombie Run")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

pygame.mixer.music.load("mario.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)

screenx = 739
screeny = 415
#player 40x50
player1_x = 500
player1_y = 255
#zombie 50x60
zombie_x = 0
zombie_y = 245
#50x42

screen = pygame.display.set_mode((screenx,screeny))

bg = pygame.image.load("arkaplan.jpeg")

sprite_counter = 0
i=0

run_to_left = False
run_to_right = False
duruyoaq = True
fireOn = False
sagadonuk = True

sagakosuyoaq = [pygame.image.load("Run_Character/Run_0.png"),pygame.image.load("Run_Character/Run_1.png"),pygame.image.load("Run_Character/Run_2.png"),pygame.image.load("Run_Character/Run_3.png"),pygame.image.load("Run_Character/Run_4.png"),pygame.image.load("Run_Character/Run_5.png"),pygame.image.load("Run_Character/Run_6.png"),pygame.image.load("Run_Character/Run_7.png"),pygame.image.load("Run_Character/Run_8.png"),pygame.image.load("Run_Character/Run_9.png")]

solakosuyoaq = [pygame.image.load("Run_Character_2/Run_0.png"),pygame.image.load("Run_Character_2/Run_1.png"),pygame.image.load("Run_Character_2/Run_2.png"),pygame.image.load("Run_Character_2/Run_3.png"),pygame.image.load("Run_Character_2/Run_4.png"),pygame.image.load("Run_Character_2/Run_5.png"),pygame.image.load("Run_Character_2/Run_6.png"),pygame.image.load("Run_Character_2/Run_7.png"),pygame.image.load("Run_Character_2/Run_8.png"),pygame.image.load("Run_Character_2/Run_9.png")]

soldan_saga_gelio = [pygame.image.load("zombie_walk/Walk (1).png"),pygame.image.load("zombie_walk/Walk (2).png"),pygame.image.load("zombie_walk/Walk (3).png"),pygame.image.load("zombie_walk/Walk (4).png"),pygame.image.load("zombie_walk/Walk (5).png"),pygame.image.load("zombie_walk/Walk (6).png"),pygame.image.load("zombie_walk/Walk (7).png"),pygame.image.load("zombie_walk/Walk (8).png"),pygame.image.load("zombie_walk/Walk (9).png"),pygame.image.load("zombie_walk/Walk (10).png")]

zombie_olduaq = [pygame.image.load("zombie_death/Dead (1).png"),pygame.image.load("zombie_death/Dead (2).png"),pygame.image.load("zombie_death/Dead (3).png"),pygame.image.load("zombie_death/Dead (4).png"),pygame.image.load("zombie_death/Dead (5).png"),pygame.image.load("zombie_death/Dead (6).png"),pygame.image.load("zombie_death/Dead (7).png"),pygame.image.load("zombie_death/Dead (8).png"),pygame.image.load("zombie_death/Dead (9).png"),pygame.image.load("zombie_death/Dead (10).png"),pygame.image.load("zombie_death/Dead (11).png"),pygame.image.load("zombie_death/Dead (12).png")]

zombie_sprite = 0
zombie_oldu = False

duruyoaq_fotosu = 0

mermiler = []

class Mermi(object):
	def __init__(self , x , y , radius , colour , facing):
		self.x = x
		self.y = y
		self.radius = radius
		self.colour = colour
		self.facing = facing
		self.vel = 8*facing
		
	def draw(self,screen):
		pygame.draw.circle(screen , self.colour, (int(self.x) , int(self.y)),self.radius)

def redraw_the_screen():
	global sprite_counter
	global duruyoaq_fotosu
	global sagadonuk
	global zombie_sprite
	global zombie_x
	global i
	screen.blit(bg , (0,0))
	if sprite_counter > 9 :
		sprite_counter = 0
		
	if duruyoaq_fotosu < 10:
		sagadonuk = 1
	else:
		sagadonuk = -1
		 
	if duruyoaq:
		if duruyoaq_fotosu < 10:
			screen.blit(sagakosuyoaq[duruyoaq_fotosu], (player1_x,player1_y))
		else:
			screen.blit(solakosuyoaq[duruyoaq_fotosu - 10], (player1_x,player1_y))
		
	if run_to_right :
		screen.blit(sagakosuyoaq[sprite_counter], (player1_x,player1_y))
		duruyoaq_fotosu = sprite_counter
		sprite_counter += 1
		
	if run_to_left :
		screen.blit(solakosuyoaq[sprite_counter], (player1_x,player1_y))
		duruyoaq_fotosu = sprite_counter + 10
		sprite_counter += 1
	for mermi in mermiler:
		mermi.draw(screen)
	if not zombie_oldu:
		screen.blit(soldan_saga_gelio[zombie_sprite], (zombie_x,zombie_y))
		zombie_sprite += 1
		if zombie_sprite > 9:
			zombie_sprite = 0
		zombie_x += 3
	elif zombie_oldu and i < 12:
		screen.blit(zombie_olduaq[i] , (zombie_x , 305-42))
		i+=1
		
	pygame.display.update()
	

isJump = False
jumpPic = 8



fps = pygame.time.Clock()
while True:
	fps.tick(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				isJump = True
			if event.key == pygame.K_f:
				if len(mermiler)<10 :
					mermiler.append(Mermi(player1_x+10 , player1_y+30 , 5 , (0,0,0), sagadonuk))
	for mermi in mermiler :
		mermi.x += mermi.vel
		if mermi.x <0 or mermi.x > 739 :
			mermiler.pop(mermiler.index(mermi))
		if (abs(mermi.x - zombie_x)< 20) and (not zombie_oldu) and (zombie_y - mermi.y) < 5:
			print(mermi.y , zombie_y)
			zombie_oldu = True
			print("YIKES")
			mermiler.pop(mermiler.index(mermi))
			
			#if event.key == pygame.K_k:
			#	fireOn = True
			#	x = player1_x + 10
			#	y = player1_y + 30
	"""if fireOn:
		if sagadonuk:
			x +=10
		else :
			x -=10
		if x <0 or x > 800:
			fireOn = False"""
	if isJump:
		if jumpPic >= 0:
			player1_y -= (jumpPic**2)/2
			jumpPic -= 1
		elif jumpPic > -9:
			player1_y += (jumpPic**2)/2
			jumpPic -= 1
		else :
			isJump = False 
			jumpPic = 8
	
	keys = pygame.key.get_pressed()
	

	if keys[pygame.K_RIGHT]:
		run_to_right = True
		duruyoaq = False
		run_to_left = False
		player1_x += 5
	elif keys[pygame.K_LEFT]:
		run_to_right = False
		run_to_left = True
		duruyoaq = False
		player1_x -= 5
	else:
		run_to_left = False
		run_to_right = False
		duruyoaq = True
		sprite_counter = 0
			
	redraw_the_screen()
