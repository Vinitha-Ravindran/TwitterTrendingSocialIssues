#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import packages


# In[ ]:


# set working directory


# In[ ]:


# read file


# In[ ]:


tokenized_words=[]
lemmatized_token_d2=[]
stop_words_removed=[]

lemmatizer = nltk.stem.WordNetLemmatizer()


# In[ ]:


for i in range(len(tweet_list)):
    #tokenize each review in the collection
    tokenized_words.append(nltk.word_tokenize(tweet_list[i].lower()))
   
    #removing all the stop-words and the punctuations
    stop_words_removed.append([token for token in tokenized_words[i] if not token in stopwords.words('english') if token.isalpha()])

    #lemmatize all the tokens created in the previous step
    lemmatized_token_d2.append([lemmatizer.lemmatize(token) for token in stop_words_removed[i] if token.isalpha()])

#each of the tokens, after stop words removal, is converted to string
lemmatized_string=[]
for i in lemmatized_token_d2:
    lemmatized_string.append(" ".join(i))


# In[ ]:


# lines_list = tokenize.sent_tokenize(paragraph)
# sentences.extend(lines_list)
nltk.download('vader_lexicon')


from nltk.sentiment.vader import SentimentIntensityAnalyzer #gives a score to all the sentence
sid=SentimentIntensityAnalyzer()
a=[]
for sentence in lemmatized_string:
    print(sentence)
    #ss is a dictionary
    ss = sid.polarity_scores(sentence) #calculate score for sentence
    a.append(ss)
#     for k in sorted(ss): #k is the key
        
#         print('{0}: {1}, '.format(k, ss[k]), end='') #print score along with results
#         print()


# In[ ]:


sen_list = []
for i in range(len(a)):
    data = a[i].get("compound", "")
    sen_list.append(data)
    


# In[ ]:


import pandas as pd
df1 = pd.DataFrame(tweet_list,columns=['tweets'])


# In[ ]:


df2 = pd.DataFrame(sen_list,columns=['sen_score'])


# In[ ]:


a=dataset['news'].tolist()


# In[ ]:


b = [i.replace('-filter:retweets','') for i in a]


# In[ ]:


dataset["news"] = b


# In[ ]:


dataset = pd.concat([outputdf['news'].reset_index(drop=True),df1.reset_index(drop=True),df2.reset_index(drop=True)], axis=1)


# In[ ]:


dataset = dataset.set_index("news")


# In[ ]:


dataset.to_csv('final_sent.csv')


# In[ ]:




