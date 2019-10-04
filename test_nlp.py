# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 12:06:07 2019

@author: Skad, toujours ce même skad
"""
import pandas as pd  
from past.builtins import execfile
import os

def include(filename):
    if os.path.exists(filename): 
        execfile(filename)
include('C:\\Users\\Skad\\.spyder-py3\\test_nlp_classif.py')

ref_positive = ('like', 'love', 'great', 'good','interesting', 'cool')
ref_negative = ('overated', 'bad', 'sad', 'worst', 'wrong')
    
###############################################################"
df = pd.read_csv('C:\\Users\\Skad\\Desktop\\Python\\testdata.txt',sep='delimiter',names=['txt'],engine='python')
# engin python is to let the ""compiler"" know that the C parser is not needed, that enable a warning Parserwarning
Tweets = df['txt']
arraySplitTweet = []
splitTweet(Tweets, arraySplitTweet)

##### Tweets that contain "like"
arrayLike = []
fun('like', arraySplitTweet, arrayLike)
print(arrayLike)
print("ici")

#print(arraySplitTweet)

#like, love, great, good, interesting, cool
#much