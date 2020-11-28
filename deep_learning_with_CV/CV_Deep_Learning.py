#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: eman-saeed
"""

from keras.datasets import mnist
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.utils.np_utils import to_categorical
#from sklearn.model import classification_report
from keras.models import Sequential
from keras.layers import Dense,Conv2D,MaxPool2D,Flatten
gpus = tf.config.experimental.list_physical_devices('GPU')


(x_train,y_train),(x_test,y_test) = mnist.load_data()
x_train.shape
single_image = x_train[0]
plt.imshow(single_image,cmap='gray_r')
y_train
y_train.shape

y_cat_test = to_categorical(y_test,10)
y_cat_train = to_categorical(y_train,10)
y_cat_train[0]
single_image
single_image.max()
x_train = x_train / x_train.max() #/255
x_test = x_test /x_test.max()
scaled_image = x_train[0]
scaled_image.max()
plt.imshow(scaled_image,cmap='gray_r')
x_train = x_train.reshape(60000,28,28,1)
x_test = x_test.reshape(10000,28,28,1)

model = Sequential()
#CONVOLUTIONAL LAYER 
model.add(Conv2D(filters=32,kernel_size=(4,4),input_shape=(28,28,1),activation='relu'))
#POOLING LAYER 
model.add(MaxPool2D(pool_size=(2,2)))
#2d-->1d
model.add(Flatten())
#DENSE LAYER
model.add(Dense(128,activation='relu'))
model.add(Dense(10,activation='softmax'))
model.compile(loss='categorical_crossentropy',
              optimizer = 'rmsprop',
              metrics = ['accuracy']
             )
summary = model.summary()

model.fit(x_train,y_cat_train,epochs=2)
model.metrics_name
model.evaluate(x_test,y_cat_test)
predications = model.predicate_classes(x_test)
