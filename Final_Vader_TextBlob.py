# Authors      : Nicholas S., Michael H.
# Program Name : Vader_TextBlob
# Last Edited  : 05/02/23
# Description  : This program use vader and textblob to conduct
# sentiment analysis on a number of tweets from the Patriots,
# Chiefs, Bills, Cowboys, Giants, Raiders, Chargers, Cardinals,
# Lions, and the Browns. The total number of positive, negative,
# and neutral tweets are counted for each team and displayed.
# Each teams summed sentiment scores are also displayed. The winners
# are decided by subtracting the total positive tweets by the
# negative tweets for each method of analysis.
# ------------------------------------------------------------------
# Imports
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

# This function gets the average vader score of a list of tweets
def Average_Vader_Scores(sia, tweet_list):
    # Initialize scores
    scores = {'neg': 0, 'neu': 0, 'pos': 0, 'compound': 0}
    # For each tweet in the list
    for tweet in tweets_list:
        # Get polarity score
        ss = sia.polarity_scores(tweet)
        # Each score to scores
        for k in scores.keys():
            scores[k] += ss[k]
    # Get length of list
    n = len(tweet_list)
    # Return average score list
    return {k: v/n for k, v in scores.items()}
# END Average_Vader_Scores

# Main
if __name__ == '__main__':
    # Download the NLTK data
    nltk.download('vader_lexicon')
    nltk.download('punkt')
    # Get the NLTK sentiment analyzer
    sia = SentimentIntensityAnalyzer()

    # Initialize list of files being read and team list
    teamList = ['Patriots', 'Chiefs', 'Bills', 'Cowboys', 'Giants', 'Raiders',
                'Chargers', 'Cardinals', 'Lions', 'Browns']
    tweet_files = ['PatriotsData.csv', 'ChiefsData.csv', 'BillsData.csv', 'CowboysData.csv', 'GiantsData.csv',
                   'RaidersData.csv', 'ChargersData.csv', 'CardinalsData.csv', 'LionsData.csv', 'BrownsData.csv']

    # Initialize current team to 0
    currentTeam = 0

    # FOR each file in tweet files
    for file in tweet_files:
        # Read file and convert tweets column into list
        df = pd.read_csv(file)
        tweets_list = df['tweets'].tolist()
        # DEBUG print list
        # print(tweets_list)

        # Initialize total text blob score
        total_textblob_score = 0

        # Initialize neutral, positive, and negative count to 0
        # for vader, textblob, and both
        total_vader_neutral = 0
        total_vader_positive = 0
        total_vader_negative = 0
        total_textblob_neutral = 0
        total_textblob_positive = 0
        total_textblob_negative = 0
        total_both_neutral = 0
        total_both_positive = 0
        total_both_negative = 0

        # For each tweet in tweets list
        for tweet in tweets_list:
            # Get sentiment scores
            res = TextBlob(tweet)
            sentiment_scores = sia.polarity_scores(tweet)
            # DEBUG print tweet and sentient score
            # print("Tweet: ", tweet)
            # print("Text Blob Scores: ", res.sentiment.polarity)
            # print("Vader Sentiment Scores: ", sentiment_scores)

            # Add textblob score to total
            total_textblob_score += res.sentiment.polarity

            # Vader
            # DEBUG print vader says
            # print("Vader says...")
            # Classify tweet as positive, negative, or neutral based on compound score
            if sentiment_scores['compound'] > 0.1:
                # Increment positive by 1
                total_vader_positive += 1
                # DEBUG print positive
                # print("Sentiment: Positive")
            elif sentiment_scores['compound'] < -0.1:
                # Increment negative by 1
                total_vader_negative += 1
                # DEBUG print negative
                # print("Sentiment: Negative")
            else:
                # Increment neutral by 1
                total_vader_neutral += 1
                # DEBUG print neutral
                # print("Sentiment: Neutral")
            # END IF
            # DEBUG print space line
            # print("---------")

            # Textblob
            # DEBUG textblob says
            # print("Textblob says...")
            # Classify tweet as positive, negative, or neutral based on compound score
            if res.sentiment.polarity > 0:
                # Increment positive by 1
                total_textblob_positive += 1
                # DEBUG print positive
                # print("Sentiment: Positive")
            elif res.sentiment.polarity < 0:
                # Increment negative by 1
                total_textblob_negative += 1
                # DEBUG print negative
                # print("Sentiment: Negative")
            else:
                # Increment neutral by 1
                total_textblob_neutral += 1
                # DEBUG print neutral
                # print("Sentiment: Neutral")
            # END IF
            # DEBUG print space line
            # print("---------")

            # Vader and Textblob
            # DEBUG print vader and textblob says
            # print("Vader and Textblob says...")
            # Classify tweet as positive, negative, or neutral based on compound score
            if sentiment_scores['compound'] > 0.1 and res.sentiment.polarity > 0:
                # Increment positive by 1
                total_both_positive += 1
                # DEBUG print positive
                # print("Sentiment: Positive")
            elif sentiment_scores['compound'] < -0.1 and res.sentiment.polarity < 0:
                # Increment negative by 1
                total_both_negative += 1
                # DEBUG print negative
                # print("Sentiment: Negative")
            else:
                # Increment neutral by 1
                total_both_neutral += 1
                # DEBUG print neutral
                # print("Sentiment: Neutral")
            # END IF
            # DEBUG print space line
            # print("---------")
        # END FOR

        # Print sentiment total's for current team
        print(teamList[currentTeam] + "\n" +
              "Total Vader Score Sentiment: " + str(Average_Vader_Scores(sia, tweets_list)) + "\n" +
              "Total Textblob Score Sentiment: " + str(total_textblob_score/len(tweets_list)) + "\n" +
              "---------------------------------------------"   + "\n" +
              "Vader" + "\n" +
              "Total Positive :" + str(total_vader_positive)    + "\n" +
              "Total Negative :" + str(total_vader_negative)    + "\n" +
              "Total Neutral  :" + str(total_vader_neutral)     + "\n" +
              "---------------------------------------------"   + "\n" +
              "Textblob" + "\n" +
              "Total Positive :" + str(total_textblob_positive) + "\n" +
              "Total Negative :" + str(total_textblob_negative) + "\n" +
              "Total Neutral  :" + str(total_textblob_neutral)  + "\n" +
              "---------------------------------------------"   + "\n" +
              "Vader and Textblob" + "\n" +
              "Total Positive :" + str(total_both_positive)     + "\n" +
              "Total Negative :" + str(total_both_negative)     + "\n" +
              "Total Neutral  :" + str(total_both_neutral)      + "\n\n")

        # Get number of supporters
        vader_num_supp = total_vader_positive - total_vader_negative
        textblob_num_supp = total_textblob_positive - total_textblob_negative
        both_num_supp = total_both_positive - total_both_negative
        # DEBUG print number of supporters
        # print(str(vader_num_supp) + " " + str(textblob_num_supp) + " " + str(both_num_supp))

        # Check if there's a new winner
        if teamList[currentTeam] == teamList[0]:
            # Initialize winner
            vader_winner = (teamList[currentTeam], vader_num_supp)
            textblob_winner = (teamList[currentTeam], textblob_num_supp)
            both_winner = (teamList[currentTeam], both_num_supp)
        # ELSE check for new winner
        else:
            if vader_num_supp > vader_winner[1]:
                vader_winner = (teamList[currentTeam], vader_num_supp)
            if textblob_num_supp > textblob_winner[1]:
                textblob_winner = (teamList[currentTeam], textblob_num_supp)
            if both_num_supp > both_winner[1]:
                both_winner = (teamList[currentTeam], both_num_supp)
        # END IF

        # Increment current team by
        currentTeam += 1
    # END FOR

    # Print winners
    print("Vader says..." + vader_winner[0] + " will win!\n" +
          "Textblob says..." + textblob_winner[0] + " will win!\n" +
          "Both say..." + both_winner[0] + " will win!\n")
# END main