#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 22:30:48 2020

@author: eman-saeed
"""


import cv2
import numpy as np

#VARIABLELS
#TRUE while mouse button down , False while mouse button UP .
drawing = False
ix = -1
iy = -1
#FUNCTTION
def draw_rectangle(event,x,y,flags,params):
        
    global ix , iy , drawing 

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
  
            
#SHOWING THE IMAGE 

img = np.zeros((512,512,3))
cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_rectangle)
     
while True:
    cv2.imshow('my_drawing',img)
    
        #CHECK FOR ESC.
    if cv2.waitKey(1) & 0xFF == 27: 
        break
cv2.destroyAllWindows()
