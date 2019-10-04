# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 16:38:57 2019

@author: Skad
"""

def fun(wordToSearch, arrayData_txt, arrayRes):
    i = 0    
    for x in arrayData_txt:
        if (wordToSearch in arrayData_txt):
            arrayRes.append(1)
        else:
            arrayRes.append(0)
        i = 1 + i
        
def splitTweet(pdDataColumn, arraySplitTweet = []):
    for x in pdDataColumn:
        arraySplitTweet.append(str(x).split())    