#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: eman-saeed
"""

import numpy as np
import matplotlib.pyplot as plt

#python image library.
"""
PIL is a library that used for transformation of image 
    into an array  that numpy can understand.
"""
from PIL import Image
"""
-> support the path of the image.
"""
pic = Image.open('English Lab Puppy (1)_0.png')
pic.show()
type(pic)
pic_arr = np.asarray(pic)
print(pic_arr.shape)
#showing image by using matplotlib library by converting the pixels to an image.
#plt.imshow(pic_arr)
pic_red = pic_arr.copy()
#plt.imshow(pic_red)

"""to show the image with the red color we select a specific channel to show."""
#R G B 
pic_red2 = pic_red[:,:,0]
"""
- cmap -> color map we choose color gray .
- RED Channel Values 0-255:
    0 -> No Color Value(pure black).
    255-> Full Color.
"""
plt.imshow(pic_red[:,:,1],cmap ='gray')

#Check for the blue
plt.imshow(pic_red[:,:,2 ],cmap ='gray')
#Check for the green channel
pic_red [:,:,1] = 0
pic_red [:,:,2]  = 0
plt.imshow(pic_red)
print(pic_red.shape)

pic_red[:,:,1].shape




