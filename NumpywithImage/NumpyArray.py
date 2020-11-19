#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 13:57:08 2020

@author: eman-saeed
"""
#importing the library
import numpy as np

"""There's a couple of ways we can create arrays:
    on of them is creating a normal Python list.
"""
mylist = [1,2,3]
type(mylist)

#we must cast the list

myarray = np.array(mylist)
print(type(myarray))
"""
we can make a 2-D array with multiple ways.
"""
print(np.arange(0,10))
print(np.arange(0,10,2))
print(np.zeros(shape=(5,5)))
type(0)
type(0.0)
type(0.)
print(np.ones(shape=(2,4)))
np.ones((2,4))
np.random.seed(101)
arr = np.random.randint(0,100,10)
arr
arr2 = np.random.randint(0,100,10)
arr2
arr.argmax()
arr.min()
arr.argmax()
arr.argmin()
arr.mean()
print(arr.reshape((2,5)))
arr.reshape((5,2))
mat = np.arange(0,100).reshape(10,10)
print(mat)
row = 0 
col = 1
print(mat[row,col])
print(mat[4,6])
print(mat[:,1])
print(mat[:,2])
(10,)
print(mat[:,1].reshape(1,10))
print(mat[:,1].shape)
print(mat[:,1].reshape(10,1))
print(mat[2,:])
print(mat)
print(mat[0:3,0:3])
print(mat[0:3,0:4])
#reasigned the values 
mat[0:3,0:4]=0
mynewmat = mat.copy()
mynewmat[0:6,:] =99
print(mynewmat)
