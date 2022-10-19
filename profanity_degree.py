import pandas as pd
import re

#for example the tweets are stored in a csv file with each tweet being stored in a single row
#each tweet is a single line only, i.e. no \n is present or is already removed.
#let the name of the file be filename.csv

df=pd.read_csv('filename.csv')   
df['racism_degree'] = 0 #let it be last column
racist = ...

def clean():
    '''
    Function to clean tweet by removing links, special characters, etc. by using regex
    It returns a tokenised data
    '''
    def clean_tweet(tweet):
        '''
        This is a utility function, created to improve readability
        which can be changed based on requirement
        '''
        #after substitution the text is split by spaces as delimiter, multiple whitespace is considered as one
        #they are then joined back into a list using join function
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    #let the name of the column that stores the tweets be 'tweets' and it is the first column of the dataset
    for i in range(len(df)):
        df.iloc[i,0]=clean_tweet(df.iloc[i,0])


def racism(tweet):
    #let the given racial slurs be present in a global list called racist
    #let r be an integer which will store the number of slur words used in each tweet
    #I assume that the racist word used will be written as a whole without censoring
    tweet = tweet.split()
    r=0
    for i in tweet:
        if i in racist:
            r=r+1
    #this statement will calculate the percentage of profanity in each sentence        
    return (r*100)/len(tweet)        


clean()

for i in range(len(df)):
    df.iloc[i,-1]=racism(df.iloc[i,-1])