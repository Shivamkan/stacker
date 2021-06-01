import pygame
pygame.init()

screenY = int(700)
screenX = int((screenY/16)*9)

screen = pygame.display.set_mode((screenX,screenY))

def handle_input():
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

while True:
	screen.fill((100,100,100))
	handle_input()
	pygame.display.flip()