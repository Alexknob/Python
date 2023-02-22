# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 15:35:31 2023

@author: Alexa
"""

#Python Data Analysis with Pandas and Matplotlib
#Coding Club
#https://ourcodingclub.github.io/tutorials/pandas-python-intro/

#This script shows how to work with basic Pandas commands and data structures

# Tutorial Aims

 # Understand what Pandas is
 # Ways of running Python and Pandas
 # Understanding the basic Pandas data structures
 # Learn how to access data from a Pandas DataFrame
 # Learn how to filter data in a Pandas DataFrame
 # Learn how to read and sort data from a file
 # Understand the basics of the Matplotlib plotting package
 # Learn how to bring together other packages to enhance your plots
 # Learn how to further customise the appearance of Matplotlib plots
 # Bonus Matplotlib: plotting data onto maps with Cartopy

# Import pandas

import pandas as pd

print(pd.__version__)

# Tutorial Data: Data about scottish mountains containing heights and coordinates of mountains


#  Understanding the basic Pandas data structures

# Create a data series

my_series = pd.Series([4.6, 2.1, -4.0, 3.0])
print(my_series)
# this returns the values and the index numbers

print(my_series.values)
# this returns just the values

# Create data frame from Python dictionary

# Note that dictionaries are part of the core Python language
# You do not need 'import pandas' if you are only working with dictionaries.
hungarian_dictionary = {'spaceship': 'űrhajó'}

# Look up an item in the dictionary
hungarian_dictionary['spaceship']

# multiple key-value pairs
hungarian_dictionary = {'spaceship': 'űrhajó',
                        'watermelon': 'görögdinnye',
                        'bicycle': 'kerékpár'}

# multiple key-value pairs with several values per key
# Names (keys) mapped to a tuple (the value) containing the height, lat and longitude.
scottish_hills = {'Ben Nevis': (1345, 56.79685, -5.003508),
                  'Ben Macdui': (1309, 57.070453, -3.668262),
                  'Braeriach': (1296, 57.078628, -3.728024),
                  'Cairn Toul': (1291, 57.054611, -3.71042),
                  'Sgòr an Lochain Uaine': (1258, 57.057999, -3.725416)}

# look up mountain key
print(scottish_hills['Braeriach'])
# this gives back the height and coordinates

# manually create a data frame

# load created dictionary in a data frame
dataframe = pd.DataFrame(scottish_hills)
print(dataframe)
# prints data in wide format

# manually create data in long format
# restructure dictionary

scottish_hills = {'Hill Name': ['Ben Nevis', 'Ben Macdui', 'Braeriach', 'Cairn Toul', 'Sgòr an Lochain Uaine'],
                   'Height': [1345, 1309, 1296, 1291, 1258],
                   'Latitude': [56.79685, 57.070453, 57.078628, 57.054611, 57.057999],
                   'Longitude': [-5.003508, -3.668262, -3.728024, -3.71042, -3.725416]}

# load created dictionary in a data frame
dataframe = pd.DataFrame(scottish_hills)
print(dataframe)
# prints data in long format

# order column names of data frame
dataframe = pd.DataFrame(scottish_hills, columns=['Hill Name', 'Height', 'Latitude', 'Longitude'])
print(dataframe)
# prints data in long format ordered by specified column order


 # Learn how to access data from a Pandas DataFrame


# First few rows of data frame
print(dataframe.head(3))

# Last few rows of data frame
print(dataframe.tail(2))

# Access one column
print(dataframe['Hill Name'])
print(dataframe['Height'])

# Access row index number
print(dataframe.iloc[0])

# Access row and column index
print(dataframe.iloc[0,0])

# Alternative way
print(dataframe['Hill Name'][0])

# Access dataframe column quickly
print(dataframe.Height)


 # Learn how to filter data in a Pandas DataFrame

# Filter out data
print(dataframe.Height > 1300)
# returns true and false values

# Actually filter out data
print(dataframe[dataframe.Height > 1300])

# Append data to a dataframe
dataframe['Region'] = ['Grampian', 'Cairngorm', 'Cairngorm', 'Cairngorm', 'Cairngorm']

print(dataframe)


# Learn how to read and sort data from a file

# read in data with read_csv
dataframe = pd.read_csv("scottish_hills.csv")
print(dataframe.head(10))

# order values by height in descending way with sort_values
sorted_hills = dataframe.sort_values(by=['Height'], ascending=False)

# Let's have a look at the top 5 to check
print(sorted_hills.head(5))


# Understand the basics of the Matplotlib plotting package

# import pyplot
import matplotlib.pyplot as plt

# look at relationship of hill height and hill latitude

# define variables
x = dataframe.Height
y = dataframe.Latitude

# Scatterplot
plt.scatter(x, y)
plt.show()

# save figure
plt.savefig("my_chart_name.png")


# Learn how to bring together other packages to enhance your plots

# Import statistical library scipy
from scipy.stats import linregress

# Use linear regression
stats = linregress(x, y)

m = stats.slope
b = stats.intercept

# build linear regression funcrion
plt.scatter(x, y)
plt.plot(x, m * x + b, color="red")   # I've added a color argument here

plt.savefig("figure.png")


# Learn how to further customise the appearance of Matplotlib plots

# modify plot details

# Change the default figure size
plt.figure(figsize=(10,10))

# Change the default marker for the scatter from circles to x's
plt.scatter(x, y, marker='x')

# Set the linewidth on the regression line to 3px
plt.plot(x, m * x + b, color="red", linewidth=3)

# Add x and y lables, and set their font size
plt.xlabel("Height (m)", fontsize=20)
plt.ylabel("Latitude", fontsize=20)

# Set the font size of the number lables on the axes
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

plt.savefig("python-linear-reg-custom.png")


# Bonus Matplotlib: plotting data onto maps with Cartopy

import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.feature as cfeature

plt.figure(figsize=(20,10))
ax = plt.axes(projection=ccrs.Mercator())
ax.coastlines('10m')

ax.xaxis.set_visible(True)
ax.yaxis.set_visible(True)

ax.set_yticks([56,57,58,59], crs=ccrs.PlateCarree())
ax.set_xticks([-8, -6, -4, -2], crs=ccrs.PlateCarree())

lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()

ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)

ax.set_extent([-8, -1.5, 55.3, 59])

plt.scatter(dataframe['Longitude'],dataframe['Latitude'],
                    color='red', marker='^', transform=ccrs.PlateCarree())
plt.savefig("munros.png")

