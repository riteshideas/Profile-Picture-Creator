import numpy as np
import cv2
import os
import readline



os.system("clear")
def createImage(colourChance = 50):
    """
    #### This function creates images randomly
    ## Parameters\n
    `colourChance` :  How much colour you want to have in your picture. 
    Like in 100 square pixles there would be `colourChance` amount of coloured pixles::
        >>> createImage(colourChance = 10)
        
    """
    # The Random colour
    color = [
            np.random.randint(0, 255),
            np.random.randint(0, 255),
            np.random.randint(0, 255)
            ]

    LeftPixls = []


    # The Left Side
    for _ in range(5):
        colour = []
        for _ in range(2):
            if np.random.randint(0, int(100/colourChance)) == 0:
                colour.append(color)
            else:
                colour.append([255, 255, 255])
        LeftPixls.append(colour)

    LeftPixls = np.array(LeftPixls, dtype="uint8")


    # The Middle Part
    MiddlePixls = []
    for _ in range(5):
        colour = []
        if np.random.randint(0, int(100/colourChance)) == 0:
            colour.append(color)
        else:
            colour.append([255, 255, 255])
        MiddlePixls.append(colour)

    MiddlePixls = np.array(MiddlePixls, dtype="uint8")


    # The Right Part (Just have to flip and add)
    RightPixls = np.fliplr(LeftPixls)
    Pixls = np.concatenate((LeftPixls, MiddlePixls, RightPixls), axis=1)

    return Pixls

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized


number = int(input("How many photos : "))


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
    img = createImage(colourChance=50)
    img = image_resize(img, 500, 500)
    cv2.imwrite(f"../photos/MyPhoto({x-1}).png", img)
