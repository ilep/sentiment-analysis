# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 16:38:57 2019

@author: Skad
"""

def include(filename):
    if os.path.exists(filename): 
        execfile(filename)

def fun(wordToSearch, arrayData_txt, arrayRes, weigh = 1):
    #Loop in the data , everytime the wordToSearch is find the output is incremented with weigh
    i = 0    
    for x in arrayData_txt:
        y = frozenset(x)  #use of set in order to speed up the search
        if (wordToSearch in y):
            arrayRes.append(weigh)
        else:
            arrayRes.append(0)
        i = 1 + i
        
def splitTweet(pdDataColumn, arraySplitTweet = []):
    #
    for x in pdDataColumn:
       # y = str(x).lower()
        arraySplitTweet.append(str(x).split())    