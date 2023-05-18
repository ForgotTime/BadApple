from PIL import Image
import numpy
WIDTH = 200
HEIGHT = 50
def image2txt(inputFile, outputFile):
	im = Image.open(inputFile).convert('L')
	charWidth = WIDTH
	charHeight = HEIGHT
	im = im.resize((charWidth, charHeight))
	target_width, target_height = im.size
	data = numpy.array(im)[:target_height, :target_width]
	f = open(outputFile, 'w')
	for row in data:
		f.write(5*' ')
		for pixel in row:
			if pixel > 127:
				f.write('#')
			else:
				f.write(' ')
		f.write('\n')
	f.close()