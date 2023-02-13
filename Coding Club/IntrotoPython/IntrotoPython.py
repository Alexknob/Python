# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 10:58:39 2023

@author: Alexa
"""

#Intro to Python
#Coding Club
#https://ourcodingclub.github.io/tutorials/python-intro/

#This script shows how to import and explore data in Python
#and how to produce good scientific code

# Tutorial Aims

# Understand why Python is so useful for scientific programming
# Installing Python and running a simple Python program
# Reading data from a file
# Get a feel for how Python looks and feels
# Load data from a text file into memory and basic data structures
# Moving beyond the core Python language with modules
# A brief introduction to data analysis with the pandas package
# Plotting data with Matplotlib


# Understand why Python is so useful for scientific programming


# simplicity of code language
"Python".startswith("P")

"thon" in "Python"

print("xyz" in "Python")

tastyword = "chocolate"
x = 3

if tastyword.count("o") < x and tastyword.endswith("e"):
  print("You have won some tasty chocolate!")
  

# Installing Python and running a simple Python program

print("Hello, World!")


# Data Exploration
# Explore Data from GeoSciences weather station
# collected 02.01.2018 - 03.01.2018


# Reading data from a file

# Version 1

# open csv file and call it weatherfile
weatherfile = open("StormEleanor_2_3_Jan.csv", "r")

# print each line in the file
for line in weatherfile:
  print(line)

# close the file
weatherfile.close()

# Version 2

# open csv file and assign it the name weatherfile
with open("StormEleanor_2_3_Jan.csv", "r") as weatherfile:
  for line in weatherfile:
    print(line)


# Get a feel for how Python looks and feels
# A note on code blocks
  
  
# Load data from a text file into memory and basic data structures

# check data type
with open("StormEleanor_2_3_Jan.csv", "r") as weatherfile:
  for line in weatherfile:
    print(type(line))
    
# this shows that imported data is string data
# need to change text file data into nummerical data 
# and tell python to split data by ,
with open("StormEleanor_2_3_Jan.csv", "r") as weatherfile:
  for line in weatherfile:
    print(line.split(','))
    
# tell python to seperate file by columns
with open("StormEleanor_2_3_Jan.csv", "r") as weatherfile:
  for line in weatherfile:
      # create a variable called data_row to store each line of the text file in a list
    data_row = line.split(',')
    # get each value of pressre by indexing data row with the number 6
    # note that python starts counting from 0
    pressure = data_row[6]
    print(pressure)
    
# tell python not to overwrite pressure every time we run the loop
# create a list of pressure values and store it as variable

# create empty list outside of the with block
pressure_data = []

with open("StormEleanor_2_3_Jan.csv", "r") as weatherfile:
  for line in weatherfile:
    data_row = line.split(',')
    pressure = data_row[6]
    # add pressure values to epmty list
    pressure_data.append(pressure)

# check data
# Oh no! This is the header line!
print(pressure_data[0])   # Prints: 'Pair_avg'

# Argh! This is a string!
print(type(pressure_data[1]))  # Prints: 'str'

# skip header line and change data type
pressure_data = []

with open("StormEleanor_2_3_Jan.csv", "r") as weatherfile:
  # tell python to skip to the next line within the csv file
  next(weatherfile)
  for line in weatherfile:
    data_row = line.split(',')
    pressure = data_row[6]
    # change data type to floats
    pressure_data.append(float(pressure))
    
# recheck data
print(pressure_data[0])
print(type(pressure_data[1]))
# All good!


# Moving beyond the core Python language with modules

# Import csv module to deal with csv files

import csv

pressure_data = []   # Create an empty list as before to store values

# open data set and store it as variable name csvfile
with open('StormEleanor_2_3_Jan.csv', 'r') as csvfile:
  # skip first line
  next(csvfile)
  # csv.reader reads the file
  # but it will read all non-quoted values as strings and the rest as numeric values
  for row in csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC):
    pressure_data.append(row[6])

# Check our variables look okay and they are the correct type:
print(pressure_data)
print(type(pressure_data[1]))


# A brief introduction to data analysis with the pandas package

# import pandas and give it the nickname pd
import pandas as pd

# import data file
data = pd.read_csv('StormEleanor_2_3_Jan.csv', delimiter=',', header=0)

# Explore data
# extract air pressure data
pressure_data = data['Pair_Avg']
print(pressure_data)


# Plotting data with Matplotlib

# import matplotlib
# indicate with .pyplot that we only import a submodule from matplotlib
import matplotlib.pyplot as plt

# Plot pressure data
plt.plot(pressure_data)
plt.savefig("pressure.png")

# Make Plot pretty
plt.ylabel("Pressure (hPa)")
plt.title("Average Pressure, JCMB Weather Station, 2-3rd Jan 2018")

# convert x axis steps into time steps with the datetime module

# import the required libraries and modules
import datetime

# Code to create the timeseries values
date_time_series = []
date_time = datetime.datetime(2018, 1, 2)
date_at_end = datetime.datetime(2018, 1, 3, 23, 59)
step = datetime.timedelta(minutes=1)

while date_time <= date_at_end:
  date_time_series.append(date_time)
  date_time += step

print(date_time_series)

# Make plot more pretty

import pandas as pd
import matplotlib.pyplot as plt
import datetime

data = pd.read_csv('StormEleanor_2_3_Jan.csv', delimiter=',', header=0)

pressure_data = data['Pair_Avg']

date_time_series = []
date_time = datetime.datetime(2018, 1, 2)
date_at_end = datetime.datetime(2018, 1, 3, 23, 59)
step = datetime.timedelta(minutes=1)

while date_time <= date_at_end:
  date_time_series.append(date_time)
  date_time += step

# plot time step on x-axis and pressure on y-axis
plt.plot(date_time_series, pressure_data)
plt.ylabel("Pressure (hPa)")
plt.xlabel("Time")
plt.title("Average Pressure, JCMB Weather Station, 2-3rd Jan 2018")
plt.xticks(rotation=-60)
plt.tight_layout()
plt.savefig("pressure_final.png")

