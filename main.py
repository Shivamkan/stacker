import pygame

pygame.init()

screenY = int(650)
screenX = int((screenY / 16) * 9)
colors = 10
auto = 2
sound = pygame.mixer.Sound("perfect.mp3")
#Do Not Change Anything after this ponit
screen = pygame.display.set_mode((screenX, screenY))
down = 0

def hls(h, s, l):
	h = h / 255
	s = s / 255
	l = l / 255

	if s == 0:
		r, g, b = 1, 1, 1
	else:
		def hue2rgb(p, q, t):
			if t < 0:
				t += 1
			if t > 1:
				t -= 1
			if t < 1 / 6:
				return p + (q - p) * 6 * t
			if t < 0.5:
				return q
			if t < 2 / 3:
				return p + (q - p) * (2 / 3 - t) * 6
			return p

		if l < 0.5:
			q = l * (1 + s)
		else:
			q = l + s - l * s

		p = 2 * l - q
		r = hue2rgb(p, q, h + 1 / 3)
		g = hue2rgb(p, q, h)
		b = hue2rgb(p, q, h - 1 / 3)

	return (round(r * 255), round(g * 255), round(b * 255))


class main:
	def __init__(self):
		self.blockhight = int(screenY / 30)
		self.hue = 0
		self.y = screenY - self.blockhight
		self.x = (screenX / 12) * 1
		self.width = (screenX / 12) * 10
		self.place = 1
		self.lastsuf = 0
		self.last = self.x
		self.dir = 1

	def draw(self, screen):
		if self.lastsuf and not down:
			screen.blit(self.lastsuf,(0,0))
		elif down:
			screen.blit(self.lastsuf,(0,self.blockhight))
		pygame.draw.rect(screen, hls(self.hue, 255, 255 / 2), (self.x, self.y, self.width, self.blockhight))
		if self.place == 1:
			self.lastsuf = screen.copy()
			self.reset()

	def move(self):
		if self.dir == 1:
			self.x += 1
		else:
			self.x -= 1
		if self.x + self.width >= screenX:
			self.dir = 0
		elif self.x <= 0:
			self.dir = 1

	def handle_input(self):
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.placeb()
			if event.type == pygame.MOUSEBUTTONDOWN:# and event.button == 1:
				self.placeb()

	def placeb(self):
		self.place = 1
		if abs(self.x - self.last) < auto:
			self.x = self.last
			sound.play()
		elif self.x > self.last:
			self.width -= self.x - self.last
		else:
			self.width -= self.last - self.x
			self.x = self.last
		self.dir = 1

	def reset(self):
		global down
		if self.y > (screenY/3):
			self.y -= self.blockhight
		else:
			down = 1
		self.place = 0
		self.hue += 255 / colors
		self.last = self.x
		self.x = 0
		if self.hue > 254:
			self.hue = 0

def resetgame(main):
	main.blockhight = int(screenY / 30)
	main.hue = 0
	main.y = screenY - main.blockhight
	main.x = (screenX / 12) * 1
	main.width = (screenX / 12) * 10
	main.place = 1
	main.lastsuf = 0
	main.last = main.x
	main.dir = 1

main = main()
clock = pygame.time.Clock()
while True:
	clock.tick(60)
	screen.fill((100, 100, 100))
	main.draw(screen)
	main.move()
	main.handle_input()
	pygame.display.flip()
	if main.width <= 0:
		resetgame(main)
