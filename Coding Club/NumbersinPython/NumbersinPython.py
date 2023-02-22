# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 19:40:57 2023

@author: Alexa
"""

#INumbers in Python
#Coding Club
#https://ourcodingclub.github.io/tutorials/numpy/

#This script shows how to 

# Tutorial Aims

# What is NumPy?
# Basic manipulation NumPy arrays
# Masked arrays
# Reading and writing data
# Cautions when using NumPy arrays



# What is NumPy?

# List of values and square each of them

a = [1, 2, 3, 4, 5]
b = []
for i in a:
    b.append(a**2)

print(b)

# 2 dimensional array and sqzare each array element
# requires 2 nested loops

a = [[1, 2], [3, 4]]
b = [[],[]]

for i in range(len(a)):
    for j in range(len(a[i])):
        b[i].append(a[i][j]**2)
        
# 3 dimensional array
# requires 3 nested loops

# Easier code with NumPy

import numpy as np

b = np.array(a)**2


# Basic manipulation NumPy arrays

# Import Package numpy

import numpy as np

# Creation of NumPy arrays

# Versions:

# 2 dimensional array with 5 rows and 6 columns and every element has value 10
a = np.full((5, 6), 10.0)

# 3 dimensional array of size 2x2x2 with every element as 1 
b = np.ones((2, 2, 2))

# 1 dimensional array of size 3 with every element as 0
c = np.zeros(3)

for i in [a, b, c]:
    print(i)
    
# Creation of different dimensional arrays by reshaping them
# a is transformed into a 2D array of size 3x3
a = np.arange(9.0).reshape(3,3)
print(a.shape)


# Accessing and slicing data

# arrange in 10x3 array with 30 values
a = np.arange(30.).reshape(10, 3)
# the next line will print the first row of the array
print(a[0])
# the next line will print the last row of the array
print(a[-1])
# which should be same as:
print(a[2])
# the next line will print the value in the third row and first column
print(a[2,0])


# Select a range of rows

a = np.arange(30.)
# selects the elements in positions from 11 to 20
print(a[10:20])

# selects the elements in positions from start to 10
print(a[:10])
# which should be same as:
print(a[0:10])

# selects the elements in positions from 20 to last
print(a[20:])
# which should be same as:
print(a[20:30])


# Slice columns

# 2 dimensional array
a = np.arange(30.).reshape(10,3)
# select second column
print(a[:, 1])
# select columns 1 (second) and 2 (third)
print(a[:, 1:3])

# 3 and 4 dimensional array
# create 3d array with dimensions (time, latitude, longitude)
a = np.zeros((3, 3, 3))
# create 4d array with dimensions (time, height, latitude, longitude)
b = np.zeros((3, 3, 3, 3))

# add 1 to the first columns
a[:, :, 0] += 1.
b[:, :, :, 0] += 1.

# or with a loop
# add 1 to the first columns simultaneously to a and b arrays
for i in [a, b]:
    i[..., 0] += 1.


# Striding (selecting every other row)

# get every other row
a = np.arange(27.).reshape(9, 3)
print(a[::2])

# Indexing of values

# get diagonal values in the 5x5 array using fancy indexing
b = np.arange(25).reshape(5, 5)
print(b[[0, 1, 2, 3, 4],[0, 1, 2, 3, 4]])

# Boolean arrays (array with True and False values)

# use Boolean array to create 1d array of selection
c = np.array([[0., 1., 2.], [2., 3., 4.]])
d = np.array([[True, False, False], [False, True, True]])
print(c[d])

# create and use the Boolean array to selectively change data
e = np.arange(9.).reshape(3, 3)
f = e>5  # select values greater than 5.0
e[f] = 10.  # make all values greater than 5.0 to 10.0
print(e)
# or you can simply do
e = np.arange(9.).reshape(3, 3)
e[e>5] = 10.0


# Masked Arrays

# array with missing data and we want the row sum
a = np.array([[np.nan, 3., 1.], [2., 8., 5.]])
print(np.sum(a, axis=1))

# use masked arrray to ignore NA values
a = np.array([[np.nan, 3., 1.], [2., 8., 5.]])
print(np.sum(np.ma.masked_invalid(a), axis=1))

# use to remove unneeded values
# here remove all values lower than 5
magnitude = np.array([2., 5., 6., 1.])
damage = np.array([1000., 100000., 110000, 10.])
print(np.sum(np.ma.masked_where(magnitude<5.0, damage)))


# Reading and writing data


# read in csv file with pandas and convert it to NumPy arrays
import numpy as np
import pandas as pd

# read file as pandas.DataFrame then get values
# data = pd.read_csv('your_csv_file').values

# save csv file using numpy
# np.savetxt('save_file.csv', your_data, delimeter=',', comments='')

# store data in binary format (it does not matter if it is human readable or not)
# save one data to npy file
# np.save('save_file1.npy' ,data)
# save collection of data to single npz file
# dataset = {'temperature': data1,
#		   'humidity': data2}
# np.savez('save_file2.npz', **dataset)

# reopen files
# open_data = np.load('save_file1.npy')
# open_dataset = np.load('save_file2.npz')
# access data in dataset
# temperature = open_dataset['temperature']

# Cautions when using NumPy