# Font by Min from: https://opengameart.org/content/8x8-font

# Imports
import pygame
from math import floor

pygame.init()


# Screen
width = 320
height = 256

screen = pygame.display.set_mode((width, height), pygame.SCALED)
clock = pygame.time.Clock()

# --Text variables--

# Order stores the order of the text spritesheet from left to right top to bottom.
order = ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "+", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "=", "{", "}", "[", "]", "|", "/", ":", ";", '"', "'", "<", ",", ">", ".", "?", "/", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Misc
spacing = 6
charsize = 8
widthlmt = 16
index = 0
running = True

# Font
font = pygame.image.load("font.png").convert()
font.set_colorkey((0, 0, 0))


# Loads subsurface from spritesheet

def load_spritesheet(image, crop):
	new_image = image.subsurface(crop[0] * crop[2], crop[1] * crop[3], crop[2], crop[3])

	return new_image

# Render text
def rendertext(text, pos):
	# char start posistion [0, 0]
	charpos = [0, 0]

	# Gets the width of the amount of character
	sheetwidth = (font.get_width() / charsize)
		
	# Rendering
	for char in text:
		# Checks if the character is in the order
		if char in order:
			# Gets the letter from the character
			surf = load_spritesheet(font, (order.index(char) % sheetwidth, floor(order.index(char) / sheetwidth), charsize, charsize))
			# Renders and Moves the character position 
			
			
			screen.blit(surf, (charpos[0] + pos[0], charpos[1] + pos[1]))
			charpos[0] += spacing

		# Move when char is space
		if char == " ":
			charpos[0] += spacing

		# Finishes when text is rendered
		if charpos[0] / spacing > widthlmt and char == " ":
			charpos[0] = 0
			charpos[1] += charsize + 2

# text type vars
delaytimer = 0
delayedtext = ""
done = False
index = 0

# text type

def rendertexttype(text, pos, delay):
	# gets the vars
	global delaytimer, delayedtext, done, index
	# func
	delaytimer += 1
	if not done:
		if delay < delaytimer:
			if index < len(text):
				# Adds a character from the text every time the delay time is greater than the delay
				delaytimer = 0
				delayedtext = delayedtext + text[index]
				index += 1
			else:
				done = True

	# Renders the text
	rendertext(delayedtext, pos)




# Mainloop
while running:
	# events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False	


	screen.fill((0, 0, 20))
	
	# render
	rendertexttype('"The quick, brown fox jumped over the lazy dog"', [90, 128], 5)


	clock.tick(60)
	pygame.display.update()