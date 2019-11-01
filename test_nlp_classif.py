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
    
#in order to factorize the code with "apply", instead of foreach
def splitTxtAndGrade(strTxt,strGrade):
    strGrade = strTxt.split()[0]
    strTxt = strTxt[1:]
        
def splitTweet(pdDataColumn, arraySplitTweet = []):
    for x in pdDataColumn:
        arraySplitTweet.append(str(x).split())    
        
def match_word(txt, word, weigh = 1):
    return weigh * int(word in txt)       

def count_word(txt, word):
    return txt.count(word)

def indicatrice(x):
    if(x>0):
        return 1
    else:
        return 0
dfTweets = pd.read_csv('C:\\Users\\Skad\\Desktop\\Python\\testdata.txt',sep='delimiter',names=['txt'],engine='python')
# engin python is to let the ""compiler"" know that the C parser is not needed, that enable a warning Parserwarning
i = 0
for tweet in dfTweets.txt:# <=> dfTweets['txt']
    #df.txt.apply(lower, args=())??
    dfTweets['txt'].at[i]  = dfTweets['txt'].at[i].lower()
    i = i + 1



def ClassifyTweet(pdDataColumn, ref_positiveWithWeigh, ref_negativeWithWeigh):
    del(pdDataColumn)
    pdDataColumn = dfTweets
    res = pdDataColumn.txt
    for word, values in ref_positiveWithWeigh.items():
        pdDataColumn['grade_%s'%word] = res.apply(match_word, args=(word,values,))     
    for word in list(ref_negativeWithWeigh):
        pdDataColumn['grade_%s'%word] = res.apply(match_word, args=(word,-1,))  
    outpdClassifier = pdDataColumn.sum(axis = 1, skipna = True)   
    print("output", outpdClassifier)
    return [indicatrice(grade) for grade in outpdClassifier]
























