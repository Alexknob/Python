# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 08:25:41 2023

@author: Alexa
"""

#Topic Modelling in Python
#Unsupervised Machine Learning to Find Tweet Topics
#Coding Club
#https://ourcodingclub.github.io/tutorials/topic-modelling-python/

#This script shows how to use topic modelling on twitter data to find what people are tweeting in relation to climate change
    # use of latend drichlet allocation (LDA)
    # non-negative matrix factorisation (NMF)

# Tutorial Aims

    # Introduction and getting started
    # Exploring text datasets
    # Extracting substrings with regular expressions
    # Finding keyword correlations in text data
    # Introduction to topic modelling
    # Cleaning text data
    # Applying topic modelling
    # Bonus exercises


# Introduction and getting started

# Data set: from https://data.world/crowdflower/sentiment-of-climate-change
 
# Import Packages

# packages to store and manipulate data
import pandas as pd
import numpy as np

# plotting packages
import matplotlib.pyplot as plt
import seaborn as sns

# model building package
import sklearn

# package to clean text
import re

# package to clean text data
import nltk
nltk.download('stopwords')
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

# Import Data

df = pd.read_csv('climate_tweets.csv')
  
# Data Exploration

# Number of tweets
print(df.shape)

# Number of unique tweets
print(df.tweet.unique().shape)

# String Comparisons

# Lambda Functions

    # Example
    
    # normal function example
def my_normal_function(x):
    return x**2 + 10

    # lambda function example
my_lambda_function = lambda x: x**2 + 10


# Finding Retweets

# how many retweets are there in the data set?

# make a new column to highlight retweets
    # call new column is_retweet
    # check in the tweet column if the first two characters are RT
    # store this in the new column
df['is_retweet'] = df['tweet'].apply(lambda x: x[:2]=='RT')
    # sum the number of entries in the is_retweet column
print(df['is_retweet'].sum())  # number of retweets

# how many unique retweets are there?

# number of unique retweets
    # check the is_retweet column of unique values
    # dataframe.loc allows to check a group of rows and columns of the dataframe by labels and for boolean (true, false) values
print(df.loc[df['is_retweet']].tweet.unique().size)

# how many popular tweets are there?

# count number of times a tweet is repeated
# sort by the number of times each tweet appears
# look up the first top 10 tweets
# 10 most repeated tweets
    # group the dataframe by the values in the tweet column
    # return number of elements in tweet column with .size
    # create a new index named counts, this adds the old index as column and puts in a new sequential index
    # sort counts values in descending order with sort_values
    # get first 10 values with head
df.groupby(['tweet']).size().reset_index(name='counts')\
  .sort_values('counts', ascending=False).head(10)

# how are the top ten tweets distributed?

# number of times each tweet appears
counts = df.groupby(['tweet']).size()\
           .reset_index(name='counts')\
           .counts

# define bins for histogram
my_bins = np.arange(0,counts.max()+2, 1)-0.5

# plot histogram of tweet counts
plt.figure()
plt.hist(counts, bins = my_bins)
plt.xlabels = np.arange(1,counts.max()+1, 1)
plt.xlabel('copies of each tweet')
plt.ylabel('frequency')
#plt.yscale('log', nonposy='clip')
plt.show()


# Extracting substrings with regular expressions

# Find who is tweeting the most, retweeting the most, and most common hashtags

# Use Re package

# Define Functions
# use re.findall to search for string patterns in tweet column

    # Who is being retweeted
def find_retweeted(tweet):
    '''This function will extract the twitter handles of retweed people'''
    return re.findall('(?<=RT\s)(@[A-Za-z]+[A-Za-z0-9-_]+)', tweet)

    # Who is being mentioned
def find_mentioned(tweet):
    '''This function will extract the twitter handles of people mentioned in the tweet'''
    return re.findall('(?<!RT\s)(@[A-Za-z]+[A-Za-z0-9-_]+)', tweet)  

    # Which hashtags are used
def find_hashtags(tweet):
    '''This function will extract hashtags'''
    return re.findall('(#[A-Za-z]+[A-Za-z0-9-_]+)', tweet)   

# Create column each for retweets, people mentioned and hashtags

# make new columns for retweeted usernames, mentioned usernames and hashtags
df['retweeted'] = df.tweet.apply(find_retweeted)
df['mentioned'] = df.tweet.apply(find_mentioned)
df['hashtags'] = df.tweet.apply(find_hashtags)


# Finding keyword correlations in text data

# What are the most popular hashtags?

# Filter dataframe for rows that contain a hashtag

# take the rows from the hashtag columns where there are actually hashtags
hashtags_list_df = df.loc[
                       df.hashtags.apply(
                           lambda hashtags_list: hashtags_list !=[]
                       ),['hashtags']]

# separate out hashtags so that each hashtag has its own row
    # do a list comprehension
    
# create dataframe where each use of hashtag gets its own row
flattened_hashtags_df = pd.DataFrame(
    [hashtag for hashtags_list in hashtags_list_df.hashtags
    for hashtag in hashtags_list],
    columns=['hashtag'])

# find number of unique hashtags

# number of unique hashtags
print(flattened_hashtags_df['hashtag'].unique().size)

# find top hashtags by frequency of appearance

# count of appearances of each hashtag
popular_hashtags = flattened_hashtags_df.groupby('hashtag').size()\
                                        .reset_index(name='counts')\
                                        .sort_values('counts', ascending=False)\
                                        .reset_index(drop=True)

# Distribution of how often hashtags appear

# number of times each hashtag appears
counts = flattened_hashtags_df.groupby(['hashtag']).size()\
                              .reset_index(name='counts')\
                              .counts

# define bins for histogram                              
my_bins = np.arange(0,counts.max()+2, 5)-0.5

# plot histogram of tweet counts
plt.figure()
plt.hist(counts, bins = my_bins)
plt.xlabels = np.arange(1,counts.max()+1, 1)
plt.xlabel('hashtag number of appearances')
plt.ylabel('frequency')
#plt.yscale('log', nonposy='clip')
plt.show()


# Find correlated hashtags
 
    # turn text into numeric form: transform list into a vector
    # need to limit amount of hashtags: we cannot correlate hashtags that only appear once or only a few times
    
# take hashtags which appear at least this amount of times
min_appearance = 10

# find popular hashtags - make into python set for efficiency
popular_hashtags_set = set(popular_hashtags[
                           popular_hashtags.counts>=min_appearance
                           ]['hashtag'])

# filter only popular hashtags in the hashtags_df 
# drop rows with no popular hashtags

# make a new column with only the popular hashtags
hashtags_list_df['popular_hashtags'] = hashtags_list_df.hashtags.apply(
            lambda hashtag_list: [hashtag for hashtag in hashtag_list
                                  if hashtag in popular_hashtags_set])
# drop rows without popular hashtag
popular_hashtags_list_df = hashtags_list_df.loc[
            hashtags_list_df.popular_hashtags.apply(lambda hashtag_list: hashtag_list !=[])]


# vectorise hashtags in each tweet

# make new dataframe
hashtag_vector_df = popular_hashtags_list_df.loc[:, ['popular_hashtags']]

for hashtag in popular_hashtags_set:
    # make columns to encode presence of hashtags
    hashtag_vector_df['{}'.format(hashtag)] = hashtag_vector_df.popular_hashtags.apply(
        lambda hashtag_list: int(hashtag in hashtag_list))

print(hashtag_vector_df)
    # for each popular hashtag there should be a 1 in the corresponding hashtag column
    
# drop popular_hashtags column from the hashtag_vector_df
hashtag_matrix = hashtag_vector_df.drop('popular_hashtags', axis=1)

# calculate the correlation matrix
correlations = hashtag_matrix.corr()

# plot the correlation matrix
plt.figure(figsize=(10,10))
sns.heatmap(correlations,
    cmap='RdBu',
    vmin=-1,
    vmax=1,
    square = True,
    cbar_kws={'label':'correlation'})
plt.show()


# Introduction to topic modelling


# Cleaning Text Data

# Goal: what are the general things people are talking about? 

# Remove Links included in tweets
    # create remove_links function
    # this takes any string and removes any link structure specified below
    
def remove_links(tweet):
    '''Takes a string and removes web links from it'''
    tweet = re.sub(r'http\S+', '', tweet) # remove http links
    tweet = re.sub(r'bit.ly/\S+', '', tweet) # rempve bitly links
    tweet = tweet.strip('[link]') # remove [links]
    return tweet

# Remove users included in tweets
    # create remove:users function
    # this takes any tweet and removes users that were tagged or replied to
    
def remove_users(tweet):
    '''Takes a string and removes retweet and @user information'''
    tweet = re.sub('(RT\s@[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet) # remove retweet
    tweet = re.sub('(@[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet) # remove tweeted at
    return tweet

# Make one Master Function combining above functions to clean tweets

# my_stopwords variable to store removed uneccessary words in case they may be interesting
my_stopwords = nltk.corpus.stopwords.words('english')
# word_rooter variable to store stemmed words
    # caution: this is only a rule-of-thumb function and may treat similar words differently
word_rooter = nltk.stem.snowball.PorterStemmer(ignore_stopwords=False).stem
# define punctuation that will be removed, all except #
my_punctuation = '!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~•@'

# cleaning master function
def clean_tweet(tweet, bigrams=False):
    # remove users with the above user function
    tweet = remove_users(tweet)
    # remove links with the above links function
    tweet = remove_links(tweet)
    # make entire tweet lower case
    tweet = tweet.lower() # lower case
    # remove any punctuation
    tweet = re.sub('['+my_punctuation + ']+', ' ', tweet) # strip punctuation
    # remove double spacing
    tweet = re.sub('\s+', ' ', tweet) #remove double spacing
    # remove numbers
    tweet = re.sub('([0-9]+)', '', tweet) # remove numbers
        # we now have lowercase tweets equally spaced and with only # punctuation
    # change tweets from string into list of words
    # remove stopwords and store these removed words in my_stopwords variable
    tweet_token_list = [word for word in tweet.split(' ')
                            if word not in my_stopwords] # remove stopwords
    # stem words by removing ending so that words have similar word stems and store stemmed words in word_rooter variable
    tweet_token_list = [word_rooter(word) if '#' not in word else word
                        for word in tweet_token_list] # apply word rooter
    # group every pair of words and put them to the end so that we keep information on word ordering
    if bigrams:
        tweet_token_list = tweet_token_list+[tweet_token_list[i]+'_'+tweet_token_list[i+1]
                                            for i in range(len(tweet_token_list)-1)]
    # join at the end
    tweet = ' '.join(tweet_token_list)
    return tweet

# apply function to data frame
df['clean_tweet'] = df.tweet.apply(clean_tweet)


# Applying TOpic Modelling

# import necessary package to transform into vector
from sklearn.feature_extraction.text import CountVectorizer

# the vectorizer object will be used to transform text to vector form
    # remove words that appear > 90% in data frame
    # remove words that appear in < 25 tweets
vectorizer = CountVectorizer(max_df=0.9, min_df=25, token_pattern='\w+|\$[\d\.]+|\S+')

# apply transformation
    # this will show the term frequency: frequency of each word appearing
tf = vectorizer.fit_transform(df['clean_tweet']).toarray()

# tf_feature_names tells us what word each column in the matric represents
    # look which word made it through the filter
tf_feature_names = vectorizer.get_feature_names()

# create model object

# import packages for modelling
from sklearn.decomposition import LatentDirichletAllocation

# choose 10 topics (can change that)
number_of_topics = 10

# build model with LDA
    # will choose 10 topics
    # has fitting method
    # output: how important different words are in different topics
model = LatentDirichletAllocation(n_components=number_of_topics, random_state=0)

# apply model
model.fit(tf)

# inspect generated topics

# define function that shows the topics found from the model and the number of words we would like to see
def display_topics(model, feature_names, no_top_words):
    topic_dict = {}
    for topic_idx, topic in enumerate(model.components_):
        topic_dict["Topic %d words" % (topic_idx)]= ['{}'.format(feature_names[i])
                        for i in topic.argsort()[:-no_top_words - 1:-1]]
        topic_dict["Topic %d weights" % (topic_idx)]= ['{:.1f}'.format(topic[i])
                        for i in topic.argsort()[:-no_top_words - 1:-1]]
    return pd.DataFrame(topic_dict)

# apply to model
# choose 10 words to be seen
no_top_words = 10
display_topics(model, tf_feature_names, no_top_words)

