# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 12:06:07 2019

@author: Skad, toujours ce même skad
"""
import pandas as pd  
from past.builtins import execfile
import os

include('C:\\Users\\Skad\\.spyder-py3\\test_nlp_classif.py')

ref_positive = ('like', 'love', 'great', 'good','interesting', 'cool')
ref_negative = ('overated', 'bad', 'sad', 'worst', 'wrong', 'hate', 'dislike')
    
###############################################################"
df = pd.read_csv('C:\\Users\\Skad\\Desktop\\Python\\testdata.txt',sep='delimiter',names=['txt'],engine='python')
df_neg = pd.read_csv('C:\\Users\\Skad\\Desktop\\Python\\testdata.txt',sep='delimiter',names=['txt'],engine='python')
# engin python is to let the ""compiler"" know that the C parser is not needed, that enable a warning Parserwarning

#Tweets = [df['txt'][0],df['txt'][1],df['txt'][2],df['txt'][3],df['txt'][7],df['txt'][94],,df['txt'][940]]


#def match_word(txt, word):
#    return int(word in txt)

df['love_in_txt'] = df.txt.apply(match_word, args=("love",))


for word in list(ref_positive):
    df['%s_in_txt'%word] = df.txt.apply(match_word, args=(word,))
    df['%s_occur'%word] = df.txt.apply(count_word, args=(word,))
    
for word in list(ref_negative):
    df_neg['%s_in_txt'%word] = df.txt.apply(match_word, args=(word,))  
    df_neg['%s_occur'%word] = df.txt.apply(count_word, args=(word,))

#print(arraySplitTweet)

#like, love, great, good, interesting, cool
#much
