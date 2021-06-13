import cv2
import numpy as np
import os
from PIL import Image




def createPicture(color=[np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)], value=2, flipType=1):
    pixles = [

    ]


    for _ in range(10):
        colour = []
        for _ in range(5):
            val = np.random.randint(0, value + 1)
            if val == 0:
                colour.append(color)

            else:
                colour.append([255, 255, 255])
        pixles.append(colour)

    pixles = np.array(pixles, dtype='uint8')
    if flipType == 1:
        left_pixles = np.flip(pixles)
        pic = np.concatenate((pixles, left_pixles), axis=1)
        return pic
    elif flipType == 2:
        left_pixles = np.flipud(pixles)
        pic = np.concatenate((pixles, left_pixles), axis=1)
        return pic
    elif flipType == 3:
        left_pixles = np.fliplr(pixles)
        pic = np.concatenate((pixles, left_pixles), axis=1)
        return pic
    else:
        raise Exception("Did not give value between 1-3 for fliptype parameter")



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