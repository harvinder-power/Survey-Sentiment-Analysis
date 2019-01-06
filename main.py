try:
    from pip import main as pipmain
except ImportError:
    from pip._internal import main as pipmain

def install(package):
	pipmain(['install', package])

# Example
if __name__ == '__main__':
    install('vaderSentiment')
    install('pandas')


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

#Initialise analyser function
analyser = SentimentIntensityAnalyzer()

#Basic sentiment analysis with score being returned
def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print (score)
    return (score)

#Replace #### with filename
#Assumes that only a one-column file format with data in column 1
df = pd.read_excel('/Users/harvinderpower/Desktop/positive_comments.xlsx')

#Initialises lists for metrics
neg_list = []
neu_list = []
pos_list = []
compound_list = []

#Initialises empty columns for metrics
df['neg'] =""
df['neu'] =""
df['pos'] =""
df['compound'] =""


#Iterates over length of data to analyse, and then put values into lists
for i in range(len(df)):
  results = (sentiment_analyzer_scores(df.iloc[i][0]))
  neg_list.append(results['neg'])  
  neu_list.append(results['neu'])
  pos_list.append(results['pos'])
  compound_list.append(results['compound'])

#Adds the values from the list into the excel spreadsheet.
series_neg = pd.Series(neg_list)
df['neg'] = series_neg.values

series_neu = pd.Series(neu_list)
df['neu'] = series_neu.values


series_pos = pd.Series(pos_list)
df['pos'] = series_pos.values

series_compound = pd.Series(compound_list)
df['compound'] = series_compound.values

df.to_excel('./output.xlsx')