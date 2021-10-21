import pygame
from scipy.ndimage import convolve

import numpy as np

kernel = np.array(
	[[2,2,2],
	[2,1,2],
	[2,2,2]]
)

map_vals = {
	1  :0,
	3  :0,
	5  :1,
	7  :1,
	9  :0,
	11 :0,
	13 :0,
	15 :0,
	17 :0,
	0  :0,
	2  :0,
	4  :0,
	6  :1,
	8  :0,
	10 :0,
	12 :0,
	14 :0,
	16 :0
}

S = 500
white_mat = np.ones((S,S,3))*255.0

def make_mat(mat):
	conv = convolve(mat, kernel)

	h,w = conv.shape

	for i in range(h):
		for j in range(w):
			conv[i,j] = map_vals[conv[i,j]]
	return conv

def mat_to_img(mat):
	img = np.zeros_like(white_mat)


	img[:,:,0] = mat * 255 
	img[:,:,1] = mat * 255 
	img[:,:,2] = mat * 255 

	return pygame.surfarray.make_surface(img)

if __name__ == '__main__':

	pygame.init()
	clock = pygame.time.Clock()

	infoObject = pygame.display.Info()
	current_w, current_h = infoObject.current_w, infoObject.current_h

	
	screen = pygame.display.set_mode((S,S))

	board = np.random.randint(0,2,(S,S))	
	running = True
	
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		board = make_mat(board)
		
		surf =  mat_to_img(board)

		screen.blit(surf, (0, 0))

		#clock.tick(5)
		pygame.display.update()