import matplotlib.pyplot as plt

# Assuming you have a list of trend names and their tweet volumes
trend_names = ['Trend 1', 'Trend 2', 'Trend 3']
tweet_volumes = [1000, 2000, 1500]

plt.barh(trend_names, tweet_volumes)
plt.xlabel('Tweet Volume')
plt.ylabel('Trending Topics')
plt.title('Twitter Trends')
plt.show()
