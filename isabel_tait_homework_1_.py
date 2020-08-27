# -*- coding: utf-8 -*-
"""Isabel Tait-Homework 1 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-Qe5bTi4pyfznhZXgsENc_JKuMlK7Fpm

Name: Isabel Tait
Znumber: Z23426504
https://colab.research.google.com/drive/1-Qe5bTi4pyfznhZXgsENc_JKuMlK7Fpm
"""

import math 
import sys 
import numpy as np


#if mathOperator == "/" 
   # divide(number1 )           

#number2 = input("\nSecond number: ") 
 
def add(firstNumber): 
    number2 = float(input("\nSecond number: ")) 
    calculatedSum = firstNumber + number2 
    print("The sum of {0} and {1} is {2}" .format(firstNumber, number2, calculatedSum)) 
    #print(firstNumber + number2)
    return calculatedSum

def subtract(firstNumber):
   number2 = float(input("\nSecond number: ")) 
   difference = firstNumber - number2 
   print("The difference of {0} and {1} is {2}" .format(firstNumber, number2, difference))
   return difference

def multiply(firstNumber):
   number2 = float(input("\nSecond number: ")) 
   product= firstNumber * number2
   print("The product of {0} and {1} is {2}" .format(firstNumber, number2, product))
   return product

def divide(firstNumber):
   number2 = float(input("\nSecond number: ")) 
   quotient=firstNumber/number2
   print("The quotient of {0} and {1} is {2}" .format(firstNumber, number2, quotient))
   return quotient

def remainder(firstNumber):
    number2 = float(input("\nSecond number: "))  
    remainderResult=firstNumber % number2
    print("The remainder of {0} and {1} is {2}" .format(firstNumber, number2, remainderResult))
    return remainderResult

def power(firstNumber):
    number2 = float(input("\nSecond number: "))
    powerResult= firstNumber ** number2
    print("The power of {0} to the {1}th power is {2}" .format(firstNumber, number2, powerResult))
    return powerResult

def naturalLog(firstNumber):
    naturalLogResult=np.log(firstNumber)
    print("The natural log of {0} is {1}" .format(firstNumber, naturalLogResult))
    return naturalLogResult

def absoluteValue(firstNumber):
    absoluteValueResult=abs(firstNumber)
    print("The absolute value of {0} is {1}" .format(firstNumber, absoluteValueResult))
    return absoluteValueResult

def calculations(firstNumber):
  number1 = float(user_input) 

  mathOperator = input("Please input a math operator: ")

  if mathOperator == '+':
    add(number1)

  elif mathOperator == '-':
    subtract(number1)

  elif mathOperator == '*':
    multiply(number1)

  elif mathOperator == '/':
    divide(number1) 

  elif mathOperator == '%':
    remainder(number1)    

  elif mathOperator == '^':
    power(number1)    
   
  elif mathOperator == 'ln':
    naturalLog(number1)   

  elif mathOperator == 'abs':
    absoluteValue(number1)   
    
  elif mathOperator == 'exp':
    print("The Exponential Value of {0} is {1}".format(number1,math.exp(number1)))
    
  return

keepGoing=True

while keepGoing==True:
  print("To perform a calculation, input a number, then operator, then second number if used")

  user_input=input("Please input your first number or enter x to exit out of calculation")
  correct =False
  while not correct:
    try:
      user_input=float(user_input)
      correct=True
    except ValueError:
      if user_input.lower() == 'x':
        sys.exit()  
      user_input=input("This is invalid. Please enter a valid digit.")

  calculations(user_input)
    #user_input=input("Please input your first number or enter x to exit out of calculation")

import matplotlib.pyplot as plt



def newDataPoints(UserDataPointsX, UserDataPointsY):
        print("Enter in more data points. Type in x if you do not wish to enter in any more data points")   
        altX=input("X value: ")
        #altY=input("Y value: ")

        
        #while not (altX=="x" or altX=="X" or altY=="x" or altY=="X"):
        if altX=="x" or altX=="X": 
          return
        else:      
          altY=float(input("Y value: "))
          if type(altY)==float is False:
              print("Invalid input")
          else:
              altXfloat=float(altX)
              altYfloat=float(altY)
              UserDataPointsX.append(altX)
              UserDataPointsY.append(altY)
              plt.xlabel('X')
              plt.ylabel('Y')
              plt.title('Assignment 1 Problem 2')
              plt.axis([0,5,0,5])
              plt.plot(C1Xaxis, C1Yaxis, "ro",label="C1")
              plt.plot(C2Xaxis, C2Yaxis,"x",label="C2")
              plt.plot(UserDataPointsX, UserDataPointsY, "1")
              plt.legend()
              plt.show()
              if altXfloat>thx and altYfloat>thy:
                  print("This data point is in Class 1")
              else:
                  print("This data point is in Class 2")
              newDataPoints(UserDataPointsX, UserDataPointsY)




