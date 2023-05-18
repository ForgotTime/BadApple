import sys, os
import image2txt
import time
import re
import play
import showCharImage

print('''
1.Bad Apple自动演示
2.Bad Apple手动演示
3.自定义图片目录演示
4.查看系统本地字符画
5.查看系统本地图片
''')
number = input("").strip()
if number == "1":
    play.animate()
elif number == "2":
    showCharImage.showCharImage2()
elif number == "3":
    ImageDir = input("请输入图片目录：\n").strip()
    showCharImage.showCharImage(ImageDir)
elif number == "4":
    showCharImage.showInnerCharImage()
elif number == "5":
    showCharImage.showInnerImage2()
else:
    print("bye~~~")
    sys.exit()