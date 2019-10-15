# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 12:06:07 2019

@author: Skad, toujours ce même skad
"""
import pandas as pd  
from past.builtins import execfile
import os
import numpy as np

include('C:\\Users\\Skad\\.spyder-py3\\test_nlp_classif.py')

ref_positive = ('like', 'love', 'great', 'good','interesting', 'cool')
ref_positiveWithWeigh = {"like":2, "love":5, "great":5,"good":2, "interesting":0.5, "cool":1, }
ref_negativeWithWeigh = {"overated":-4, "bad":-5,"stupid":-5, "sad":-5, "worst":-5, "wrong":-5, "hate":-5, "dislike":-5}
    
###############################################################
dfTweets = pd.read_csv('C:\\Users\\Skad\\Desktop\\Python\\testdata.txt',sep='delimiter',names=['txt'],engine='python')
# engin python is to let the ""compiler"" know that the C parser is not needed, that enable a warning Parserwarning


i = 0
for tweet in dfTweets.txt:# <=> dfTweets['txt']
    #df.txt.apply(lower, args=())??
    dfTweets['txt'].at[i]  = dfTweets['txt'].at[i].lower()
    i = i + 1

#Tweets = [df['txt'][0],df['txt'][1],df['txt'][2],df['txt'][3],df['txt'][7],df['txt'][94],,df['txt'][940]]

"""for word in list(ref_positiveWithWeigh):
    dfTweets['%s_in_txt'%word] = dfTweets.txt.apply(match_word, args=(word,))
    #dfTweets['%s_occur'%word] = dfTweets.txt.apply(count_word, args=(word,))
   
for word in list(ref_negativeWithWeigh):
    dfTweets['%s_in_txt'%word] = dfTweets.txt.apply(match_word, args=(word,))  
    
    #dfTweets['%s_occur'%word] = dfTweets.txt.apply(count_word, args=(word,))
    """
res = dfTweets    
for word, values in ref_positiveWithWeigh.items():
    res['grade_%s'%word] = dfTweets.txt.apply(match_word, args=(word,values,))     
    #df['grade'] = df.txt.apply(match_word, args=(word.keys(),int(word.values())))
    
for word in list(ref_negativeWithWeigh):
    res['grade_%s'%word] = dfTweets.txt.apply(match_word, args=(word,))  

res.sum(axis = 1, skipna = True)    

#print(arraySplitTweet)

#like, love, great, good, interesting, cool
#much
