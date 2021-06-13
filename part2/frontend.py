import numpy as np
import cv2
import backend as Image
import readline
import os


os.system("clear")
number = int(input("How many pictures : "))
for i in range(number):
    try:
        os.mkdir("../photos")
    except:
        pass
    files = []
    files = os.listdir("../photos")

    if len(files) == 0:
        x = 1
    elif files != []:
        x = len(files) + 1
    else:
        pass

    colour = [np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)]
    img = Image.createPicture(color=colour, value=1, flipType=1)
    img = Image.image_resize(img, 500, 500)
    cv2.imwrite(f"../photos/MyPhoto({x-1}).png", img)