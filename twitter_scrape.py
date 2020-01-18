#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tweepy
import json
import urllib.request, urllib.error, urllib.parse
import pandas as pd 
import re 
import html
import os
from ast import literal_eval
import nltk
from nltk.corpus import stopwords


# In[ ]:


# set working directory


# In[ ]:


ckey = 'kKnjuObMw1bz8IvbOocURToLc'
csecret = 'P9UEWGYsnWHMAkkRPo9q5loClRLBTpNArE8GdO8uIrZIK5VDWG'
atoken = '3147064200-CZf14apOjmZG5t6D5bqEChPGMvzwWrryPQTw8bW'
asecret = 'RbEQLFGTqkVSFjRWr7k8vE3FRnLSjioUGqUVDPrOVd6Ux'

# the authentication process for tweepy
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

print(api)


# In[ ]:


import pandas as pd

df=pd.read_csv('C:/Users/vinit/Desktop/Purdue/Subject/Fall Mod-2/Analyzing Unstrutured Data MGMT 590-049/class/tweets.csv')
df
news_list=df['news'].values.T.tolist()
news_list=list(set(news_list))
news_list


# In[ ]:


maxid = 999999999999999999


# In[ ]:


import time
tweet_text = []
tweet_id = []
tweet_created = []
name_list=[]


for name in news_list:
    
    #name= val+'airlines'+' '+ '-filter:retweets'  
    print(name)

    for i in range(0 , 10):

        if i == 0:
            #get the initial tweets:
            tweets = api.search( q = name , count = 100, lang='en', tweet_mode='extended')

        else:

            tweets = api.search(q = name, count = 100, max_id = maxid, lang='en', tweet_mode='extended')

        maxid = 99999999999999999999

        for tweet in tweets:
            if tweet.id < maxid:
                maxid = tweet.id

                #extract the text from these tweets
                name_list.append(name)
                tweet_text.append(tweet.full_text)
                tweet_id.append(tweet.id)
                tweet_created.append(str(tweet.created_at))

        maxid = maxid - 1
    time.sleep(500)
    


# In[ ]:


print(len(name_list), len(tweet_text), len(tweet_id), len(tweet_created))
print(tweet_text)


# In[ ]:


outputdf=pd.DataFrame(list(zip(name_list, tweet_text,tweet_id,tweet_created)),columns=['news','tweet_text','tweet_id','tweet_date'])

outputdf.to_csv('tweets_output.csv')


# In[ ]:


tweet_list = outputdf['tweet_text'].tolist()


# In[ ]:


for i in range(len(tweet_list)):
    tweet_list[i] = re.sub(r"http\S+", "", tweet_list[i])


# In[ ]:


for i in range(len(tweet_list)):
    tweet_list[i] = html.unescape(tweet_list[i])


# In[ ]:



tweet_list = [i.replace('\n','') for i in tweet_list]
tweet_list = [i.replace('\t','') for i in tweet_list]

