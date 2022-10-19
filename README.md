
# Affinity Answers


### 1. Imagine there is a file full of Twitter tweets by various users and you are provided a set of words that indicates racial slurs. Write a program that can indicate the degree of profanity for each sentence in the file. Write in any programming language (preferably in Python)-make any assumptions, but remember to state them. Please place the code in GitHub with proper documentation and share. 

**Ans:**
* I have assumed that the data provided is a csv file, with the name filename.csv
* Each tweet is present in the csv file at the first column.
* Each tweet is in a single line only, i.e. no `\n`, if present has been removed.
```python
import pandas as pd
import re

#for example the tweets are stored in a csv file with each tweet being stored in a single row
#each tweet is a single line only, i.e. no \n is present or is already removed.
#let the name of the file be filename.csv

df=pd.read_csv('filename.csv')   
df['racism_degree'] = 0 #let it be last column
```
> Created a new column and initialised it to `0` to store the degree of racism as a percentage.
> I am using pandas to easily manipulate csv files, and regex to clean data.

* I have assumed that the tweets data is available in the first column of the csv file.
* Each tweet is in a single line, without any `\n`.
* I assume that there are no racial slurs in the links, or mentions.
* Racial slurs are not censored by special symbols, and are used exactly how they appear in the set of words provided.
* I assume that the tweets and the set of racial slurs are all in lower case.
```python
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
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    #let the name of the column that stores the tweets be tweets and it is the first column of the dataset
    for i in range(len(df)):
        df.iloc[i,0]=clean_tweet(df.iloc[i,0])
```
> This function is used to clean the tweets to remove the links, mentions, and special characters.
> Each tweet from each row is passed to the `clean_tweet` function to clean the data.
> I have used a separate `clean_tweet` function to improve readability of the code, and to allow code reusability and easy to modify based on requirement.

* I have assumed that the racial slurs are globally available in a variable called `racist`.
*  The racial slurs are not censored and available exactly how it is provided in the racial slurs set. Eg: `black` in the tweet will be exactly available in the `racist` variable. It will not be present in any other forms, such as `b***k`.
```python
def racism(tweet):
    #let the given racial slurs be present in a global set called racist
    #let r be an integer which will store the number of slur words used in each tweet
    #I assume that the racist word used will be written as a whole without censoring
    tweet=tweet.split(" ")
    r=0
    for i in tweet:
        if i in racist:
            r=r+1
    #this statement will calculate the percentage of profanity in each sentence        
    return (r*100)/len(tweet)   
```
> In this function, each word in a tweet is checked if it is a racial slur, and the counter `r` is increased if it encounters a racial slur.
> `r` holds the number of slur words used in each tweet, so the percentage of profanity can be given by $\frac{r}{num\ of\ words\ in\ tweet} * 100$
> This is the percentage of words that are racial slurs in the tweet.
> Eg: for a tweet of length 10, if 3 racial slurs occur, then it will be 30% profane. Similarly, for the same word length, if a single racial slur occurs `n` times, then the profanity will be `n * 10%`.

```python
clean()
for i in range(len(df)):
     df.iloc[i,-1]=racism(df.iloc[i,-1])
```
> After function declaration is done and the dataset is loaded, the clean function will execute the cleaning process to remove the links, mentions, and special characters.
> The loop will then run to calculate the degree of profanity, measured in terms of percentages.
<hr>

### 2. Which is an interesting data set you discovered recently? Why is it your favorite? No datasets on Kaggle, please. 

**Ans:** I recently came across this dataset on the website of the Government of the UK which contains data on the trends of people washing their hands during the recent COVID - 19 pandemic. Data was collected quarterly starting from April 2020. 

As someone very particular about hygiene, especially cleaning my hands before eating food I find this dataset very interesting. People were grouped according to their geographical location, gender, marital status etc to name a few and were asked a variety of questions like if they wash their hands after contact with animals.
 
The data is primarily numerical and the collection was performed per International standards of market research like ISO 20252 and with the Ipsos MORI Terms and Conditions.
[Link to Data](https://www.data.gov.uk/dataset/1f9e8832-d668-43ff-9511-d01f8ce0af22/handwashing-consumer-tracker)

---

### 3. Why do we need a database? We can store everything in a file, no? 
**Ans:** Databases are more structured than files. When we use databases we have many RDBMS systems which help us quickly access and manipulate data. It also helps in managing the large size of data. These systems have many useful features including the data saving feature which helps in case of a system crash.  

Many programming languages have special libraries to handle databases quickly.  A database has security built into it with access rights and it also helps to store different types of data in a single place. The integrity of data stored in a database is never lost due to its ACID properties.

---
### 4. How well versed are you on the Unix command line?

**Ans:** I have basic proficiency in Unix. I recently completed a training session on UNIX commands and I have a bit of experience using these commands hands-on as well. I am constantly trying to do most of my work through the command line to improve my Unix skills.
