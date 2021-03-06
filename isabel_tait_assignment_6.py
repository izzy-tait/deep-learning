# -*- coding: utf-8 -*-
"""Isabel_Tait_Assignment_6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10erY7z496VmHFT3CFOxHVqOJSP1MYNAi

Isabel Tait 
Z23426504
Assignment 6
https://colab.research.google.com/drive/10erY7z496VmHFT3CFOxHVqOJSP1MYNAi
"""

import tensorflow.keras
from tensorflow.keras.datasets import cifar10

import numpy as np 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, BatchNormalization
from tensorflow.keras import optimizers
import matplotlib.pyplot as plt
from tensorflow.keras.callbacks import ModelCheckpoint

# The data, split between train and test sets:
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

#splitting validation set 

x_valid=x_train[:int(0.2*x_train.shape[0])]
y_valid=y_train[:int(0.2*x_train.shape[0])]

x_train_new=x_train[int(0.2*x_train.shape[0]):] #reforming training set to not include validation set 
y_train_new=y_train[int(0.2*x_train.shape[0]):]

print(len(x_valid))
print(len(x_train_new))

#normalize the image 
x_train = x_train_new/255
x_test = x_test/255
x_valid=x_valid/255

#Convert the label vectors for all the sets to binary class matrices
y_train = tensorflow.keras.utils.to_categorical(y_train_new, num_classes=10)
y_test = tensorflow.keras.utils.to_categorical(y_test, num_classes=10)
y_valid =tensorflow.keras.utils.to_categorical(y_valid, num_classes=10)

print(x_train.shape)

model = Sequential()
model.add(Conv2D(32,(3,3), padding='same', input_shape=x_train.shape[1:]))
model.add(Activation('relu'))
model.add(Conv2D(32, kernel_size=1))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64, (3,3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, kernel_size=1))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))


model.summary()

#compile and train 

adam = optimizers.Adam(lr=0.001)
model.compile(loss='categorical_crossentropy',
              optimizer=adam,
              metrics=['accuracy'])

filepath="/content/drive/My Drive/model_save.h6"

checkpoint = ModelCheckpoint(filepath, verbose=1, monitor='val_loss',save_best_only=True, period=1) 


#train for 50 epochs with a batch size of 16
history=model.fit(x_train, y_train, batch_size=16, epochs=50, validation_data=(x_valid, y_valid), callbacks=[checkpoint])

#Plot training and validation loss 
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

#Find traning/validation loss and accuracy 
results = model.evaluate(x_train, y_train, batch_size=64)
print('Training Loss, Training Accuracy:', results)

results= model.evaluate(x_valid, y_valid, batch_size=64)
print('Validation Loss, Validation Accuracy', results)

from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator( rotation_range=10,
                 width_shift_range=0.1, height_shift_range=0.1,
                 horizontal_flip=True)

model2 = Sequential()
model2.add(Conv2D(32,(3,3), padding='same', input_shape=x_train.shape[1:]))
model2.add(Activation('relu'))
model2.add(Conv2D(32, kernel_size=1))
model2.add(Activation('relu'))
model2.add(MaxPooling2D(pool_size=(2,2)))

model2.add(Conv2D(64, (3,3), padding='same'))
model2.add(Activation('relu'))
model2.add(Conv2D(64, kernel_size=1))
model2.add(Activation('relu'))
model2.add(MaxPooling2D(pool_size=(2,2)))

model2.add(Flatten())
model2.add(Dense(512, activation='relu'))
model2.add(Dropout(0.5))
model2.add(Dense(10, activation='softmax'))

#compile and train 

adam = optimizers.Adam(lr=0.001)
model2.compile(loss='categorical_crossentropy',
              optimizer=adam,
              metrics=['accuracy'])

filepath="/content/drive/My Drive/model2_save.h6"

checkpoint2 = ModelCheckpoint(filepath, verbose=1, monitor='val_loss',save_best_only=True, mode='auto') 


#train for 50 epochs with a batch size of 16
history2=model2.fit(datagen.flow(x_train, y_train, batch_size=16) , steps_per_epoch=x_train.shape[0]/16, epochs=15, validation_data=(x_valid, y_valid), callbacks=[checkpoint2])

#Plot training and validation loss 
plt.plot(history2.history['loss'])
plt.plot(history2.history['val_loss'])
plt.title('model 2 loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

#Find traning/validation loss and accuracy 
results = model2.evaluate(x_train, y_train, batch_size=64)
print('Training Loss, Training Accuracy:', results)

results= model2.evaluate(x_valid, y_valid, batch_size=64)
print('Validation Loss, Validation Accuracy', results)

"""g) In the first model, the graph displays a low training error and high validation error. This means that the model is overfitting the training data. It starts to become overfitted around the fifth epoch. 
In the second model, the model neither underfits or overfits the data. Both the training and validation losses stay low and constant throughout the epochs.

Problem 2
"""

model3 = Sequential()
model3.add(Conv2D(32,(3,3), padding='same', input_shape=x_train.shape[1:]))
model3.add(BatchNormalization())
model3.add(Activation('relu'))
model3.add(Conv2D(32, kernel_size=1))
model3.add(BatchNormalization())
model3.add(Activation('relu'))
model3.add(MaxPooling2D(pool_size=(2,2)))

model3.add(Conv2D(64, (3,3), padding='same'))
model3.add(BatchNormalization())
model3.add(Activation('relu'))
model3.add(Conv2D(64, kernel_size=1))
model3.add(BatchNormalization())
model3.add(Activation('relu'))
model3.add(MaxPooling2D(pool_size=(2,2)))

model3.add(Flatten())
model3.add(Dense(512, activation='relu'))
model3.add(Dropout(0.5))
model3.add(Dense(10, activation='softmax'))


adam = optimizers.Adam(lr=0.01)
model3.compile(loss='categorical_crossentropy',
              optimizer=adam,
              metrics=['accuracy'])

filepath="/content/drive/My Drive/model3_save.h6"

checkpoint3 = ModelCheckpoint(filepath, verbose=1, monitor='val_loss',save_best_only=True, period=1) 


#train for 50 epochs with a batch size of 16
history3=model.fit(x_train, y_train, batch_size=64, epochs=50, validation_data=(x_valid, y_valid), callbacks=[checkpoint3])

#Plot training and validation loss 
plt.plot(history3.history['loss'])
plt.plot(history3.history['val_loss'])
plt.title('model 3 loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

#Find traning/validation loss and accuracy 
results = model3.evaluate(x_train, y_train, batch_size=64)
print('Training Loss, Training Accuracy:', results)

results= model3.evaluate(x_valid, y_valid, batch_size=64)
print('Validation Loss, Validation Accuracy', results)

"""b) The training loss in problem 1e is how a training loss should usually look, it should be an L-shape, because the loss is exponentially decreasing. The training loss in this model is constant, it does not change and is a straight line."""