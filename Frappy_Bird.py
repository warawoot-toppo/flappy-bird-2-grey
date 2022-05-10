import pygame
import sys
import random
pygame.init()


def game_floor():
	screen.blit(floor_base, (floor_x_pos,700))
	screen.blit(floor_base, (floor_x_pos + 576,700))


def check_collision(pipes):
	for pipe in pipes:
		if bird_rect.colliderect(pipe):
			random_sound = random.choice(mix_die_sound)
			random_sound.play()
			return False
	if bird_rect.top <= -100 or bird_rect.bottom > 700:
		random_sound = random.choice(mix_die_sound)
		random_sound.play()
		return False
	return True 	

def create_pipe():
	random_pipe_pos = random.choice(pipe_height)
	top_pipe = pipe_surface.get_rect(midbottom = (600, random_pipe_pos - 300))
	bottom_pipe = pipe_surface.get_rect(midtop = (600, random_pipe_pos))
	return bottom_pipe, top_pipe

def move_pipes(pipes):
	for pipe in pipes:
		pipe.centerx -= 5
		
		
	return pipes	 


def draw_pipes(pipes):
	for pipe in pipes:
		if pipe.bottom >= 800:
			screen.blit(pipe_surface, pipe) 
		else:
			flip_pipe = pygame.transform.flip(pipe_surface, False, True)
			screen.blit(flip_pipe, pipe)	


############# Window ##############
screen = pygame.display.set_mode((576,800))
background = pygame.image.load('img/background.png')
background = pygame.transform.scale2x(background)
icon = pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Toppo Flappy Bird')
clock = pygame.time.Clock()


################ Player ##############
bird = pygame.image.load('img/bird.png')
bird = pygame.transform.scale(bird, (40, 30))
bird_rect = bird.get_rect(center = (100,400))
grcvity = 0.7
bird_movement = 0


############# Floor #################
floor_base = pygame.image.load('img/base.png')
floor_base = pygame.transform.scale2x(floor_base)
floor_x_pos = 0
game_active = True


############# Message #############
message = pygame.image.load('img/icon.png')
message = pygame.transform.scale2x(message)
game_over_rect = message.get_rect(center = (288, 400))


############## pipe ###############
pipe_surface = pygame.image.load('img/base1.png')
pipe_surface = pygame.transform.scale(pipe_surface, (70, 336))
pipe_list = []
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)  
pipe_height = 400, 600, 800


################ Sound Effect #################
flap_sound = pygame.mixer.Sound('sf/a.mp3')
die_sound0 = pygame.mixer.Sound('sf/aaaa.mp3')
die_sound1 = pygame.mixer.Sound('sf/crazy.mp3')
die_sound2 = pygame.mixer.Sound('sf/ear-rap.mp3')
die_sound3 = pygame.mixer.Sound('sf/fart-with.mp3')
die_sound4 = pygame.mixer.Sound('sf/9o7st.mp3')
die_sound5 = pygame.mixer.Sound('sf/pornhub.mp3')
die_sound6 = pygame.mixer.Sound('sf/pen-kuy-rai.mp3')
die_sound8 = pygame.mixer.Sound('sf/sf1.mp3')
die_sound11 = pygame.mixer.Sound('sf/sf4.mp3')
die_sound12 = pygame.mixer.Sound('sf/sf5.mp3')
die_sound13 = pygame.mixer.Sound('sf/sf6.mp3')
die_sound15 = pygame.mixer.Sound('sf/sf8.mp3')
die_sound16 = pygame.mixer.Sound('sf/sf9.mp3')
die_sound18 = pygame.mixer.Sound('sf/sf11.mp3')
die_sound19 = pygame.mixer.Sound('sf/sf12.mp3')
die_sound20 = pygame.mixer.Sound('sf/sf13.mp3')
mix_die_sound = []
mix_die_sound.append(die_sound0)
mix_die_sound.append(die_sound1)
mix_die_sound.append(die_sound2)
mix_die_sound.append(die_sound4)
mix_die_sound.append(die_sound5)
mix_die_sound.append(die_sound6)
mix_die_sound.append(die_sound8)
mix_die_sound.append(die_sound11)
mix_die_sound.append(die_sound12)
mix_die_sound.append(die_sound13)
mix_die_sound.append(die_sound15)
mix_die_sound.append(die_sound16)
mix_die_sound.append(die_sound18)
mix_die_sound.append(die_sound19)
mix_die_sound.append(die_sound20)



################ Main Event ###############
while True:
	

	#### FPS #####
	clock.tick(120)
	

	############# Event For Exit ############
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit() 
		

		########## Event For Keyboard ###############	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and game_active:
				bird_movement = 0
				bird_movement -= 12
				flap_sound.play()
			if event.key == pygame.K_SPACE and game_active == False:
				bird_rect.center = (100, 300)
				bird_movement = 0
				pipe_list.clear()
				game_active = True	
		

		if event.type == spawnpipe and game_active:
			pipe_list.extend(create_pipe())			
	



	############ Background ##########
	screen.blit(background,(0,0))
	

	############ Bird Event ##############
	if game_active:
		bird_movement += grcvity	
		bird_rect.centery += bird_movement
		screen.blit(bird, bird_rect)		
		pipe_list = move_pipes(pipe_list)
		draw_pipes(pipe_list)
		game_active = check_collision(pipe_list)
	else:
		screen.blit(message, game_over_rect)	


	############ floor Loop ############	
	floor_x_pos -= 5 
	game_floor()
	if floor_x_pos < - 576:
		floor_x_pos = 0


	pygame.display.update()
