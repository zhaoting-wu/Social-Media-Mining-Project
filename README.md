## Project of EECS 510: Social Media Mining

Members: **Zhaoting Wu, Yijie Wu**
Emails: **{zhaotingwu2020, yijiewu2018}@u.northwestern.edu**

# Introduction

Accurate disease forecasts are imperative when preparing for influenza epidemic outbreaks. This need has driven the research community to bring a multitude of influenza forecasting methods to bear, drawing upon a wide range of statistical techniques and laboratory, clinical, epidemiological, climatological, and demographic data sources. Nevertheless, disease forecasts are often limited by the time required to collect new, accurate data.
With the help of social networking such as Twitter, Facebook and Instagram, This task now becomes durable since each of those generates TB level of real time dataset everyday and they are easy to acquire with the API provided by the companies.
In this paper, we will mainly focus on utilizing the power of Twitter and try to  understand the some of the key factors that is related to disease Flu. We are especially interested in the Geo distribution of the outbreak of the flu as well as the outbreak time duration. We will also try to understand the sentiment related to this.

# Data Source and Collection
## Data Source

The datasource for this project is Twitter. Twitter is one of the famous social networking services where user can read and post messages which are 148 characters in length. Twitter messages are also called as Tweets. We will use these tweets as raw data. The reason we chose twitter as our data source is due to the fact that Twitter is a real time social media and it provides enough information we needed for this project.

## Data Collection

We use the tweepy package provided the Twitter Company. We wrote a Python script to automatically retrieve the related tweets that we are interested and stored them into an online server. We deployed the program on Amazon AWS and collected data extensively for 21 days(5/7/2017-6/1/2017).  We define 2 subsets of keyword filters for this project. The filter one which contains the list of keywords[get a flu, catch a cold, sore throat] is used to generate dataset 1, and the list of keywords[flu, cough] is used to generate dataset 2.
The raw dataset we have is about 859.1 MB for the dataset 1 and 1.65GB for the dataset2. All the raw data is stored as JSON format.

## Data Selection and Cleaning

After we acquired the original raw dataset, we further decided to extract certain features from it. The key features we chose are listed below:
 tweets['created_at']          The time when this tweet is posted
 tweets['id']                  The id of this user
 tweets['text']                The content of the tweet
 tweets['source']      	       The links this tweet refers to
 tweets['screen_name']         The user name
 tweets['location']            The location where this tweet is posted
 tweets['followers'] 	         The amount of followers for the user
 tweets['friends'] 	           The amount of friends for the user
 tweets['time_zone']           The time zone this user belongs to
 
We wrote another python script to automatically extract this key features from our dataset and stored it as a pandas dataframe for future analysis.

# Data Analysis

## Geo Distribution

For this section, we are mainly interested to understand the Geo distribution of the outbreak                                                                           of the flu. The granularity we chose is to do is State level analysis within the U.S. due to the fact of the sparsity of twitter’s geo information. In a random sample of over 1 million Twitter users, only 26% have listed a user location as granular as a city name (e.g., Los Angeles, CA); the rest are overly general (e.g., California), missing altogether, or nonsensical (e.g., Wonderland). 
Before doing any geo related analysis, we first wrote a python script to regularize the geo information in the twitter. The goal of this script is to convert various user provided location information to a standard form- abbreviation of the State name. (e.g if the user provided location is Chicago, this script will return IL as its result)

## Time Distribution

For this section, we are mainly interested to understand the time distribution of the outbreak                                                                           of the flu. Due to the limitation of the length of this quarter. We have only collected the data intensively for 21 days(5/7/2017-6/1/2017) and then we analyze the outbreak clustered by date for both dataset 1 and dataset 2. Even the time window we have is short, which only spans about 21 days, we still managed to draw some interesting insights from our datasets. 
Before we are able to process any data, we, like before, wrote a Python script to convert the time format to the standard YYYY-mm-dd format. The key part of code to achieve is listed below.

## Sentiment Analysis

For this section, we are interested in the sentiment distribution of the outbreak of the flu. Although getting a flu is not a good stuff, some cases maybe still impact people’s opinion on the flu. We need to do sentiment analysis about this aspect to check whether the results follow our intuition. If not, we need to make it clear why this result happens.

### Sentiment Analysis by Geo Locations 

Firstly, we combine the sentiment with the location. We are interested in whether people from different locations will have different views on the flu. From the same logic, to achieve this goal, we firstly divide all the data into different dataset according to the location of each tweet, and we use a sentiment analyze calculator to calculate the polarity value of the text of each tweet, then we check which type this tweet belongs to in the type list of positive, neutral and negative. 

### Sentiment Analysis by Dates

Except the sentiment distribution along with geo location, we also want to know the sentiment distribution by dates. People’s attitudes towards flu maybe vary with different time, for example, in weekdays, people are annoyed with works, so they maybe tend to have negative attitude about the flu, but in weekend, people always have a good mood, the sentiment about flu will be neutral, even positive.

## Geo Locations CLustering Analysis

Generally, diseases have a source of outbreak, and the center of source usually reports the disease most frequently. In order to find the regions with the most frequent flu outbreak in US, we conduct a machine learning method to analyze the detailed relations.

