import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))

def main():
	
	sysfont = pygame.font.SysFont(None, 36)
	counter = 0
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
				
		counter += 1
		
		SURFACE.fill((0, 0, 0))
		
		
