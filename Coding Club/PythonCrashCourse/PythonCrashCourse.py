# -*- coding: utf-8 -*-

#Python Crash Course
#Coding Club
#https://ourcodingclub.github.io/tutorials/python_crash_course/

#This script introduces the basic python commands.


#Print and type function
 x=5.0
 print(type(x))
 
 #Integers
 
 x = 5
 y= 89
 year=2018
 
 print(type(x))
 
 #Dictionaries
 
 my_dictionary = { "jurassic park": "life finds a way",
                  "terminator": ["i'll", "be", "back"]  }

print(my_dictionary['jurassic park'])

# Simple Maths & Operators

print('winter' + 'coming')

print(34 + 99)

print(True + True)

print (4 + 2)

print ('4' + '2')

print(20/4)

print(14*3)

print(12%5)

print(2**4)

# Comparison Operators

print (5 > 12)

print(17 >= 17)

print(1==0)

# Boolean Operators

print(True & True)

print(False & True)

print(True | False)

print (True | True)

print(False & True)

# boolean operators can be replaced with and, or and not

to_be = True
print(to_be or not to_be)

# Loops

# this is the list of number we would like to find the mean of
precip = [2,7,1,9,0,2,4,5]

# we make a variable total which we can add the items from the list to
total=0

# in this next line we say we will repeat this adding loop 8 times
# during this loop the variable i will take on the values 0-7, increasing by 1 on each pass
for i in range(8):
    # on each pass we add the next number to the total we have so far
    total = total + precip[i]

# finally we will divide by the number of items to get the mean
mean_precip = total / 8

print(mean_precip)

# Functions

# We would like to know the mean of each sample

daily_precipitation_edinburgh = [2,7,1,9,0,2,4,5]
daily_precipitation_glasgow = [5,5,3,6,7,3,2,8]
daily_precipitation_dundee = [4,2,5,7,2,6,8,7]

# Define Function
# the def keyword tells python you are about to make a function
# the variable name that comes after 'def' is the function name
# in this case our function is called my_mean
# x is a stand in for our input. We call it x but it could have been any variable name at all
def my_mean(x):
  # we make a variable total which we can add the items from the list to
  total=0

  # in this next line we say we will repeat this adding loop 8 times
  # during this loop the variable i will take on the values 0-7, increasing by 1 on each pass
  for i in range(8):
      # on each pass we add the next number to the total we have so far
      total = total + x[i]

  # finally we will divide by the number of items to get the mean
  mean_value = total / 8

  # in this final line we return the answer
  # the rest of the variables here, like total, will be thrown away
  return mean_value

# Run Function
mean_precipitation_edinburgh = my_mean(daily_precipitation_edinburgh)
print(mean_precipitation_edinburgh)

print(my_mean(daily_precipitation_glasgow))

# if-else statements

# set the today variable
today='Thursday'

# check if today is friday
if today=='Friday':
  # if today is friday then this is printed
  print("Why not go home early?")
else:
  #if today is not friday then this is printed
  print("Hard work is a virtue! You can do it! I believe in you!")


# Packages

# first we invite numpy over : import numpy
# at the same time we give numpy the nickname np : as np
import numpy as np

# here is the data we want to investigate
x = [1,3,6,2,8,4,1]

# now that numpy (np) is here we can ask them to use their mean function
x_mean = np.mean(x)
# then we ask numpy to use its standard deviation function on the data
x_standard_dev = np.std(x)

# finally we will print the result
print(x_mean)
print(x_standard_dev)


