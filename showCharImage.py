import sys, os
import image2txt
import re
import subprocess
import time

IMAGE_SHOW_DIR = "/root/ViewSky/"
if not os.path.exists(IMAGE_SHOW_DIR):
    os.makedirs(IMAGE_SHOW_DIR)

def getTxtTest(imageFile):
	txtFile = "test.txt"
	image2txt.image2txt(imageFile, txtFile)
	os.system("clear")
	os.system(f'cat {txtFile}')

def get_sorted_image_name_list(ImageNameList):
    image_list = []
    for ImageName in ImageNameList:
        ImageNumber = int(re.match("\d+", ImageName).group())
        image_list.append(ImageNumber)
    image_list.sort()
    ImageNameList = [f"{i}.png" for i in image_list]
    return ImageNameList

def showCharImage(ImageDir):
    ImageNameList = os.listdir(ImageDir)
    image_list = [os.path.join(ImageDir, i) for i in ImageNameList if re.search("\.jpg|png", i)]
    for imageFile in image_list:
        getTxtTest(imageFile)
        command = input("")
        if command.strip() == "q":
            break

def showInnerCharImage():
    file = open("image.txt", "r")
    image_list = file.readlines()
    image_list = [i.strip() for i in image_list]
    file.close()
    for imageFile in image_list:
        getTxtTest(imageFile)
        # subprocess.run(f"eog {imageFile}",shell=True)
        command = input("")
        if command.strip() == "q":
            break

def showInnerImage():
    file = open("image.txt", "r")
    image_list = file.readlines()
    image_list = [i.strip() for i in image_list]
    file.close()
    for imageFile in image_list:
        subprocess.run(f"eog {imageFile}",shell=True)
        command = input("")
        if command.strip() == "q":
            break

def showInnerImage2():
    # contents = os.listdir(IMAGE_SHOW_DIR)
    # if contents:
    #     first_image = IMAGE_SHOW_DIR + contents[0]
    #     subprocess.run(f"eog {first_image}", shell=True)
    #     return
    # subprocess.run(f"rm -rf {IMAGE_SHOW_DIR}*.jpg", shell=True)
    file = open("image.txt", "r")
    image_list = file.readlines()
    image_list = [i.strip() for i in image_list]
    file.close()
    for imageFile in image_list:
        subprocess.run(f"cp {imageFile} {IMAGE_SHOW_DIR}", shell=True)
    imageFile = IMAGE_SHOW_DIR + os.path.basename(imageFile)
    subprocess.run(f"eog {imageFile}",shell=True)

def showCharImage2():
    ImageDir = "images/"
    ImageNameList = os.listdir(ImageDir)
    ImageNameList = get_sorted_image_name_list(ImageNameList)
    image_list = [os.path.join(ImageDir, i) for i in ImageNameList if re.search("\.jpg|png", i)]
    for imageFile in image_list:
        getTxtTest(imageFile)
        command = input("")
        if command.strip() == "q":
            break

if __name__ == '__main__':
    showInnerImage2()