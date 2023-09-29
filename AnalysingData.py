import tweepy

# Your authentication and API setup here...

# Define a function to analyze tweets
def analyze_tweets(query, num_tweets):
    # Create an empty list to store tweet texts
    tweets = []

    try:
        # Use the Cursor method to search for tweets
        for tweet in tweepy.Cursor(api.search, q=query, tweet_mode='extended').items(num_tweets):
            # Extract and store the tweet text
            tweets.append(tweet.full_text)

        # Perform your analysis on the collected tweets
        for tweet in tweets:
            # Example: Print each tweet
            print(tweet)

    except tweepy.TweepError as e:
        print("Error: " + str(e))

# Example usage:
query = "your_search_query"
num_tweets = 10  # Number of tweets to retrieve
analyze_tweets(query, num_tweets)
