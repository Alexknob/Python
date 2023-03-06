
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

**Topic Modelling**
   * machine learning algorithm to discover topics in a collection of documents

**Two Versions**
   * Both take a matrix with
      * row = 1 document
      * column = 1 word
      * at each row-column intersection: number of times that a given word appears in the document (bag-of-words format)
   * Topic Modelling algorithm forms topics from the matrix words
   * algorithm looks at co-occurence of words in the documents
   * if words appear together often in the same document they are likely to form a topic
   * based on this algorithm will form topics (list of words that appear often together) and score words in the topic
   * the higher the score the more important the topic
   * but: we have to decide what topics mean
      * **Latend Dirichlet Allocation (LDA)**
         * Input: number of topics chosen, fitting method
         * Output: fitted parameters that tell how important different words are in different topics
         * works well on long text documents but not so good on short text documents like tweets
      * **Non-negative Matrix Factorisation (NMF)**
        

### 6. Cleaning text data

* most important to apply topic modelling algorithm: clean data
* Python package: ```nltk```
* *Master function* = combines sub-functions into one big function making code more reusable
* Removal of *Stopwords* = words that do not tell us much
* *Stemmig* words = remove the end of the words so similar words will be viewed as the same by the algorithm because they have the same word stem
* *Bigram* function = word pair combination like i_scream scream_for for_ice ice_cream, this is done to keep the information of word ordering when converting sentences into vector form, we can then filter the vector for unnatural bigrams that do not make sense and remove them


### 7. Applying Topic Modelling

* Output:

![image](https://user-images.githubusercontent.com/114161001/223081624-8a67680c-ec25-46af-ad5a-4b21fbd02c9e.png)

  
