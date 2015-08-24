#engine 2: calculating sentiment of tweets that contain top words
#Script for computing top-N unigram

from collections import Counter
from pandas import * 
import numpy
import re

############### You can modify this part ##############

fileName = "jokowitweet.txt"
topN     = 50

#######################################################

fin = open(fileName, "r")
words = re.findall('\w+', fin.read())

c = Counter(words)
kv = c.most_common(topN)

#tranform into data frame

common_word = DataFrame(kv)

#rename
common_word.columns = ['word','count']

#averaging the sentiment words

#retrieve the data
data = read_csv("score_jokowi2.csv")

#calculate the average sentiment
avg_score = []

for i in range(0,len(common_word)):
	#find the indices
	indices = [j for j,s in enumerate(data['tweet_processed']) if common_word['word'][i] in s]
	avg_score.append(numpy.mean(data['score'][indices]))

#transform the avg_score into dataframe
avg_score = DataFrame(avg_score)

common_word2 = common_word.join(avg_score)
common_word2.columns = ['word','count','avg_score']

#write to csv file
common_word2.to_csv("word_jkw_score.csv")

#for k,v in kv:
#   print(k, v)