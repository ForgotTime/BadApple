import sys, os
import image2txt
import time

def getTxtTest(imageFile):
	txtFile = "test.txt"
	image2txt.image2txt(imageFile, txtFile)
	os.system("clear")
	os.system(f'cat {txtFile}')

def getTxt(imagePath, txtPath):
	img_count = 1
	txtFile = txtPath + str(img_count) + '.txt'
	if os.path.exists(txtFile):
		return
	while img_count <= len(os.listdir(imagePath)):
		imageFile = imagePath + str(img_count) + '.png'
		txtFile = txtPath + str(img_count) + '.txt'
		image2txt.image2txt(imageFile, txtFile)
		print ('txt ' + str(img_count) + ' collected.')
		img_count += 1

def play(txtPath):
	txt_count = 1
	while txt_count <= len(os.listdir(txtPath)):
		os.system('clear')
		os.system('cat ' + txtPath + str(txt_count) + '.txt')
		time.sleep(1.0/11.25)
		txt_count += 1

def animate():
	txt_dir_path = 'txt/'
	img_dir_path = 'images/'
	getTxt(img_dir_path, txt_dir_path)
	play(txt_dir_path)

if __name__ == '__main__':
	animate()
