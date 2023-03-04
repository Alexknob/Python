
# Topic Modelling in Python

## Unsupervised Machine Learning to find Tweed Topics

https://ourcodingclub.github.io/tutorials/topic-modelling-python/

## Tutorial Steps

* Introduction and getting started
* Exploring text datasets
* Extracting substrings with regular expressions
* Finding keyword correlations in text data
* Introduction to topic modelling
* Cleaning text data
* Applying topic modelling


### 1. Introduction and getting started

**Useful packages**

* data manipulation: pandas, numpy
* plotting, statistical data visualisation: pyplot, seaborn
* model building: sklearn
* cleaning text, regular expression operations: re

### 2. Exploring text datasets

* to find out the shape of the data set: ````df.shape````
* number of unique tweets: ````df.tweet.unique().shape````
* to apply functions to the values in each cell of a column use ````.apply````

* **String Comparisons**
    * used to compare if two strings or parts of them are the same
    
* **Lambda Functions**
    * quick and dirty :smirk: way to write functions
    * formatting: ````my_lambda_function = lambda x: f(x)````
        * replace ````f(x)```` with any function you want

### 3. Extracting substrings with regular expressions

* **re package**
    * Extra tutorial [here](https://www.datacamp.com/tutorial/python-regular-expression-tutorial)
    * Regular Expression
    * important for text manipulation to extract and replace patterns in string data
 
### 4. Finding keyword correlations in text data

* Flatten data sets with **List Comprehension**
    * https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
* Correlation Matrix
    * seaborn package allows to plot correlation matrix with ````sns.heatmap````
    * Heatmap plot:
        * ![grafik](https://user-images.githubusercontent.com/114161001/222893616-e15a7cbd-eba4-49cb-bf22-188893571d38.png)
          * this shows strong correlation between SaveTerra and SierraClub and GlobalWarming and FoxNews
          * this shows strong negative correlation between tcot and climate
 
### 5. Introduction to topic modelling
