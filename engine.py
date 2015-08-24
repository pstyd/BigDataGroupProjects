from pandas import *
from sentianal import Sentianal
from normalizer import Normalizer
from stpremoval import StpRemoval
import numpy as numpy

import matplotlib.pyplot as plt

sourcefile = "jokowitweet.txt"

#dump the sourcefile into dataframe
fin = open(sourcefile,'r')
tweet = []

for line in fin:
	line = line.strip()
	tweet.append(line)

#store in dataframe
jkw_data = DataFrame(tweet)

#rename the column
jkw_data.columns = ['tweet']

#score the tweet
score = []

#create normalizer object
norm = Normalizer()

#create Stop word Removal object
st = StpRemoval()

#create sentiment analysis object
s = Sentianal()

for i in range(0,len(jkw_data)):
	#normalize
	line = norm.normalize(jkw_data['tweet'][i])
	
	#remove stopword
	line = st.removeStp(line)

	#score sentiment
	score.append(s.compute(line))

#join the dataframe
score_data = DataFrame(score)
jkw_data = jkw_data.join(score_data)
jkw_data.columns = ['tweet_processed','score']

#write to csv file
jkw_data.to_csv("score_jokowi2.csv")

#try to find common words