isRunning= "true"

while isRunning=="true":
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Assignment 1 Problem 2')
        plt.axis([0,5,0,5])
        C1Xaxis=[2,3,2]
        C1Yaxis=[2,2,3]
        C2Xaxis=[1,1,2]
        C2Yaxis=[2,1,1]
        plt.plot(C1Xaxis, C1Yaxis, "ro",label="C1")
        plt.plot(C2Xaxis, C2Yaxis,"x", label="C2")
        plt.legend()
        plt.show()

        print("Please enter in the threshold x and y values.")
        thx=float(input("Please enter in threshold x:"))
        thy=float(input("Please enter in threshold y:"))

        NewC1X=[]
        NewC1Y=[]

        NewC2X=[]
        NewC2Y=[]

        for j in range(3):
          if C1Xaxis[j]>thx and C1Yaxis[j]>thy:
              NewC1X.append(C1Xaxis[j])
              NewC1Y.append(C1Yaxis[j])
          else:
              NewC2X.append(C1Xaxis[j])
              NewC2Y.append(C1Yaxis[j])    

        for k in range(3):
          if C2Xaxis[k]>thx and C2Yaxis[k]>thy:
              NewC1X.append(C2Xaxis[k])
              NewC1Y.append(C2Yaxis[k])
          else:
              NewC2X.append(C2Xaxis[k])
              NewC2Y.append(C2Yaxis[k])   

        NewC1Xlength=len(NewC1X)
        #print("NewC1Xlength: ")
        #print(NewC1Xlength)

        NewC2Xlength=len(NewC2X)
        #print("NewC2Xlength: ")
        #print(NewC2Xlength)

        count=0

        for h in range(3):
            for i in range (NewC1Xlength):
                if C1Xaxis[h]==NewC1X[i] and C1Yaxis[h]==NewC1Y[i]:
                 count=count+1
        for m in range(3):
             for n in range(NewC2Xlength):        
               if C2Xaxis[m]==NewC2X[n] and C2Yaxis[m]==NewC2Y[n]:
                 count=count+1

        #print(count)
        
        trainingAccuracy=count/6   
        print("The training accuracy is ", trainingAccuracy)       
                

        print("Please input new data point to plot")
        newX=float(input("Please enter in x value: "))#check if x to exit and check is a number
        newY=float(input("Please enter in y value: "))

        UserDataPointsX=[]
        UserDataPointsY=[]

        UserDataPointsX.append(newX)
        UserDataPointsY.append(newY)

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Assignment 1 Problem 2')
        plt.axis([0,5,0,5])
        plt.plot(C1Xaxis, C1Yaxis, "ro",label="C1")
        plt.plot(C2Xaxis, C2Yaxis,"x",label="C2")
        plt.plot(UserDataPointsX, UserDataPointsY, "1")
        plt.legend()
        plt.show()

        if newX>thx and newY>thy:
            print("This data point is in Class 1")
        else:
            print("This data point is in Class 2")

        newDataPoints(UserDataPointsX, UserDataPointsY)

from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np 
from random import randint

(x_train, y_train), (x_test, y_test) = mnist.load_data()
#print(x_train.shape, y_train.shape)
#print(x_test.shape, y_test.shape)
print("The number of images in the training set is ",x_train.shape[0])
print("The number of images in the testing set is ", x_test.shape[0])
print("The wide and height of the image is ", x_train.shape[1], "x", x_train.shape[2])


def plot_fun(images,labels):
  plt.figure() #figsize=(15,8)

  for i in range(0,10):
      digit=i
      x_train_d=images[labels==digit,:,:]
      x_train_i=x_train_d[randint(0,len(x_train_d)),:,:] #selecting a digit from the set
      fig=plt.subplot(2,5,1+digit) 
      fig.imshow(x_train_i,cmap='gray')
      plt.title('Label: ' + str(digit))
  return

print("Selecting 10 random integers from training set")
plot_fun(x_train,y_train)
print("Selecting 10 random integers from testing set")
plot_fun(x_test, y_test)


num_train_img=x_train.shape[0]
train_ind=np.arange(0,num_train_img)
train_ind_s=np.random.permutation(train_ind)
#print(train_ind[1:10])
#print(train_ind_s[1:10])
x_train=x_train[train_ind_s,:,:]
y_train=y_train[train_ind_s]
#selecting 50% of training data
x_valid=x_train[0:int(0.2*num_train_img),:,:]
y_valid=y_train[0:int(0.2*num_train_img)]
#The rest of the training set
x_train=x_train[int(0.2*num_train_img):,:,:]
y_train=y_train[int(0.2*num_train_img):]

print("The number of images in the validation set is ", x_valid.shape[0])
print("The number of images in the training set is ", x_train.shape[0])
print("The number of images in the testing set is ", x_test.shape[0])

