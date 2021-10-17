import random
from PIL import Image, ImageDraw  

A=100
while A < 601:
	file = str(A)+'.jpg'
	image = Image.open(file)
	draw = ImageDraw.Draw(image)
	width = image.size[0]  
	height = image.size[1]  	
	pix = image.load() 
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = (a + b + c) // 3
			draw.point((i, j), (S, S, S))
	image.save(str(A) + "chb.jpg")
	A = A + 1
del draw