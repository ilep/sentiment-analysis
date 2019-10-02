#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:54:12 2019

@author: ivanlptr
"""

'''
kaggle michigan competition
http://konukoii.com/blog/2018/02/19/twitter-sentiment-analysis-using-combined-lstm-cnn-models/


Stanford sentiment treebank data 
https://towardsdatascience.com/sentiment-analysis-for-text-with-deep-learning-2f0a0c6472b5


Sentiment 140
http://help.sentiment140.com/for-students/


'''

import os
import pandas

WD = r'/Users/lantian/Desktop/Ivan/travail/sentiment analysis/'
os.chdir(WD)


DATA_FOLDER = WD + 'data/'  

df = pandas.read_table('%s%s' % (DATA_FOLDER, 'michigan_kaggle_training.txt'), 
                       names=['sentiment', 'txt'])

df_stanford = pandas.read_table('%s%s' % (DATA_FOLDER, 'stanfordSentimentTreebank/datasetSentences.txt'),
                                index_col='sentence_index')

df_sentiment = pandas.read_table('%s%s' % (DATA_FOLDER, 'stanfordSentimentTreebank/sentiment_labels.txt'))
















