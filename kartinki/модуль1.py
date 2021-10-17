import random
from PIL import Image, ImageDraw  

mode = int(input('mode:'))  
image = Image.open("temp.jpg")  
draw = ImageDraw.Draw(image)  
width = image.size[0]  
height = image.size[1]  	
pix = image.load() 
if (mode == 0):
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = (a + b + c) // 3
			draw.point((i, j), (S, S, S))
