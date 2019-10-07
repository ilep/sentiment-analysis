# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 12:06:07 2019

@author: Skad, toujours ce même skad
"""
import pandas as pd  
from past.builtins import execfile
import os

include('C:\\Users\\Skad\\.spyder-py3\\test_nlp_classif.py')

#ref_positive = frozenset('like', 'love', 'great', 'good','interesting', 'cool')
#ref_negative = frozenset('overated', 'bad', 'sad', 'worst', 'wrong')
    
###############################################################"
df = pd.read_csv('C:\\Users\\Skad\\Desktop\\Python\\testdata.txt',sep='delimiter',names=['txt'],engine='python')
# engin python is to let the ""compiler"" know that the C parser is not needed, that enable a warning Parserwarning

#Tweets = df['txt']
Tweets = [df['txt'][0],df['txt'][1],df['txt'][2],df['txt'][3],df['txt'][5],df['txt'][94]]
arraySplitTweet = []
splitTweet(Tweets, arraySplitTweet)
#print(arraySplitTweet)

##### Tweets that contain "like"
arrayLike = []
arrayLove = []
fun('like', arraySplitTweet, arrayLike)
fun('love', arraySplitTweet, arrayLove)
print("array like\n", arrayLike)
print("array love\n", arrayLove)
print(df['txt'][4])

#print(arraySplitTweet)

#like, love, great, good, interesting, cool
#much